[TOC]

# MongoDB日常数据统计(python_scripts)

### 一、前言

#### 文件介绍

##### MongoDB_statistics文件夹下有如下4个文件：

|文件|简介|
|:----|:----|
|README.md|脚本函数指南，说明文档，日常参考|
|daily_use.py|日常函数调用，发送指令，日常使用|
|config.ini|基础配置文件，连接桥梁，勿动勿删|
|execute_program.py|脚本函数集合，执行程序，无需修改|

##### 可将daily_use.py重命名后多复制几份，分别处理不同的collection，但务必保证与其他三个文件在同一目录下。

> ***注意事项***  
>
> 涉及集合字段的统计中，部分是先对集合进行循环查询，集合字段为空的数据不参与统计。问题函数有：5.2、5.3、5.4、6.2、6.3、6.4、7.2、7.3、7.4、8.2、8.3、8.4;  
> 涉及求和、均值的统计中，部分是先把字段值强制转换为浮点数进行，无法转换或不存在字段值的数据，不参与统计。问题函数有：4.1、4.2、4.8、6.2、6.3、6.4、7.2、7.3、7.4、8.2、8.3、8.4。

### 二、函数及参数介绍

#### (一)、抽取部分数据

##### 1.1 取出前N条数据，并存入MongoDB同目录新collection

    collection_name = "han1" # collection名称
    count = 10 # 提取数据条数
    execute_program.query_data1(collection_name,count)

##### 1.2 随机取出N条数据，并存入MongoDB同目录新collection

    collection_name = "han2" # collection名称
    count = 10 # 提取数据条数
    execute_program.query_data2(collection_name,count)

##### 1.3 条件筛选取出部分字段(非集合字段)，并将结果保存至csv

    dict = {"area":"河南","city":"郑州市"} # 筛选条件
    fields = ["area","city","buyerclass","bidtype","projectcycle"] # 要取出的字段
    csv_name = "test1" # csv的表名
    execute_program.query_data3(dict,fields,csv_name)

##### 1.4 条件筛选取出部分字段(含集合字段)，并存入MongoDB同目录新collection

    dict = {"area":"河南","city":"郑州市"} # 筛选条件
    fields = ["area","city","buyerclass","bidtype","topscopeclass2"] # 要取出的字段
    collection_name = "test2" # collection名称
    execute_program.query_data4(dict,fields,collection_name)

#### (二)、提取字段值

##### 2.1 提取字段(含集合字段)的前几位字符(一个汉字、单词、数字、标点算一个字符)存入新字段

    origin_field = "subscopeclass" # 要提取的字段名称
    chars = 4 # 要提取前几位字符
    result_field = "test3" # 要放入的新字段名称
    execute_program.tag_field1(origin_field,chars,result_field)

##### 2.2 提取满足条件的字段值存入新字段

    field_name = "budget" # 要提取的字段
    flag_if  = {"budget":{'$gt':1000,'$lte':2000}} # 提取条件
    flag_field = "test4" # 标签字段名称
    execute_program.tag_field2(field_name,flag_if,flag_field)

#### (三)、分析字段值

##### 3.1 返回数值字段(非集合字段)有值个数、最大值、最小值、均值、中位数

    field = "createtime" # 字段名称
    execute_program.value_analysis(field)

#### (四)、打标签

##### 4.1 值的双范围标签(非集合字段)，通常用于时间、金额等可以进行比较的字段

    field = "budget" # 要分割的字段
    value = 0 # 分割值,前包后不包
    value_flag_ahead = "小于等于0" # 分割值前面的标记
    value_flag_after = "大于0" # 分割值后面的标记
    flag_field = "test5" # 标签字段名称
    execute_program.tagged1(field,value,value_flag_ahead,value_flag_after,flag_field)

##### 4.2 值的多范围标签(非集合字段,前包后不包)，通常用于时间、金额等可以进行比较的字段

    field = "publishtime" # 要判断的字段名称
    flag_list = [{"1月":[1546272000,1548950400]},{"2月":[1548950400,1551369600]},{"3月":[1551369600,1554048000]},{"4月":[1554048000,1556640000]},{"5月":[1556640000,1559318400]},{"6月":[1559318400,1561910400]}] # 标签，起始值，截止值
    flag_field = "test6" # 要放入的新字段名称
    execute_program.tagged2(field,flag_list,flag_field)

##### 4.3 值的条件标签

    field = "budget" # 要处理的字段
    flag_if  = {"budget":{'$gt':1000,'$lte':2000}} # 打标签的条件
    flag_text = "哈哈哈" # 标签内容
    flag_field = "test7" # 标签字段名称
    execute_program.tagged3(field,flag_if,flag_text,flag_field)

##### 4.4 全字段搜索是否包含关键词，只要有关键词组中的一个就打上标签

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    flag_field = "test8" # 要放入的新字段名称
    execute_program.tagged4(flag_list,flag_field)

##### 4.5 部分字段搜索是否包含关键词，只要有关键词组中的一个就打上标签

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test9" # 要放入的新字段名称
    fields = ["projectname","buyer"] # 要搜索的字段
    execute_program.tagged5(flag_list,field,fields)

