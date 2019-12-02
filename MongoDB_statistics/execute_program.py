# -*- coding: utf-8 -*-
from pymongo import MongoClient
import csv,numpy,configparser,os
#============================勿动这个文件==============================
#============================勿动这个文件==============================
#============================勿动这个文件==============================

# 连接MongoDB数据库中collection。
def collect():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    config.read(parent_dir + '/config.ini')
    db_host = config.get('mongo', 'host')
    db_name = config.get('mongo', 'dbname')
    db_collection = config.get('mongo', 'collection')
    db = MongoClient(db_host)[db_name]
    collection = db[db_collection]
    return collection

# (一)、抽取部分数据
# 1.1 取出前N条数据，并存入MongoDB同目录新collection。
def query_data1(collection_name,number):
    collection2 = collect()[collection_name]
    for item in collect().find().limit(number):
        collection2.insert_one(item)
    print("完成1.1")

# 1.2 随机取出N条数据，并存入MongoDB同目录新collection。
def query_data2(collection_name,number):
    collection2 = collect()[collection_name]
    for item in collect().aggregate([{'$sample': {"size": number}}]):#这个语句还可以加限制条件
        collection2.insert_one(item)
    print("完成1.2")

# 1.3 条件筛选取出部分字段(非集合字段)，并将结果保存至csv。
def query_data3(dict,columns,csv_name):
    dict2 = {}
    for i in columns:
        dict2[i]=1
    file = csv_name + '.csv'
    headers = columns
    listing = []
    for item in collect().find(dict, dict2):
        listing1 = []
        for i in columns:
            listing1.append(item[i])
        listing.append(listing1)
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成1.3，已将结果保存至", file)

# 1.4 条件筛选取出部分字段(含集合字段)，并存入MongoDB同目录新collection。
def query_data4(dict,columns,collection_name):
    dict2 = {}
    for i in columns:
        dict2[i] = 1
    collection2 = collect()[collection_name]
    for item in collect().find(dict, dict2):
        collection2.insert_one(item)
    print("完成1.4，已将结果保存至MongoDB", collection_name)

# (二)、提取字段值
# 2.1 提取字段(含集合字段)的前几位字符(一个汉字、单词、数字、标点算一个字符)存入新字段。
def tag_field1(original_field,number,result_field):#处理字段名称，提取前几位，生成字段名称
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            listing = []
            if original_field in item:
                for word in item[original_field]:
                    word_former = word[:number]
                    listing.append(word_former)
                result = list(set(listing))
                collect().update_many({"_id": item["_id"]}, {"$set": {result_field : result}})
    print("完成2.1")

# 2.2 提取满足条件的字段值存入新字段
def tag_field2(field_name,flag_if,flag_field):
    dict = {"_id":"$_id"}
    dict[field_name] = "$"+field_name
    for item in collect().aggregate([{"$match":flag_if},{"$group":{'_id': dict,"count": {"$sum": 1}}}]):
        collect().update_many({"_id": item["_id"]["_id"]}, {"$set": {flag_field: item['_id'][field_name]}})
    print("完成2.2")

# (三)、分析字段值
# 3.1 返回数值字段(非集合字段)有值个数、最大值、最小值、均值、中位数
def value_analysis(original_field):
    values = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value=float(item[original_field])
                #if b>0:
                values.append(value)
            except:
                pass
    print("len",len(values))
    print("max",max(values))
    print("min",min(values))
    print("mean",numpy.mean(values))
    print("median",numpy.median(values))

# (四)、打标签
# 4.1 值的双范围标签(非集合字段)，通常用于时间、金额等可以进行比较的字段
def tagged1(field_name,value,value_flag_ahead,value_flag_after,flag_field):
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value1 = float(item[field_name])
                if value1 <= value:
                    collect().update_many({"_id": item["_id"]}, {"$set": {flag_field: value_flag_ahead}})
                else:
                    collect().update_many({"_id": item["_id"]}, {"$set": {flag_field: value_flag_after}})
            except:
                pass
    print("完成4.1")

