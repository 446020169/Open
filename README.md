# <span id="head2"> MongoDB日常数据统计(python_scripts)</span>

### <span id="head3"> 一、前言</span>

#### <span id="head4"> 文件介绍</span>

##### MongoDB_statistics文件夹下有如下4个文件：

|文件|简介|
|:----|:----|
|README.md|脚本函数指南，说明文档，日常参考|
|daily_use.py|日常函数调用，发送指令，日常使用|
|config.ini|基础配置文件，连接桥梁，勿动勿删|
|execute_program.py|脚本函数集合，执行程序，无需修改|

##### 可将 daily_use.py 重命名后多复制几份，分别处理不同的 collection，但务必保证与其他三个文件在同一目录下。

##        

> **注意事项**  
>
> 涉及集合字段的统计中，部分是先对集合进行循环查询，集合字段为空的数据不参与统计。问题函数有：5.2、5.3、5.4、6.2、6.3、6.4、7.2、7.3、7.4、8.2、8.3、8.4;  
> 涉及求和、均值的统计中，部分是先把字段值强制转换为浮点数进行，无法转换或不存在字段值的数据，不参与统计。问题函数有：4.1、4.2、4.8、6.2、6.3、6.4、7.2、7.3、7.4、8.2、8.3、8.4。

##   

### <span id="head5"> 二、函数及参数介绍</span>

#### [函数目录](#head6)