##### 4.6 全字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test10" # 要放入的新字段名称
    execute_program.tagged6(flag_list,field)

##### 4.7 部分字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test11" # 要放入的新字段名称
    fields = ["projectname","buyer"] # 要搜索的字段
    execute_program.tagged7(flag_list,field,fields)

##### 4.8 两个字段(不含集合字段)值的运算(加减乘除)，并将结果存为新字段

    field1 = "jgtime"
    field2 = "zbtime"
    arithmetic = "-" # 仅支持填写"+","-","*","/","//"，例如：（当前含义为：field1-field2=flag_field）
    flag_field = "gap_time"
    execute_program.tagged8(field1,field2,arithmetic,flag_field)
> 注意仅支持field1和field2同时为数值类型的数据处理

#### (五)、计数统计

##### 5.1 普通字段的联合计数,并将结果保存至csv

    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test12" # csv的表名
    execute_program.query_count1(fields,csv_name)

##### 5.2 一个集合字段的计数,并将结果保存至csv

    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test13" # csv的表名
    execute_program.query_count2(field_sets,csv_name)

##### 5.3 一个集合字段和多个普通字段联合计数,并将结果保存至csv

    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test14" # csv的表名
    execute_program.query_count3(field_sets,fields,csv_name)

##### 5.4 一个集合字段和多个普通字段的联合计数，并存入MongoDB同目录新collection

    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test15" # collection名称
    execute_program.query_count4(field_sets,fields,collection_name)

#### (六)、求和统计

##### 6.1 普通字段的联合求和,并将结果保存至csv

    field_sum = "budget" # 求和字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test16" # csv的表名
    execute_program.query_sum1(field_sum,fields,csv_name)

##### 6.2 一个集合字段的求和,并将结果保存至csv

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test17" # csv的表名
    execute_program.query_sum2(field_sum,field_sets,csv_name)

##### 6.3 一个集合字段和多个普通字段的联合求和,并将结果保存至csv

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test18" # csv的表名
    execute_program.query_sum3(field_sum,field_sets,fields,csv_name)

##### 6.4 一个集合字段和多个普通字段的联合求和,并存入MongoDB同目录新collection

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test19" # collection名称		
    execute_program.query_sum4(field_sum,field_sets,fields,collection_name)

#### (七)、求平均值

##### 7.1 普通字段的联合求均值,并将结果保存至csv

    field_avg = "budget" # 求均值字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test20" # csv的表名
    execute_program.query_avg1(field_avg, fields, csv_name)

##### 7.2 一个集合字段的求均值,并将结果保存至csv

    field_avg = "budget" # 求均值字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test21" # csv的表名
    execute_program.query_avg2(field_avg,field_sets,csv_name)

##### 7.3 一个集合字段和多个普通字段的联合求均值,并将结果保存至csv

    field_avg = "budget"  # 求均值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test22"  # csv的表名
    execute_program.query_avg3(field_avg,field_sets,fields,csv_name)

##### 7.4 一个集合字段和多个普通字段的联合求均值，并存入MongoDB同目录新collection

    field_avg = "budget" # 求均值字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test23" # collection名称
    execute_program.query_avg4(field_avg,field_sets,fields,collection_name)

#### (八)、复合统计

##### 8.1 普通字段的联合复合统计(计数，有值数，求和，均值),并将结果保存至csv

    field_number = "budget" # 统计值字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test24" # csv的表名
    execute_program.query_complex1(field_number,fields,csv_name)

##### 8.2 一个集合字段的复合统计(有值数，求和，均值),并将结果保存至csv

    field_number = "budget" # 统计值字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test25" # csv的表名
    execute_program.query_complex2(field_number,field_sets,csv_name)

##### 8.3 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值),并将结果保存至csv

    field_number = "budget"  # 统计值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test26"  # csv的表名
    execute_program.query_complex3(field_number,field_sets,fields,csv_name)

##### 8.4 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值)，并存入MongoDB同目录新collection

    field_number = "budget"  # 统计值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    collection_name = "test27" # collection名称
    execute_program.query_complex4(field_number,field_sets,fields,collection_name)

#### (九)、条件复合统计

##### 9.1 普通字段的条件联合复合统计(计数，有值数，求和，均值),并将结果保存至csv

    field_if  = {"budget":{'$gt':1000,'$lte':20000}} # 条件
    field_number = "budget"  # 统计值字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test28" # csv的表名
    execute_program.query_complex_if1(field_if,field_number,fields,csv_name)

##### 9.2 普通字段的条件联合复合统计(计数，有值数，求和，均值),并存入MongoDB同目录新collection

    field_if  = {"budget":{'$gt':1000,'$lte':20000}} # 条件
    field_number = "budget"  # 统计值字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    collection_name = "test29" # collection名称
    execute_program.query_complex_if2(field_if,field_number,fields,collection_name)

#### (十)、字段删除

##### 字段(含集合字段)删除，用于整理最终结果

    fields =  ["area", "city"]  # 列表可含N个普通字段
    execute_program.del_field(fields)

## 

***后续迭代优化：*** *1、处理遗留问题；2、把配置文件整合到类中，移至execute_program.py内，在daily_use.py中调用类，修改实例属性；3、将常用的函集合合封装成类。*