# 4.2 值的多范围标签(非集合字段,前包后不包)，通常用于时间、金额等可以进行比较的字段
def tagged2(field_name,flag_list,flag_name):
    flag_list1 = []
    flag_list2 = []
    flag_list3 = []
    for i in flag_list:
        flag_list1.append(list(i.keys())[0])
        flag_list2.append(list(i.values())[0][0])
        flag_list3.append(list(i.values())[0][1])
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[field_name])
                for i in range(len(flag_list1)):
                    if flag_list2[i] <= value < flag_list3[i]:
                        collect().update_many({"_id": item["_id"]}, {"$set": {flag_name: flag_list1[i]}})
                        break
            except:
                pass
    print("完成4.2")

# 4.3 值的条件标签
def tagged3(field_name,flag_if,flag_text,flag_field):
    dict = {"_id":"$_id"}
    dict[field_name] = "$"+field_name
    for item in collect().aggregate([{"$match":flag_if},{"$group":{'_id': dict,"count": {"$sum": 1}}}]):
        collect().update_many({"_id": item["_id"]["_id"]}, {"$set": {flag_field: flag_text}})
    print("完成4.3")

# 4.4 全字段搜索是否包含关键词，只要有关键词组中的一个就打上标签
def tagged4(flag_list,flag_name):
    flag_list1 = []
    flag_list2 = []
    for i in flag_list:
        flag_list1.append(list(i.keys())[0])
        flag_list2.append(list(i.values())[0])
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            text = str(item)
            flag_list3 = []
            for i in range(len(flag_list1)):
                for flag_word in flag_list2[i]:
                    value = (text.find(flag_word))
                    if value > 0:
                        flag_list3.append(flag_list1[i])
                        break
            if len(flag_list3) > 0:
                collect().update_many({"_id": item["_id"]}, {"$set": {flag_name: flag_list3}})
    print("完成4.4")

# 4.5 部分字段搜索是否包含关键词，只要有关键词组中的一个就打上标签
def tagged5(flag_list,flag_name,columns):
    flag_list1 = []
    flag_list2 = []
    for i in flag_list:
        flag_list1.append(list(i.keys())[0])
        flag_list2.append(list(i.values())[0])
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            text = ""
            for k in columns:
                text += str(item[k])
            flag_list3 = []
            for i in range(len(flag_list1)):
                for flag_word in flag_list2[i]:
                    value = (text.find(flag_word))
                    if value > 0:
                        flag_list3.append(flag_list1[i])
                        break
            if len(flag_list3) > 0:
                collect().update_many({"_id": item["_id"]}, {"$set": {flag_name: flag_list3}})
    print("完成4.5")

# 4.6 全字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签
def tagged6(flag_list,flag_name):
    flag_list1 = []
    flag_list2 = []
    for i in flag_list:
        flag_list1.append(list(i.keys())[0])
        flag_list2.append(list(i.values())[0])
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            text = str(item) 
            flag_list3 = []
            for i in range(len(flag_list1)):
                bools = []
                for flag_word in flag_list2[i]:
                    value = (text.find(flag_word))
                    if value > 0:
                        bools.append(True)
                    else:
                        bools.append(False)
                if all(bools):
                    flag_list3.append(flag_list1[i])
            if len(flag_list3) > 0:
                collect().update_many({"_id": item["_id"]}, {"$set": {flag_name: flag_list3}})
    print("完成4.6")

# 4.7 部分字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签
def tagged7(flag_list,flag_name,columns):
    flag_list1 = []
    flag_list2 = []
    for i in flag_list:
        flag_list1.append(list(i.keys())[0])
        flag_list2.append(list(i.values())[0])
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            text = ""
            for k in columns:
                text += str(item[k])
            flag_list3 = []
            for i in range(len(flag_list1)):
                bools = []
                for flag_word in flag_list2[i]:
                    value = (text.find(flag_word))
                    if value > 0:
                        bools.append(True)
                    else:
                        bools.append(False)
                if all(bools):
                    flag_list3.append(flag_list1[i])
            if len(flag_list3) > 0:
                collect().update_many({"_id": item["_id"]}, {"$set": {flag_name: flag_list3}})
    print("完成4.7")

# 4.8 两个字段(不含集合字段)值的运算(加减乘除)，并将结果存为新字段
def tagged8(column1,column2,arithmetic,flag_field):
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value1 = float(item[column1])
                value2 = float(item[column2])
                if arithmetic == "+":
                    value3 = value1 + value2
                elif arithmetic == "-":
                    value3 = value1 - value2
                elif arithmetic == "*":
                    value3 = value1 * value2
                elif arithmetic == "/":
                    value3 = value1 / value2
                elif arithmetic == "//":
                    value3 = value1 // value2
                collect().update_many({"_id": item["_id"]}, {"$set": {flag_field : value3 }})
            except:
                pass
    print("完成4.8")

