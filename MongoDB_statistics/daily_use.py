# -*- coding: utf-8 -*-                                                       #|
import configparser,execute_program                                           #|
# 修改至配置文件                                                               #|
def write_config(db_host,db_name,db_collection):                              #|
    config = configparser.ConfigParser()                                      #|
    config.read("config.ini")                                                 #|
    config.set('mongo', 'host', db_host)                                      #|
    config.set('mongo', 'dbname', db_name)                                    #|
    config.set('mongo', 'collection', db_collection)                          #|
    with open("config.ini","w") as f:                                         #|
        config.write(f)                                                       #|
        print("配置信息已更新")                                                #|
#==============================上面勿动=======================================#|

#=====请在这里修改需要操作的MongoDB服务器|数据库|表======
db_host = "192.168.3.207:27082"
db_name = "hanhongfei"
db_collection = "project_1009_limit1000"
write_config(db_host,db_name,db_collection)

#===========请在下面写出需要调用的函数及其参数============

# 6.3 一个集合字段和多个普通字段的联合求和,并将结果保存至csv
field_sum = "budget" # 求和字段
field_sets = "topscopeclass2" # 集合字段
fields = ["area","city"] # 列表可含N个普通字段
csv_name = "test18" # csv的表名
execute_program.query_sum3(field_sum,field_sets,fields,csv_name)