- [(一)、抽取部分数据](#head6)
	- [1.1 取出前N条数据](#head7)
	- [1.2 随机取出N条数据](#head8)
	- [1.3 条件筛选取出部分字段(非集合字段)存至csv](#head9)
	- [1.4 条件筛选取出部分字段(含集合字段)存至collection](#head10)
- [(二)、提取字段值](#head11)
	- [2.1 提取字段的前几位字符](#head12)
	- [2.2 提取满足条件的字段值](#head13)
- [(三)、分析字段值](#head14)
	- [3.1 返回数值字段有值个数、最大值、最小值、均值、中位数](#head15)
- [(四)、打标签](#head16)
	- [4.1 值的双范围标签](#head17)
	- [4.2 值的多范围标签](#head18)
	- [4.3 值的条件标签](#head19)
	- [4.4 全字段搜索是否包含关键词，只要有关键词组中的一个就打上标签](#head20)
	- [4.5 部分字段搜索是否包含关键词，只要有关键词组中的一个就打上标签](#head21)
	- [4.6 全字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签](#head22)
	- [4.7 部分字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签](#head23)
	- [4.8 两个字段值的加减乘除运算](#head24)
- [(五)、计数统计](#head25)
	- [5.1 普通字段的联合计数](#head26)
	- [ 5.2 一个集合字段的计数](#head27)
	- [5.3 一个集合字段和多个普通字段联合计数存至csv](#head28)
	- [5.4 一个集合字段和多个普通字段联合计数存至collection](#head29)
- [(六)、求和统计](#head30)
	- [6.1 普通字段的联合求和](#head31)
	- [6.2 一个集合字段的求和](#head32)
	- [6.3 一个集合字段和多个普通字段的联合求和存至csv](#head33)
	- [6.4 一个集合字段和多个普通字段的联合求和存至collection](#head34)
- [(七)、求平均值](#head35)
	- [7.1 普通字段的联合求均值](#head36)
	- [7.2 一个集合字段的求均值](#head37)
	- [7.3 一个集合字段和多个普通字段的联合求均值存至csv](#head38)
	- [7.4 一个集合字段和多个普通字段的联合求均值collection](#head39)
- [(八)、复合统计](#head40)
	- [8.1 普通字段的联合复合统计(计数，有值数，求和，均值)](#head41)
	- [8.2 一个集合字段的复合统计(有值数，求和，均值)](#head42)
	- [8.3 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值)存至csv](#head43)
	- [8.4 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值)存至collection](#head44)
- [(九)、条件复合统计](#head45)
	- [9.1 普通字段的条件联合复合统计(计数，有值数，求和，均值)存至csv](#head46)
	- [9.2 普通字段的条件联合复合统计(计数，有值数，求和，均值)存至collection](#head47)
- [(十)、字段删除](#head48)
	- [ 10.1 字段删除，用于整理最终结果](#head49)

## 

#### <span id="head6"> (一)、抽取部分数据</span>


##### <span id="head7">1.1 取出前N条数据，并存入MongoDB同目录新collection</span>

    collection_name = "han1" # collection名称
    count = 10 # 提取数据条数
    execute_program.query_data1(collection_name,count)

##### <span id="head8">1.2 随机取出N条数据，并存入MongoDB同目录新collection</span>

    collection_name = "han2" # collection名称
    count = 10 # 提取数据条数
    execute_program.query_data2(collection_name,count)

##### <span id="head9">1.3 条件筛选取出部分字段(非集合字段)，并将结果保存至csv</span>

    dict = {"area":"河南","city":"郑州市"} # 筛选条件
    fields = ["area","city","buyerclass","bidtype","projectcycle"] # 要取出的字段
    csv_name = "test1" # csv的表名
    execute_program.query_data3(dict,fields,csv_name)

##### <span id="head10">1.4 条件筛选取出部分字段(含集合字段)，并存入MongoDB同目录新collection</span>

    dict = {"area":"河南","city":"郑州市"} # 筛选条件
    fields = ["area","city","buyerclass","bidtype","topscopeclass2"] # 要取出的字段
    collection_name = "test2" # collection名称
    execute_program.query_data4(dict,fields,collection_name)

#### <span id="head11"> (二)、提取字段值</span>

##### <span id="head12">2.1 提取字段(含集合字段)的前几位字符(一个汉字、单词、数字、标点算一个字符)存入新字段</span>

    origin_field = "subscopeclass" # 要提取的字段名称
    chars = 4 # 要提取前几位字符
    result_field = "test3" # 要放入的新字段名称
    execute_program.tag_field1(origin_field,chars,result_field)

##### <span id="head13">2.2 提取满足条件的字段值存入新字段</span>

    field_name = "budget" # 要提取的字段
    flag_if  = {"budget":{'$gt':1000,'$lte':2000}} # 提取条件
    flag_field = "test4" # 标签字段名称
    execute_program.tag_field2(field_name,flag_if,flag_field)

#### <span id="head14"> (三)、分析字段值</span>

##### <span id="head15">3.1 返回数值字段(非集合字段)有值个数、最大值、最小值、均值、中位数</span>

    field = "createtime" # 字段名称
    execute_program.value_analysis(field)

#### <span id="head16"> (四)、打标签</span>

##### <span id="head17">4.1 值的双范围标签(非集合字段)，通常用于时间、金额等可以进行比较的字段</span>

    field = "budget" # 要分割的字段
    value = 0 # 分割值,前包后不包
    value_flag_ahead = "小于等于0" # 分割值前面的标记
    value_flag_after = "大于0" # 分割值后面的标记
    flag_field = "test5" # 标签字段名称
    execute_program.tagged1(field,value,value_flag_ahead,value_flag_after,flag_field)

##### <span id="head18">4.2 值的多范围标签(非集合字段,前包后不包)，通常用于时间、金额等可以进行比较的字段</span>

    field = "publishtime" # 要判断的字段名称
    flag_list = [{"1月":[1546272000,1548950400]},{"2月":[1548950400,1551369600]},{"3月":[1551369600,1554048000]},{"4月":[1554048000,1556640000]},{"5月":[1556640000,1559318400]},{"6月":[1559318400,1561910400]}] # 标签，起始值，截止值
    flag_field = "test6" # 要放入的新字段名称
    execute_program.tagged2(field,flag_list,flag_field)

##### <span id="head19">4.3 值的条件标签</span>

    field = "budget" # 要处理的字段
    flag_if  = {"budget":{'$gt':1000,'$lte':2000}} # 打标签的条件
    flag_text = "哈哈哈" # 标签内容
    flag_field = "test7" # 标签字段名称
    execute_program.tagged3(field,flag_if,flag_text,flag_field)

##### <span id="head20">4.4 全字段搜索是否包含关键词，只要有关键词组中的一个就打上标签</span>

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    flag_field = "test8" # 要放入的新字段名称
    execute_program.tagged4(flag_list,flag_field)

##### <span id="head21">4.5 部分字段搜索是否包含关键词，只要有关键词组中的一个就打上标签</span>

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test9" # 要放入的新字段名称
    fields = ["projectname","buyer"] # 要搜索的字段
    execute_program.tagged5(flag_list,field,fields)

##### <span id="head22">4.6 全字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签</span>

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test10" # 要放入的新字段名称
    execute_program.tagged6(flag_list,field)

##### <span id="head23">4.7 部分字段搜索是否包含关键词，满足关键词组中的所有关键词才打上标签</span>

    flag_list = [{"医疗1":["医疗","医生"]},{"教育2":["教育","学校"]},{"政务3":["政务"]},{"交通4":["交通"]},{"安防":["安防"]}]# 标签，值列表
    field = "test11" # 要放入的新字段名称
    fields = ["projectname","buyer"] # 要搜索的字段
    execute_program.tagged7(flag_list,field,fields)

##### <span id="head24">4.8 两个字段(不含集合字段)值的运算(加减乘除)，并将结果存为新字段</span>

    field1 = "jgtime"
    field2 = "zbtime"
    arithmetic = "-" # 仅支持填写"+","-","*","/","//"，例如：（当前含义为：field1-field2=flag_field）
    flag_field = "gap_time"
    execute_program.tagged8(field1,field2,arithmetic,flag_field)

> 注意仅支持field1和field2同时为数值类型的数据处理

#### <span id="head25"> (五)、计数统计</span>

##### <span id="head26">5.1 普通字段的联合计数,并将结果保存至csv</span>

    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test12" # csv的表名
    execute_program.query_count1(fields,csv_name)

##### <span id="head27">5.2 一个集合字段的计数,并将结果保存至csv</span>

    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test13" # csv的表名
    execute_program.query_count2(field_sets,csv_name)

##### <span id="head28">5.3 一个集合字段和多个普通字段联合计数,并将结果保存至csv</span>

    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test14" # csv的表名
    execute_program.query_count3(field_sets,fields,csv_name)

##### <span id="head29">5.4 一个集合字段和多个普通字段的联合计数，并存入MongoDB同目录新collection</span>

    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test15" # collection名称
    execute_program.query_count4(field_sets,fields,collection_name)

#### <span id="head30"> (六)、求和统计</span>

##### <span id="head31">6.1 普通字段的联合求和,并将结果保存至csv</span>

    field_sum = "budget" # 求和字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test16" # csv的表名
    execute_program.query_sum1(field_sum,fields,csv_name)

##### <span id="head32">6.2 一个集合字段的求和,并将结果保存至csv</span>

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test17" # csv的表名
    execute_program.query_sum2(field_sum,field_sets,csv_name)

##### <span id="head33">6.3 一个集合字段和多个普通字段的联合求和,并将结果保存至csv</span>

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test18" # csv的表名
    execute_program.query_sum3(field_sum,field_sets,fields,csv_name)

##### <span id="head34">6.4 一个集合字段和多个普通字段的联合求和,并存入MongoDB同目录新collection</span>

    field_sum = "budget" # 求和字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test19" # collection名称		
    execute_program.query_sum4(field_sum,field_sets,fields,collection_name)

#### <span id="head35"> (七)、求平均值</span>

##### <span id="head36">7.1 普通字段的联合求均值,并将结果保存至csv</span>

    field_avg = "budget" # 求均值字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test20" # csv的表名
    execute_program.query_avg1(field_avg, fields, csv_name)

##### <span id="head37">7.2 一个集合字段的求均值,并将结果保存至csv</span>

    field_avg = "budget" # 求均值字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test21" # csv的表名
    execute_program.query_avg2(field_avg,field_sets,csv_name)

##### <span id="head38">7.3 一个集合字段和多个普通字段的联合求均值,并将结果保存至csv</span>

    field_avg = "budget"  # 求均值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test22"  # csv的表名
    execute_program.query_avg3(field_avg,field_sets,fields,csv_name)

##### <span id="head39">7.4 一个集合字段和多个普通字段的联合求均值，并存入MongoDB同目录新collection</span>

    field_avg = "budget" # 求均值字段
    field_sets = "topscopeclass2" # 集合字段
    fields = ["area","city"] # 列表可含N个普通字段
    collection_name = "test23" # collection名称
    execute_program.query_avg4(field_avg,field_sets,fields,collection_name)

#### <span id="head40"> (八)、复合统计</span>

##### <span id="head41">8.1 普通字段的联合复合统计(计数，有值数，求和，均值),并将结果保存至csv</span>

    field_number = "budget" # 统计值字段
    fields = ["area","city"] # 列表可含N个普通字段
    csv_name = "test24" # csv的表名
    execute_program.query_complex1(field_number,fields,csv_name)

##### <span id="head42">8.2 一个集合字段的复合统计(有值数，求和，均值),并将结果保存至csv</span>

    field_number = "budget" # 统计值字段
    field_sets = "topscopeclass2" # 集合字段
    csv_name = "test25" # csv的表名
    execute_program.query_complex2(field_number,field_sets,csv_name)

##### <span id="head43">8.3 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值),并将结果保存至csv</span>

    field_number = "budget"  # 统计值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test26"  # csv的表名
    execute_program.query_complex3(field_number,field_sets,fields,csv_name)

##### <span id="head44">8.4 一个集合字段和多个普通字段的联合复合统计(有值数，求和，均值)，并存入MongoDB同目录新collection</span>

    field_number = "budget"  # 统计值字段
    field_sets = "topscopeclass2"  # 集合字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    collection_name = "test27" # collection名称
    execute_program.query_complex4(field_number,field_sets,fields,collection_name)

#### <span id="head45"> (九)、条件复合统计</span>

##### <span id="head46">9.1 普通字段的条件联合复合统计(计数，有值数，求和，均值),并将结果保存至csv</span>

    field_if  = {"budget":{'$gt':1000,'$lte':20000}} # 条件
    field_number = "budget"  # 统计值字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    csv_name = "test28" # csv的表名
    execute_program.query_complex_if1(field_if,field_number,fields,csv_name)

##### <span id="head47">9.2 普通字段的条件联合复合统计(计数，有值数，求和，均值),并存入MongoDB同目录新collection</span>

    field_if  = {"budget":{'$gt':1000,'$lte':20000}} # 条件
    field_number = "budget"  # 统计值字段
    fields = ["area", "city"]  # 列表可含N个普通字段
    collection_name = "test29" # collection名称
    execute_program.query_complex_if2(field_if,field_number,fields,collection_name)

#### <span id="head48"> (十)、字段删除</span>

##### <span id="head49"> 字段(含集合字段)删除，用于整理最终结果</span>

    fields =  ["area", "city"]  # 列表可含N个普通字段
    execute_program.del_field(fields)

## <span id="head50"> </span>

***后续迭代优化：*** *1、处理遗留问题；2、把配置文件整合到类中，移至execute_program.py内，在daily_use.py中调用类，修改实例属性；3、将常用的函集合合封装成类。*