# (五)、计数统计
# 5.1 普通字段的联合计数,并将结果保存至csv
def query_count1(columns,csv_name):
    dict = {}
    for i in range(len(columns)):
        header = "column"+str(i)
        value = "$"+columns[i]
        dict[header] = value 
    listing = []
    for item in collect().aggregate([{"$group": {"_id": dict, "count": {"$sum": 1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column"+str(i)]
            listing1.append(column_name)
        listing1.append(item["count"])
        listing.append(listing1)
    file = csv_name + '.csv'
    headers = columns + ["count"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成5.1,已将结果保存至",file)

# 5.2 一个集合字段的计数,并将结果保存至csv
def query_count2(column_set,csv_name):
    listing = []
    listing2 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                for i in item[column_set]:
                    if i in listing:
                        listing2[listing.index(i)] += 1
                    else:
                        listing.append(i)
                        listing2.append(1)
    listing3 = []
    for j in range(len(listing)):
        listing4 = []
        listing4.append(listing[j])
        listing4.append(listing2[j])
        listing3.append(listing4)
    file = csv_name + '.csv'
    headers = [column_set] + ["count"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing3)
    print("完成5.2,已将结果保存至", file)

# 5.3 一个集合字段和多个普通字段联合计数,并将结果保存至csv
def query_count3(column_set,columns,csv_name):
    listing=[]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                for i in item[column_set]:
                    if len(listing)==0:
                        info1 = []
                        for j in columns:
                            info1.append(item[j])
                        info1.append(i)
                        info1.append(1)
                        listing.append(info1)
                    else:
                        for k in listing:
                            bools = []
                            for m in range(len(columns)):
                                if k[m] == item[columns[m]]:
                                    bools.append(True)
                                else:
                                    bools.append(False)
                            if k[-2] == i:
                                bools.append(True)
                            else:
                                bools.append(False)
                            if all(bools):
                                k[-1]+=1
                                break
                        else:
                            info2 = []
                            for j in columns:
                                info2.append(item[j])
                            info2.append(i)
                            info2.append(1)
                            listing.append(info2)
    file = csv_name + '.csv'
    headers = columns + [column_set] + ["count"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成5.3,已将结果保存至", file)

# 5.4 一个集合字段和多个普通字段的联合计数，并存入MongoDB同目录新collection
def query_count4(column_set,columns,collection_name):
    collection2 = collect()[collection_name]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                for i in item[column_set]:
                    info = {}
                    for j in columns:
                        info[j] = item[j]
                    info[column_set] = i
                    if not collection2.find_one(info):
                        info["count"] = 1
                        collection2.insert_one(info)
                    else:
                        for item2 in collection2.find(info):
                            item2["count"] += 1
                            collection2.update_one(info,{"$set": {"count": item2["count"]}})
    print("完成5.4,已将结果保存至MongoDB", collection_name)

# (六)、求和统计
# 6.1 普通字段的联合求和,并将结果保存至csv
def query_sum1(columns_sum,columns,csv_name):
    dict = {}
    for i in range(len(columns)):
        header = "column" + str(i)
        value = "$" + columns[i]
        dict[header] = value
    listing = []
    value1 = "$" + columns_sum
    for item in collect().aggregate([{"$group": {"_id": dict, "sum": {"$sum": value1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column" + str(i)]
            listing1.append(column_name)
        listing1.append(item["sum"])
        listing.append(listing1)
    file = csv_name + '.csv'
    headers = columns + ["sum"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成6.1,已将结果保存至", file)

# 6.2 一个集合字段的求和,并将结果保存至csv
def query_sum2(columns_sum,column_set,csv_name):
    listing = []
    listing2 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_sum])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if i in listing:
                            listing2[listing.index(i)] += value
                        else:
                            listing.append(i)
                            listing2.append(value)
            except:
                pass
    listing3 = []
    for j in range(len(listing)):
        listing4 = []
        listing4.append(listing[j])
        listing4.append(listing2[j])
        listing3.append(listing4)
    file = csv_name + '.csv'
    headers = [column_set] + ["sum"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing3)
    print("完成6.2,已将结果保存至", file)

# 6.3 一个集合字段和多个普通字段的联合求和,并将结果保存至csv
def query_sum3(columns_sum,column_set,columns,csv_name):
    listing=[]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_sum])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if len(listing)==0:
                            info1 = []
                            for j in columns:
                                info1.append(item[j])
                            info1.append(i)
                            info1.append(value)
                            listing.append(info1)
                        else:
                            for k in listing:
                                bools = []
                                for m in range(len(columns)):
                                    if k[m] == item[columns[m]]:
                                        bools.append(True)
                                    else:
                                        bools.append(False)
                                if k[-2] == i:
                                    bools.append(True)
                                else:
                                    bools.append(False)
                                if all(bools):
                                    k[-1] += value
                                    break
                            else:
                                info2 = []
                                for j in columns:
                                    info2.append(item[j])
                                info2.append(i)
                                info2.append(value)
                                listing.append(info2)
            except:
                pass
    file = csv_name + '.csv'
    headers = columns + [column_set] + ["sum"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成6.3,已将结果保存至", file)

# 6.4 一个集合字段和多个普通字段的联合求和,并存入MongoDB同目录新collection
def query_sum4(columns_sum,column_set,columns,collection_name):
    collection2 = collect()[collection_name]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                try:
                    value = float(item[columns_sum])
                    for i in item[column_set]:
                        info = {}
                        for j in columns:
                            info[j] = item[j]
                        info[column_set] = i
                        if not collection2.find_one(info):
                            info["sum"] = value
                            collection2.insert_one(info)
                        else:
                            for item2 in collection2.find(info):
                                item2["sum"] += value
                                collection2.update_one(info,{"$set": {"sum": item2["sum"]}})
                except:
                    pass
    print("完成6.4,已将结果保存至MongoDB", collection_name)

# (七)、求平均值
# 7.1 普通字段的联合求均值,并将结果保存至csv
def query_avg1(columns_avg, columns, csv_name):
    dict = {}
    for i in range(len(columns)):
        header = "column" + str(i)
        value = "$" + columns[i]
        dict[header] = value
    listing = []
    value1 = "$" + columns_avg
    for item in collect().aggregate([{"$group": {"_id": dict, "avg": {"$avg": value1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column" + str(i)]
            listing1.append(column_name)
        listing1.append(item["avg"])
        listing.append(listing1)
    file = csv_name + '.csv'
    headers = columns + ["avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成7.1,已将结果保存至", file)

# 7.2 一个集合字段的求均值,并将结果保存至csv
def query_avg2(columns_avg,column_set,csv_name):
    listing = []
    listing2 = []
    listing3 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_avg])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if i in listing:
                            listing2[listing.index(i)] += value
                            listing3[listing.index(i)] += 1
                        else:
                            listing.append(i)
                            listing2.append(value)
                            listing3.append(1)
            except:
                pass
    listing5 = []
    for j in range(len(listing)):
        listing4 = []
        listing4.append(listing[j])
        listing4.append(listing2[j]/listing3[j])
        listing5.append(listing4)
    file = csv_name + '.csv'
    headers = [column_set] + ["avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing5)
    print("完成7.2,已将结果保存至", file)

# 7.3 一个集合字段和多个普通字段的联合求均值,并将结果保存至csv
def query_avg3(columns_avg,column_set,columns,csv_name):
    listing = []
    listing2 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_avg])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if len(listing) == 0:
                            info1 = []
                            for j in columns:
                                info1.append(item[j])
                            info1.append(i)
                            info1.append(value)
                            info1.append(1)
                            listing.append(info1)
                        else:
                            for k in listing:
                                bools = []
                                for m in range(len(columns)):
                                    if k[m] == item[columns[m]]:
                                        bools.append(True)
                                    else:
                                        bools.append(False)
                                if k[-3] == i:
                                    bools.append(True)
                                else:
                                    bools.append(False)
                                if all(bools):
                                    k[-1] += 1
                                    k[-2] += value
                                    break
                            else:
                                info2 = []
                                for j in columns:
                                    info2.append(item[j])
                                info2.append(i)
                                info2.append(value)
                                info2.append(1)
                                listing.append(info2)
            except:
                pass
    for element in listing:
        denominator = element.pop()
        numerator = element.pop()
        element.append(numerator/denominator)
        listing2.append(element)
    file = csv_name + '.csv'
    headers = columns + [column_set] + ["avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing2)
    print("完成7.3,已将结果保存至", file)

# 7.4 一个集合字段和多个普通字段的联合求均值，并存入MongoDB同目录新collection
def query_avg4(columns_avg,column_set,columns,collection_name):
    collection2 = collect()[collection_name]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                try:
                    value = float(item[columns_avg])
                    for i in item[column_set]:
                        info = {}
                        for j in columns:
                            info[j] = item[j]
                        info[column_set] = i
                        if not collection2.find_one(info):
                            info["sum"] = value
                            info["count"] = 1
                            collection2.insert_one(info)
                        else:
                            for item2 in collection2.find(info):
                                item2["sum"] += value
                                item2["count"] += 1
                                collection2.update_one(info, {"$set": {"sum": item2["sum"],"count":item2["count"]}})
                except:
                    pass
    for item3 in collection2.find():
        mean_value = item3["sum"]/item3["count"]
        collection2.update_one({"_id":item3["_id"]}, {"$set": {"avg": mean_value}})
        collection2.update_one({"_id": item3["_id"]}, {"$unset": {"sum": "","count": ""}})
    print("完成7.4,已将结果保存至MongoDB", collection_name)

# (八)、复合统计
# 8.1 普通字段的联合复合统计(计数，有值数，求和，均值),并将结果保存至csv
def query_complex1(columns_number,columns,csv_name):
    dict = {}
    for i in range(len(columns)):
        header = "column" + str(i)
        value = "$" + columns[i]
        dict[header] = value
    listing = []
    value1 = "$" + columns_number
    for item in collect().aggregate([{"$group": {"_id": dict,"count":{"$sum":1},"sum":{"$sum":value1}, "avg": {"$avg": value1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column" + str(i)]
            listing1.append(column_name)
        listing1.append(item["count"])
        try:
            count_valuable = item["sum"] / item["avg"]
            listing1.append(count_valuable)
        except:
            listing1.append(0)
        listing1.append(item["sum"])
        listing1.append(item["avg"])
        listing.append(listing1)
    file = csv_name + '.csv'
    headers = columns + ["count","count_valuable","sum","avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成8.1,已将结果保存至", file)

# 8.2 一个集合字段的复合统计(有值数，求和，均值),并将结果保存至csv
def query_complex2(columns_number,column_set,csv_name):
    listing = []
    listing2 = []
    listing3 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_number])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if i in listing:
                            listing2[listing.index(i)] += value
                            listing3[listing.index(i)] += 1
                        else:
                            listing.append(i)
                            listing2.append(value)
                            listing3.append(1)
            except:
                pass
    listing5 = []
    for j in range(len(listing)):
        listing4 = []
        listing4.append(listing[j])
        listing4.append(listing3[j])
        listing4.append(listing2[j])
        listing4.append(listing2[j] / listing3[j])
        listing5.append(listing4)
    file = csv_name + '.csv'
    headers = [column_set] + ["count_valuable","sum","avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing5)
    print("完成8.2,已将结果保存至", file)

# 8.3 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值),并将结果保存至csv
def query_complex3(columns_number,column_set,columns,csv_name):
    listing = []
    listing2 = []
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            try:
                value = float(item[columns_number])
                if column_set in item and len(item[column_set]) > 0:
                    for i in item[column_set]:
                        if len(listing) == 0:
                            info1 = []
                            for j in columns:
                                info1.append(item[j])
                            info1.append(i)
                            info1.append(1)
                            info1.append(value)
                            listing.append(info1)
                        else:
                            for k in listing:
                                bools = []
                                for m in range(len(columns)):
                                    if k[m] == item[columns[m]]:
                                        bools.append(True)
                                    else:
                                        bools.append(False)
                                if k[-3] == i:
                                    bools.append(True)
                                else:
                                    bools.append(False)
                                if all(bools):
                                    k[-1] += value
                                    k[-2] += 1
                                    break
                            else:
                                info2 = []
                                for j in columns:
                                    info2.append(item[j])
                                info2.append(i)
                                info2.append(1)
                                info2.append(value)
                                listing.append(info2)
            except:
                pass
    for element in listing:
        denominator = element[-2]
        numerator = element[-1]
        element.append(numerator / denominator)
        listing2.append(element)
    file = csv_name + '.csv'
    headers = columns + [column_set] + ["count_valuable","sum","avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing2)
    print("完成8.3,已将结果保存至", file)

# 8.4 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值)，并存入MongoDB同目录新collection
def query_complex4(columns_number,column_set,columns,collection_name):
    collection2 = collect()[collection_name]
    total = collect().find().count() 
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            if column_set in item and len(item[column_set]) > 0:
                try:
                    value = float(item[columns_number])
                    for i in item[column_set]:
                        info = {}
                        for j in columns:
                            info[j] = item[j]
                        info[column_set] = i
                        if not collection2.find_one(info):
                            info["count"] = 1
                            info["sum"] = value
                            collection2.insert_one(info)
                        else:
                            for item2 in collection2.find(info):
                                item2["count"] += 1
                                item2["sum"] += value
                                collection2.update_one(info, {"$set": {"sum": item2["sum"], "count": item2["count"]}})
                except:
                    pass
    for item3 in collection2.find():
        mean_value = item3["sum"] / item3["count"]
        collection2.update_one({"_id": item3["_id"]}, {"$set": {"avg": mean_value}})
    print("完成8.4,已将结果保存至MongoDB", collection_name)

# (九)、条件复合统计
# 9.1 普通字段的条件联合复合统计(计数，有值数，求和，均值),并将结果保存至csv
def query_complex_if1(columns_if,columns_number,columns,csv_name):
    dict = {}
    for i in range(len(columns)):
        header = "column" + str(i)
        value = "$" + columns[i]
        dict[header] = value
    listing = []
    value1 = "$" + columns_number
    for item in collect().aggregate([{"$match":columns_if},{"$group":{"_id": dict,"count":{"$sum":1},"sum":{"$sum":value1}, "avg": {"$avg": value1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column" + str(i)]
            listing1.append(column_name)
        listing1.append(item["count"])
        try:
            count_valuable = item["sum"] / item["avg"]
            listing1.append(count_valuable)
        except:
            listing1.append(0)
        listing1.append(item["sum"])
        listing1.append(item["avg"])
        listing.append(listing1)
    file = csv_name + '.csv'
    headers = columns + ["count", "count_valuable", "sum", "avg"]
    with open(file, 'w', newline='', encoding='utf-8')as f:  # 有则覆盖，无则新建
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(listing)
    print("完成9.1,已将结果保存至", file)

# 9.2 普通字段的条件联合复合统计(计数，有值数，求和，均值),并存入MongoDB同目录新collection
def query_complex_if2(columns_if,columns_number,columns,collection_name):
    collection2 = collect()[collection_name]
    dict = {}
    for i in range(len(columns)):
        header = "column" + str(i)
        value = "$" + columns[i]
        dict[header] = value
    listing = []
    value1 = "$" + columns_number
    for item in collect().aggregate([{"$match":columns_if},{"$group":{"_id": dict,"count":{"$sum":1},"sum":{"$sum":value1}, "avg": {"$avg": value1}}}]):
        listing1 = []
        for i in range(len(columns)):
            column_name = item["_id"]["column" + str(i)]
            listing1.append(column_name)
        listing1.append(item["count"])
        try:
            count_valuable = item["sum"] / item["avg"]
            listing1.append(count_valuable)
        except:
            listing1.append(0)
        listing1.append(item["sum"])
        listing1.append(item["avg"])
        listing.append(listing1)
    headers = columns + ["count", "count_valuable", "sum", "avg"]
    for a in range(len(listing)):
        dict2 = {}
        for b in range(len(headers)):
            dict2[headers[b]] = listing[a][b]
        collection2.insert_one(dict2)
    print("完成9.2,已将结果保存至MongoDB", collection_name)

# (十)、字段删除
# 字段(含集合字段)删除，用于整理最终结果
def del_field(columns):
    dict = {}
    for i in columns:
        dict[i] = ""
    total = collect().find().count()
    counter = -5000
    frequency = total // 5000 + 1
    for freq in range(frequency):
        counter += 5000
        print("已处理：",counter,"条")
        for item in collect().find().skip(counter).limit(5000):
            collect().update_many({"_id": item["_id"]}, {"$unset": dict})
    print("字段已删除完成")

#==============================以上勿动================================
#==============================以上勿动================================
#==============================以上勿动================================
