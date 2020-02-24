<p align = "right"> :man_student: :handshake: :man_student:  &emsp; :pray: &emsp; :point_up_2: :heavy_plus_sign: :star: </p>  
 
# <span id="head1"> MongoDB常用语句汇总</span>

- [ MongoDB常用语句汇总](#head1)
	- [ 一、登陆、显示、操作](#head2)
	- [ 二、插入、删除、更新](#head3)
		- [ （一）插入](#head4)
		- [ （二）删除](#head5)
		- [ （三）更新](#head6)
	- [ 三、$操作符](#head7)
		- [ （一）查询操作符](#head8)
			- [ 1、数值比较符](#head9)
			- [ 2、and、or逻辑符](#head10)
			- [ 3、$in、$nin、$not](#head11)
			- [ 4、$exists存在操作符](#head12)
			- [ 5、$mod取模运算符](#head13)
			- [ 6、$all、$size数组操作符](#head14)
			- [ 7、$type操作符](#head15)
			- [ 8、正则条件](#head16)
			- [ 9、$偏移操作符  ](#head17)
			- [ 10、$where条件操作符](#head18)
			- [ 11、内嵌文档操作符](#head19)
			- [ 12、$text操作符](#head20)
			- [ 13、$expr操作符](#head21)
		- [ （二）更新操作符](#head22)
			- [1、$set  ](#head23)
			- [2、$unset  ](#head24)
			- [3、$inc  ](#head25)
			- [4、$rename  ](#head26)
			- [5、$push  ](#head27)
			- [6、$pushAll  ](#head28)
			- [7、$addToSet  ](#head29)
			- [8、$each  ](#head30)
			- [9、$pull  ](#head31)
			- [10、$pullAll](#head32)
			- [11、$pop  ](#head33)
			- [12、$bit  ](#head34)
			- [13、$slice  ](#head35)
			- [14、$mul  ](#head36)
			- [15、$position  ](#head37)
			- [16、$setOnInsert  ](#head38)
			- [17、$currentDate  ](#head39)
	- [ 四、查询](#head40)
		- [ （一）基本查询](#head41)
		- [ （二）distinct去重查询](#head42)
		- [ （三）count计数查询](#head43)
		- [ （四）Limit、Skip、sort限制查询](#head44)
	- [ 五、聚合](#head45)
		- [ （一）aggergate()简介](#head46)
		- [ （二）聚合$group表达式运算符](#head47)
		- [ （三）其他聚合运算符](#head48)
		- [ （四）聚合例子](#head49)
			- [ 1、$project实例](#head50)
			- [ 2、$match实例](#head51)
			- [ 3、$skip实例](#head52)
			- [ 4、$group实例](#head53)
			- [ 5、$concat实例](#head54)
			- [ 6、$add、$subtract、$multiply、$divide](#head55)
			- [ 7、$cond条件及其if-else使用](#head56)
			- [ 8、$redact操作符的使用](#head57)
			- [ 9、字段比较](#head58)
			- [ 10、时间聚合统计](#head59)
			- [ 11、$substr截取字符串](#head60)
			- [ 12、$lookup实例](#head61)
	- [ 六、索引](#head62)
		- [ （一）常规索引语法](#head63)
		- [ （二）其他索引语法](#head64)
		- [ （三）高级索引](#head65)
		- [ （四）索引限制](#head66)
	- [ 七、高级教程与操作](#head67)
		- [ （一）MongoDB关系](#head68)
		- [ （二）数据库引用](#head71)
		- [ （三）覆盖索引查询](#head72)
		- [ （四）查询分析](#head73)
		- [ （五）原子操作](#head74)
		- [ （六）ObjectId](#head75)
		- [ （七）Map Reduce](#head76)
		- [ （八）固定集合](#head77)
		- [ （九）自定义函数](#head78)
	- [ 八、集合方法大全](#head79)
	- [ 九、数据库方法大全](#head80)
	- [ 十、Studio3T小技巧](#head81)
	- [ 十一、忠告](#head82)

## <span id="head2"> 一、登陆、显示、操作</span>

假设在本机上有一个端口为27082的MongoDB服务，假设已经把mongo bin文件加入到系统PATH下。  
>登陆：mongo --port 27082  
>显示DB：show dbs/show databases  
>进入某DB：use test_cswuyg（有则进入，无则新建）  
>显示集合：show collections/show tables  
>显示当前DB：db  

进入某DB后，就可以直接使用查询、统计语句了，例如：  
>db.project_2018_2019.find({}).count()  
>db.getCollection("project_2018_2019").find({}).count()  

其他库表语句：  
>删除DB：db.dropDatabase()  
>删除集合：db.collection.drop()  
>新建集合（名字为runoob）：db.createCollection("runoob")  

## <span id="head3"> 二、插入、删除、更新</span>

### <span id="head4"> （一）插入</span>

插入文档：db.mycol2.insert({"name" : "菜鸟教程"})（有则插入，无则新建），3.2版本之后，常用以下方法：  

插入一条数据：
>db.collection.insertOne({"a": 3})  

插入多条数据：
>db.collection.insertMany([{"b": 3}, {'c': 4}])（通常先创建数据，将数据放入数组中，一次insert到集合中）  

### <span id="head5"> （二）删除</span>

删除文档：db.col.remove({'title':'MongoDB 教程'})  
>删除条件下所有文档，常用一下方式：  
>db.col.find() #先查询确认一下要删的数据  
>db.col.remove({}) #执行删除，无条件则删除所有  
>db.col.find() #再查询确认删除完成  

remove()方法并不会真正释放空间，需要继续执行db.repairDatabase()来回收磁盘空间。remove()方法已经过时了，现在官方推荐使用 deleteOne() 和 deleteMany()方法。  
>删除status等于D的一个文档：db.inventory.deleteOne({status:"D"})  
>删除status等于A的全部文档：db.inventory.deleteMany({status:"A"})  

### <span id="head6"> （三）更新</span>

update() 方法用于更新已存在的文档。语法格式如下：

db.collection.update(query,update,{upsert: boolean,multi: boolean,writeConcern: document})

query : update的查询条件，类似sql update查询内where后面的。  
update : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的。  
upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。  
multi : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。  
writeConcern :可选，抛出异常的级别。  

例如：
>db.col.update({'title':'MongoDB教程'},{$set:{'title':'MongoDB'}})  

**update()也已过时，推荐使用 updateOne() 和 updateMany()方法。**  

save()方法有更新和插入两种功能，已存在则更新，不存在则插入。  
>db.collection.save({"_id" : 100,"name" : "菜鸟教程"})  

**save()也已过时，推荐使用 saveOne() 和 saveMany()方法。**  

## <span id="head7"> 三、$操作符</span>

### <span id="head8"> （一）查询操作符</span>

#### <span id="head9"> 1、数值比较符</span>

操作|格式|范例|RDBMS中的类似语句
:---|:------------ |:--|:------------
等于|{key:value}|db.col.find({"by":"菜鸟教程"}).pretty()|where by = '菜鸟教程'
小于|{key:{$lt:value}}|db.col.find({"likes":{$lt:50}}).pretty()|where likes  50
小于或等于|{key:{$lte:value}}|db.col.find({"likes":{$lte:50}}).pretty()|where likes = 50
大于|{key:{$gt:value}}|db.col.find({"likes":{$gt:50}}).pretty()|where likes  50
大于或等于|{key:{$gte:value}}|db.col.find({"likes":{$gte:50}}).pretty()|where likes = 50
不等于|{key:{$ne:value}}|db.col.find({"likes":{$ne:50}}).pretty()|where likes != 50

组合使用，获取"col"集合中 "likes" 大于等于100，小于 200 的数据，你可以使用以下命令：  
>db.col.find({likes : {$gte:100,$lt:200}})

#### <span id="head10"> 2、and、or逻辑符</span>

演示and和or联合使用，类似常规SQL语句为：'where likes>50 AND (by = '菜鸟教程' OR title = 'MongoDB 教程')'
>db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()

and在这里体现为逗号，当然也可以这样用：{$and:[{key:value},{key:value}]}。

#### <span id="head11"> 3、$in、$nin、$not</span>

$in  
在范围内  
查询年龄为18,28  
>db.test.find({age:{$in:[18, 28]}})

$nin  
不在范围内  
查询年龄不为18,28  
>db.test.find({age:{$nin:[18, 28]}})

$not $in  
不在范围内  
查询年龄不为18,28  
>db.test.find({age: {$not: {$in:[18,28]}}})

$not  
不等于  
查询名字不以T开头的  
>db.test.find({name: {$not: /^T.*/}})

#### <span id="head12"> 4、$exists存在操作符</span>

$exists，查询包含age字段的数据  
>db.test.find({age: {$exists: true}})

true存在，false不存在  

null，查询age字段不存在或者值为null的数据  
>db.test.find({age:null})

#### <span id="head13"> 5、$mod取模运算符</span>

查询age取模10等于1的数据。  
>db.student.find({age:{$mod:[10,1]}})
结果显示年龄为1、11、21……  

#### <span id="head14"> 6、$all、$size数组操作符</span>

数组中所有包含banana  
>db.test.find({"fruit":"banana"})

同时包含bananat和apple(顺序无关紧要)  
>db.test.find({"fruit": {"$all": ["banana","apple"]}})

精确匹配(数据必须和查询条件完全匹配，顺序也必须保持一致)  
>db.test.find({"fruit":["apple","banana","peach"]})

下标(数组的起始下标是0)  
>db.test.find({"fruit.2":"peach"})

$size，数组长度，查询fruit长度为3.  
>db.test.find({"fruit": {$size : 3}})

#### <span id="head15"> 7、$type操作符</span>

$type操作符是基于BSON类型来检索集合中匹配的数据类型，并返回结果。  
MongoDB 中可以使用的类型如下表所示：  

类型|数字|备注
:---|:----:|:---
Double|1|  
String|2|  
Object|3|  
Array|4|  
Binary data|5|  
Undefined|6|已废弃。  
Object id|7|  
Boolean|8|  
Date|9|  
Null|10|  
Regular Expression|11|  
JavaScript|13|  
Symbol|14|  
JavaScript (with scope)|15|  
32-bit integer|16|  
Timestamp|17|  
64-bit integer|18|  
Min key|255|Query with -1.  
Max key|127|  

如果想获取 "col" 集合中 title 为 String 的数据，可以使用以下命令：  
>db.col.find({"title" : {$type : 2}})  
>或  
>db.col.find({"title" : {$type : 'string'}})  

#### <span id="head16"> 8、正则条件</span>

查询title包含"教"字的文档：  
>db.col.find({title:/教/})

查询title字段以"教"字开头的文档：  
>db.col.find({title:/^教/})

查询title字段以"教"字结尾的文档：  
>db.col.find({title:/教$/})

忽略大小写  
>db.test.find({name:/stephen?/i})

$regex方法  
>db.collection.find( { sku: /adC/i } );等效于下面这种写法
>db.collection.find( { sku: { $regex: 'abC', $options: 'i' } } );

参数介绍：  
参数 i : 忽略大小写，{field:{$regex/pattern/i}}，设置i选项后，模式中的字母会进行大小写不敏感匹配。  
参数 m : 多行匹配模式，{field:{$regex/pattern/,$options:'m'}，m选项会更改^和$元字符的默认行为，分别使用与行的开头和结尾匹配，而不是与输入字符串的开头和结尾匹配。  
参数 s : 单行匹配模式{field:{$regex:/pattern/,$options:'s'}，设置s选项后，会改变模式中的点号(.)元字符的默认行为，它会匹配所有字符，包括换行符(\n)，只能显式位于option选项中。  
参数 x : 忽略非转义的空白字符，{field:{$regex:/pattern/,$options:'m'}，设置x选项后，正则表达式中的非转义的空白字符将被忽略，同时井号(#)被解释为注释的开头注，只能显式位于option选项中。  

i，m，x，s可以组合使用，例如:{name:{$regex:/j*k/,$options:"si"}}  
在设置索引的字段上进行正则匹配可以提高查询速度，而且当正则表达式使用的是前缀表达式时，查询速度会进一步提高，例如:{name:{$regex: /^joe/}  

还有一个情形是：匹配规则中使用了锚,所谓的锚就是 **^开头, $结束** ，例如：
>db.products.find( { description: { $regex: /^S/, $options: 'm' } } )

意思就是匹配description字段的value值中，以大写S开头的value值。匹配后结果是：  
{ "_id" : 100, "sku" : "abc123", "description" : "Single line description." }  
{ "_id" : 101, "sku" : "abc789", "description" : "First line\nSecond line" }  
可以看出，第二条记录中descriptio的值包含\n换行字符，而他之所以能匹配出来就是因为添加了m 参数。  

此时可以分析出m参数的使用场景：  
应该是为了匹配字段value值中以某个字符开头(^)，或者是某个字符结束($).即便value中包含换行符(\n)也能匹配到。  
从上例最后例子看出，m参数应该是和锚同时使用才有意思，否则直接去匹配也能匹配出来。说明m是在特殊需求下才使用的！  

>db.products.find( { description: { $regex: /m.*line/, $options: 'si' } } )

匹配value中包含m且之后为任意字符包括换行符并且还包含line字符的字符串，不区分大小写。  
结果为：  
{ "_id" : 102, "sku" : "xyz456", "description" : "Many spaces before line" }  
{ "_id" : 103, "sku" : "xyz789", "description" :"Multiple\nline description" }  

如果不加s参数时，语句为：  
db.products.find( { description: { $regex: /m.*line/, $options: 'i' } } )  
结果为：  
{ "_id" : 102, "sku" : "xyz456", "description" : "Many spaces before line" }  

#### <span id="head17">9、$偏移操作符  </span>

在需要对数组中的值进行操作的时候，可通过位置或者定位操作符（"$"）,数组是0开始的，可以直接将下标作为键来选择元素。  
示例如下：  
{ "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC", "comments" : [ { "by" : "joe", "votes" : 3 }, { "by" : "jane", "votes" : 7 } ] }  
> t.update( {'comments.by':'joe'}, {$inc:{'comments.$.votes':1}}, false, true )  
> t.find()  

{ "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC", "comments" : [ { "by" : "joe", "votes" : 4 }, { "by" : "jane", "votes" : 7 } ] }  

update后面第一个参数false意为没找到符合条件的数据不新插入；  
update后面第二个参数true意为按条件查出来所有记录全部更新；  
上面这种方式能更新数组中所满足条件的值。  
下面这种方式只能更新满足条件的第一个值：  
> t.update( {'comments.by':'joe'}, {$inc:{'comments.$.votes':1}})  

这里的 $ 也可以用值来代替，例如：0、1、2、3……。  
> t.update( {'comments.by':'joe'}, {$inc:{'comments.0.votes':1}})  

#### <span id="head18"> 10、$where条件操作符</span>

条件操作符，aggregate中不支持$where。  
$where 用它可以执行任意JavaScript作为查询的一部分，这就使得查询能做（几乎）任何事情，最典型的就是比较两个文档的键的值是否相等，一定要避免使用where。因为它在速度上要比常规查询慢很多，只有走投无路才考虑，将常规查询作为前置过滤，与where组合使用可以不牺牲性能，如果可能的话，用索引根据非where子句进行过滤，where只用于对结果进行调优。  

判断两个字段相等  
>db.xxx.find({"$where":"this.filed1 == this.filed2 ", xxx:"xxx",xxx:"xxx" })

>db.test.find({ "$where": "this.fields1 == this.fields2" }).limit(10);

判断两个字段不相等  
>db.xxx.find({"$where":"this.filed1 != this.filed2 ", xxx:"xxx",xxx:"xxx" })

#### <span id="head19"> 11、内嵌文档操作符</span>

$elemMatch它会限定条件进行分组，仅当需要对一个内嵌文档的多个键操作时才会用到，并且只返回内嵌文档中符合条件的第一条数据。  
使用方法演示：  
>db.test.insert({"id":1, "members":[{"name":"BuleRiver1", "age":27, "gender":"M"}, {"name":"BuleRiver2", "age":23, "gender":"F"}, {"name":"BuleRiver3", "age":21, "gender":"M"}]});

(1) 使用db.test.find({"members":{"name":"BuleRiver1"}});  
查询的结果是空集。  
(2) 使用db.test.find({"members":{"name":"BuleRiver1", "age":27, "gender":"M"}});  
可以得到结果，只有完全匹配一个的时候才能获取到结果。  
(3) 使用db.test.find({"members":{"age":27, "name":"BuleRiver1", "gender":"M"}});  
得到的结果是空集，把键值进行颠倒，也无法得到结果。  
(4) 使用db.test.find({"members.name":"BuleRiver1"});  
可以查询出结果的。  
(5) 使用db.test.find({"members.name":"BuleRiver1", "members.age":27});  
也可以查询出结果。  
(6) 使用db.test.find({"members.name":"BuleRiver1", "members.age":23});  
也可以查询出结果。  
不过我们应该注意到：BuleRiver1是数组中第一个元素的键值，而23是数组中第二个元素的键值，这样也可以查询出结果。  

对于我们的一些应用来说，以上结果显然不是我们想要的结果。所以我们应该使用$elemMatch操作符:  
(1) $elemMatch+同一个元素中的键值组合  
>db.test.find({"members":{"$elemMatch":{"name":"BuleRiver1", "age":27}}});

可以查询出结果；  
(2)$elemMatch+不同元素的键值组合  
>db.test.find({"members":{"$elemMatch":{"name":"BuleRiver1", "age":23}}});

查询不出结果。  
因此，(1)展示的嵌套查询正是我们想要的查询方式。  

#### <span id="head20"> 12、$text操作符</span>

全文检索对每一个词建立一个索引，指明该词在文章中出现的次数和位置，当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户的检索方式。这个过程类似于通过字典中的检索字表查字的过程。  
目前支持15种语言的全文索引：danish、dutch、english、finnish、french、german、hungarian、italian、norwegian、portuguese、romanian、russian、spanish、swedish、turkish。Mongodb 3.2之后的企业版中才开始加入了对中文的支持。  

创建全文索引  
{"post_text": "enjoy the mongodb articles on Runoob",  
"tags": [  
"mongodb",  
"runoob"]}  

建立全文索引，这样我们可以搜索文章内的内容：  
>db.posts.createIndex({post_text:"text"})  

使用全文索引  
使用全文索引可以提高搜索效率。  
>db.posts.find({$text:{$search:"runoob"}})  

{ "_id" : ObjectId("53493d14d852429c10000002"),  
"post_text" : "enjoy the mongodb articles on Runoob",  
"tags" : [ "mongodb", "runoob" ]}  

删除全文索引  
删除已存在的全文索引，可以使用 find 命令查找索引名：  
>db.posts.getIndexes()  

通过以上命令获取索引名，本例的索引名为post_text_text，执行以下命令来删除索引：  
>db.posts.dropIndex("post_text_text")  

#### <span id="head21"> 13、$expr操作符</span>

使用$expr运算符联合多个运算，选出budget值大于spent值的数据  
例子：
{ "_id" : 1, "category" : "food", "budget": 400, "spent": 450 }
{ "_id" : 2, "category" : "drinks", "budget": 100, "spent": 150 }
{ "_id" : 3, "category" : "clothes", "budget": 100, "spent": 50 }
{ "_id" : 4, "category" : "misc", "budget": 500, "spent": 300 }
{ "_id" : 5, "category" : "travel", "budget": 200, "spent": 650 }

>db.monthlyBudget.find( { $expr: { $gt: [ "$spent" , "$budget" ] } } )

结果如下：
{ "_id" : 1, "category" : "food", "budget" : 400, "spent" : 450 }
{ "_id" : 2, "category" : "drinks", "budget" : 100, "spent" : 150 }
{ "_id" : 5, "category" : "travel", "budget" : 200, "spent" : 650 }

### <span id="head22"> （二）更新操作符</span>

#### <span id="head23">1、$set  </span>

用来指定一个键并更新键值，若键不存在并创建。  
>{ $set : { field : value } }

#### <span id="head24">2、$unset  </span>

用来删除一个键。
>{ $unset : { field : 1} }

#### <span id="head25">3、$inc  </span>

可以对文档的某个值为数字型（只能为满足要求的数字）的键进行增减的操作。  
>{ $inc : { field : value } }

#### <span id="head26">4、$rename  </span>

修改字段名称  
{$rename:{old_field_name:new_field_name}}  
要将name字段改名为"alias"，如下面的代码所示：  
{"_id":ObjectId("4fe686288414d282f712fae8"),"name":[],"userid":3}  
>db.t3.update({"userid":3},{$rename:{"name":"alias"}})  
>db.t3.find()

{"_id":ObjectId("4fe686288414d282f712fae8"),"alias":[],"userid":3}

#### <span id="head27">5、$push  </span>

把value追加到field里面去，field一定要是数组类型才行，如果field不存在，会新增一个数组类型加进去。  
>{ $push : { field : value } }

#### <span id="head28">6、$pushAll  </span>

同$push，只是一次可以追加多个值到一个数组字段内。  
>{ $pushAll : { field : value_array } }

#### <span id="head29">7、$addToSet  </span>

增加一个值到数组内，而且只有当这个值不在数组内才增加。  
>{ $addToSet : { field : value } }

#### <span id="head30">8、$each  </span>

$each修饰符允许$addToSet操作符添加多个元素到数组字段中，$addToset和它组合起来可以添加多个不同的值,而用ne和push组合就不能实现.  
{ _id: 1, letters: ["a", "b"] }  

db.test.update(
{ _id: 1 },
{ $addToSet: {letters: [ "c", "d" ] } })

{ _id: 1, letters: [ "a", "b", [ "c", "d" ] ] }  
如果想将数组中的每个元素分开添加到letters字段中，可以使用$each修饰符。  
{ _id: 2, item: "cable", tags: [ "electronics", "supplies" ] }  

db.inventory.update(
{ _id: 2 },
{ $addToSet: { tags: { $each: [ "camera", "electronics", "accessories" ] } } })

上面的操作只会将"camera"和"accessories"元素添加到tags数组字段中，由于"electronics"元素已经存在于数组中了。  
{_id: 2,item: "cable",tags: [ "electronics", "supplies", "camera", "accessories" ]}  

#### <span id="head31">9、$pull  </span>

从数组field内删除一个等于value值。  
>{ $pull : { field : _value } }

#### <span id="head32"> 10、$pullAll</span>

同$pull，只是一次可以从数组field内删除多个等于value值。  
>{ $pullAll : { field : value_array}}

#### <span id="head33">11、$pop  </span>

删除数组的第一个或最后一个元素
>{ $pop : { field : 1 } }

#### <span id="head34">12、$bit  </span>

位操作，integer类型 **暂时不会用**
>{$bit : { field : {and : 5}}}
>{$bit: {fields: {and|or|xor: int}}}

#### <span id="head35">13、$slice  </span>

返回数组的一个子集合,它也可以返回指定地方的指定条数，如果数组长度不够则返回指定地方之后的所有数据。另外，除非特别声明，否则使用slice时将返回文档中的所有键，这与其他的不太一样。  
$slice在$push中是为了限制数组的总长度，-1说明数组长度为1，-5说明数组长度为5，数组为0说明数组是空。  
假设原先address数组中有3个元素：  
{"_id":1,"name":"bill","address":[{"street":"Xingzhuang5","num":2},{"street":"Xuhui6"},{"street":"Xingzhuang6","num":2}]}  
>db.ArrayTest.updateOne({ "name" : "bill"},{$push: {"address": {$each: [{"street" : "Xuhui7"},{ "street" : "Xingzhuang7", "num" : 2}], $slice: -3}}})

运行结果，我们分析一下应该是总长度为3，由于要新增2个元素，所以最前面的两个元素会被删除，在Xingzhuang6后面会再增加2个新元素:  
{"_id":1,"name":"bill","address":[{"street":"Xingzhuang6","num":2},{"street":"Xuhui7"},{"street":"Xingzhuang7","num":2}]}  

#### <span id="head36">14、$mul  </span>

$mul操作符用一个数字乘以一个操作符，指定一个$mul操作符，使用一下原型：  
{ $mul: { field: number } }  
如果指定的字段在文档中不存在，$mul操作符创建字段并且设置值为0作为乘数；  

例1：  
乘以一个字段的值：考虑如下的products集合文档：  
{ _id: 1, item: "ABC", price: 10.99 }  
>db.products.update({_id:1},{ $mul: { price: 1.25 } })  

操作的结果是：  
{ _id: 1, item: "ABC", price: 13.7375 }  

例2：  
$mul操作符应用到一个不存在的字段上：考虑如下的products集合文档：  
{ _id: 2,  item: "Unknown" }  
>db.products.update({ _id: 2 },{ $mul: { price: NumberLong(100) } })  

执行的结果是：  
{ "_id" : 2, "item" : "Unknown", "price" : NumberLong(0) }  

例3：  
乘以混合数据类型：考虑如下的products集合文档：  
{ _id: 3,  item: "XYZ", price: NumberLong(10) }  
>db.products.update({ _id: 3 },{ $mul: { price: NumberInt(5) } })  

得到的结果是：  
{ "_id" : 3, "item" : "XYZ", "price" : NumberLong(50) }  

#### <span id="head37">15、$position  </span>

$position修饰符指定使用$push操作符插入数组中的数据元素的位置，并且必须和$each一起使用；使用位置修饰符的格式如下：  
{$push: {field: {$each: [ value1, value2, ... ],$position: num}}}  
如果num是负数或者0插入的数据就放到数组的开始位置，如果num大于或者等于数组的长度则不对数组做任何修改直接放入到数组的最后位置。  

例1：  
将元素插入到数组开始的位置：  
{ "_id" : 1, "scores" : [ 100 ] }  
以下操作会将元素放到数组的开始位置：  
>db.students.update({ _id: 1 },{$push: {scores: {$each: [ 50, 60, 70 ],$position: 0}}})  

操作的结果是：  
{ "_id" : 1, "scores" : [  50,  60,  70,  100 ] }  

例2：  
将元素插入到数组的中间位置：  
{ "_id" : 1, "scores" : [  50,  60,  70,  100 ] }  
以下操作会更新scores字段并将20、30元素放入索引为2的位置  
>db.students.update({_id:1},{$push: {scores: {$each: [ 20, 30 ],$position: 2}}})

操作结果是：
{ "_id" : 1, "scores" : [  50,  60,  20,  30,  70,  100 ] }

#### <span id="head38">16、$setOnInsert  </span>

如果update的更新参数upsert:true，也就是如果要更新的文档不存在的话会插入一条新的记录，$setOnInsert操作符会将指定的值赋值给指定的字段，如果要更新的文档存在那么$setOnInsert操作符不做任何处理；  
你可以指定upsert参数在db.collection.update()和db.collection.findAndModify()方法中；  
db.collection.update(query,{ $setOnInsert: { field1: value1, ... } },{ upsert: true })  

例子：  

db.products.update({ _id: 1 },{
$set: { item: "apple" },
$setOnInsert: { defaultQty: 100 }},
{upsert: true})

如果指定的集合文档不存在将会创建一个_id为1，其它的值为$set操作符和$setOnInsert操作符指定的字段和值；  
新的集合文档是：  
{ "_id" : 1, "item" : "apple", "defaultQty" : 100 }  
如果是用 db.collection.update()和upsert:true能够查找到指定的集合文档，Mongodb将会更新$set操作符指定的值，忽略掉$setOnInsert指定的值；  

#### <span id="head39">17、$currentDate  </span>

$currentDate设置字段的值为当前时间，值为Date类型或者Timestamp时间戳类型，默认是Date类型。  
$currentDate操作符的使用格式是：  
{ $currentDate: { field1: typeSpecification1, ... } }  
typeSpecification字段可以是一个boolean true类型设置当前字段是日期Date类型，或者一个文档{ $type: "timestamp" }或者{ $type: "date" }根据指定的类型设置日期，该操作是只支持小写的timestamp和小写的date。  
$currentDate操作符是只用在更新操作上，不可以用在insert操作，更新日期类型的字段时建议使用$currentDate操作符，因为它是直接取的数据库服务端的时间，而使用new Date()设置日期取的是当前服务器上的时间，容易造成误差。  

例子：  
{ _id: 1, status: "a", lastModified: ISODate("2013-10-02T01:11:18.965Z") }  
如下操作更新lastModified字段为当前时间，cancellation.date字段设置为当前时间戳，并且更新status字段和cancellation.reason字段。  

db.users.update({ _id: 1 },{
$currentDate: {
lastModified: true,
"cancellation.date": { $type: "timestamp" }},
$set: {
status: "D",
"cancellation.reason": "user request"}})

更新的结果是：  
{"_id" : 1,"status" : "D","lastModified" : ISODate("2014-09-17T23:25:56.314Z"),  
"cancellation" : {  
"date" : Timestamp(1410996356, 1),  
"reason" : "user request"}}  

## <span id="head40"> 四、查询</span>

### <span id="head41"> （一）基本查询</span>

>db.collection.find(query, projection)

query ：可选，使用查询操作符指定查询条件  
projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。  

find() 方法以非结构化的方式来显示所有文档。如果你需要以易读的方式来读取数据，可以使用 pretty() 方法，语法格式如下：  
>db.collection_name.find().pretty()  

pretty() 方法以格式化的方式来显示所有文档。  

除了 find() 方法之外，还有一个 **findOne()** 方法，它只返回一个文档。  

### <span id="head42"> （二）distinct去重查询</span>

distinct，查询年龄为18,并且城市不重复的数据  
>db.test.distinct("city",{age:18})

### <span id="head43"> （三）count计数查询</span>

count，查询年龄为18的总数  
>db.test.find({age:18}).count()

### <span id="head44"> （四）Limit、Skip、sort限制查询</span>

limit()方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。  
> db.col.find({},{"title":1,_id:0}).limit(2)

skip方法同样接受一个数字参数作为跳过的记录条数。  
>db.col.find({},{"title":1,_id:0}).skip(2)

以下实例会跳过第一条符合条件的文档数据，显示第二条符合条件的文档数据。  
>db.col.find({},{"title":1,_id:0}).limit(1).skip(1)

sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。  
>db.COLLECTION_NAME.find().sort({KEY:1})

**skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。**

## <span id="head45"> 五、聚合</span>

### <span id="head46"> （一）aggergate()简介</span>

MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。有点类似sql语句中的 count(*)。  
aggregate() 方法的基本语法格式如下所示：  
>db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)

MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。  
表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。  
这里我们介绍一下聚合框架中常用的几个操作：  

运算符|说明
:---|:------------
$project|通过重命名，添加或删除字段重塑文档。你也可以重新计算值，并添加子文档。例如，下面的例子包括title并排除name：{$project:{title:1,name:0}} 以下是把name重命名为title的例子:{$project{title:"$name"}} 下面是添加一个新的total字段，并用price和tax字段计算它的值的例子:{$project{total:{$add:["$price","$tax"]}}}
$match|通过使用query对象运算符来过滤文档集，只输出符合条件的文档。
$limit|限定可以传递到聚合操作的下一个管道中的文档数量。例如{$limit:5}
$skip|指定处理聚合操作的下一个管道前跳过的一些文档
$unwind|将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。例如{$unwind:"$myArr"}
$group|把文档分成一组新的文档用于在管道中的下一级。新对象的字段必须在$group对象中定义。你还可以把表2中列出的分组表 达式运算符应用到该组的多个文档中。例如，使用下面的语句汇总value字段：{$group:{set_id:"$0_id",total:{$sum:"$value"}}}
$sort| 在把文档传递给处理聚合操作的下一个管道前对它们排序。排序指定一个带有field:sort_order属性的对象，其中sort_order 为1表示升序，而-1表示降序
$sample|随机选择N条documents，语法“{$sample: {size:20}}”。
$count|返回聚合管道此阶段的文档数量计数。
$cond|判断用的，可以跟if then 语句。
$redact|通过基于文档本身中存储的信息限制每个文档的内容来重塑流中的每个文档。包含$project和$match的功能。可用于实现字段级别的编辑。对于每个输入文档，输出一个或零个文档。
$lookup|对同一数据库中的另一个集合执行左外连接，以从“已连接”集合中过滤文档以进行处理。
$out|将聚合管道的结果文档写入集合。要使用$out舞台，它必须是管道中的最后一个阶段。
$facet|在同一组输入文档的单个阶段内处理多个聚合管道。支持创建能够在单个阶段中跨多个维度或方面表征数据的多面聚合。
$addFields|向文档添加新字段。类似于 $project，$addFields重塑流中的每个文档; 具体而言，通过向输出文档添加新字段，该文档包含输入文档和新添加字段中的现有字段。
$bucket|根据指定的表达式和存储区边界，将传入的文档分组，称为存储桶。
$bucketAuto|根据指定的表达式将传入的文档分类为特定数量的组（称为存储桶）。自动确定存储桶边界，以尝试将文档均匀地分配到指定数量的存储桶中。
$collStats|返回有关集合或视图的统计信息。
$geoNear|基于与地理空间点的接近度返回有序的文档流。集成的功能 $match，$sort以及$limit地理空间数据。输出文档包括附加距离字段，并且可以包括位置标识符字段。
$graphLookup|对集合执行递归搜索。对于每个输出文档，添加一个新的数组字段，其中包含该文档的递归搜索的遍历结果。
$indexStats|返回有关集合的每个索引的使用的统计信息。
$listSessions|列出活动时间足以传播到system.sessions集合的所有会话。
$replaceRoot|用指定的嵌入文档替换文档。该操作将替换输入文档中的所有现有字段，包括_id字段。指定嵌入在输入文档中的文档以将嵌入文档提升到顶层。
$sortByCount|根据指定表达式的值对传入文档进行分组，然后计算每个不同组中的文档计数。
$currentOp|返回有关MongoDB部署的活动和/或休眠操作的信息。要运行，请使用该db.aggregate()方法。
$listLocalSessions|列出最近在当前连接mongos或mongod实例上使用的所有活动会话 。这些会话可能尚未传播到system.sessions集合中。

### <span id="head47"> （二）聚合$group表达式运算符</span>

运算符|说明
:---|:------------
$sum|返回一组文档中以个字段的全部值的总和。例如:db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
$avg|返回一组文档中以个字段的平均值。例如:db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])
$max|返回一组文档中一个字段的最大值。例如:db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])
$min|返回一组文档中一个字段的最小值。例如:db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])
$push|在结果文档中插入值到一个数组中。返回一组文档中所有文档所选字段的全部值的数组。例如:db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])
$addToSet|在结果文档中插入值到一个数组中，但不创建副本。返回一组文档中所有文档所选字段的全部唯一值的数组。可去重。例如:db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])
$first|根据资源文档的排序获取第一个文档数据。例如：db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])
$last|根据资源文档的排序获取最后一个文档数据。例如:db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])

### <span id="head48"> （三）其他聚合运算符</span>

计算新的字段值时，可以应用一些字符串和算术运算符。下表列出了在聚合运算符中计算新字段值可以应用的最常用的一些运算符。

运算符|说明
:---:|:------------
$add|计算数值的总和。例如：valuePlus5:{$add:["$value",5]}
$divide|给定两个数值，用第一个数除以第二个数。例如：valueDividedBy5:{$divide:["$value",5]}
$mod|取模。例如:{$mod:["$value",5]}
$multiply|计算数值数组的乘积。例如:{$multiply:["$value",5]}
$subtract|给定两个数值，用第一个数减去第二个数。例如:{$subtract:["$value",5]}
$concat|连接两个字符串 例如：{$concat:["str1","str2"]}
$strcasecmp|比较两个字符串并返回一个整数来反应比较结果。例如 {$strcasecmp:["$value","$value"]}
$substr|返回字符串的一部分。例如:hasTest：{$substr:[< string > , < start > , < length >]}
$toLower|将字符串转化为小写。
$toUpper|将字符串转化为大写。

### <span id="head49"> （四）聚合例子</span>

#### <span id="head50"> 1、$project实例</span>

>db.article.aggregate({ $project : {title : 1 ,author : 1}});
这样的话结果中就只还有_id,tilte和author三个字段了，默认情况下_id字段是被包含的，如果要想不包含_id话可以这样:
>db.article.aggregate({ $project : {_id : 0 ,title : 1 ,author : 1}});

#### <span id="head51"> 2、$match实例</span>

$match用于获取分数大于70小于或等于90记录，然后将符合条件的记录送到下一阶段$group管道操作符进行处理。
>db.articles.aggregate( [{ $match : { score : { $gt : 70, $lte : 90 } } },{ $group: { _id: null, count: { $sum: 1 } } }]);

#### <span id="head52"> 3、$skip实例</span>

经过$skip管道操作符处理后，前五个文档被"过滤"掉。
>db.article.aggregate({ $skip : 5 });

#### <span id="head53"> 4、$group实例</span>

db.getCollection("project_2018_2019").aggregate([
{"$match":{"buyer_gov":1,"bidopentime":{$gt:1546272000,$lt:1577808000},$or:[{bidstatus:"中标"},{bidstatus:"成交"},{bidstatus:"合同"}],"budget":{$lt:10000000000}}},
{"$group":{"_id":{"buyer_gov":"$buyer_gov"},"count":{"$sum":1},"sum1":{"$sum":"$bidamount"},"sum2":{"$sum":"$budget"}}}]).toArray();

最终结果仅包含buyer_gov、count、sum1、sum2。

#### <span id="head54"> 5、$concat实例</span>

连接符，用来连接两个或者多个字符串，仅支持在aggregate中使用。
>{$concat:["$field1","-","$field2"]}

#### <span id="head55"> 6、$add、$subtract、$multiply、$divide</span>

加减乘除，仅支持在aggregate中使用。

>{$add:["field1","field2"]}
>{$subtract:["field1","field2"]}
>{$multiply:["$field1","$field2"]}
>{$divide:["$field1","$field2"]}

在聚合使用时，通常和match联合使用，例如：
db.seoProduceAnalyse.aggregate([
{"$project":{"val":{"$subtract":["$a","$b"]}}},
{"$match":{"val":{"$lt":1}}},
{"$group":{"_id":1,"count":{"$sum":1}}}])

意为：a与 b两个值减得到值val；条件是val<1，按照_id展示count的数量。

#### <span id="head56"> 7、$cond条件及其if-else使用</span>

例1：
{ "_id" : 1, "item" : "abc1", qty: 300 }
{ "_id" : 2, "item" : "abc2", qty: 200 }
{ "_id" : 3, "item" : "xyz1", qty: 250 }

现在我们想根据qty的值来生成新的数据（值）

db.inventory.aggregate([{$project:{
item: 1,
discount:{
$cond:{
if:{$gte: [ "$qty", 250 ]},
then: 30,
else: 20 }}}}])

结果为：  
{ "_id" : 1, "item" : "abc1", "discount" : 30 }  
{ "_id" : 2, "item" : "abc2", "discount" : 20 }  
{ "_id" : 3, "item" : "xyz1", "discount" : 30 }  
可以发现，discount是我们新的键，它根据cond的if判断后，分别被赋上了相应的值（then和else可以省略）  

例2（高级聚合使用）：  
报表生成中使用了mongodb的$cond 及其if else语句；mongodb不支持case when语句。  
功能：对影片观看时间统计用户数（1、十分钟以内观看记录用户；2、10-30分钟；3、30-80分钟；4、80分钟以上）；  

temp_result = self.db[Constants.action_table].aggregate([
{"$match":{'actionInfo.status':7}},
{"$group": {"_id": {"mac": '$mac',"sn": '$sn',"day_time": {"$substrBytes": ["$time", 0, 10]}},"duration": {'$sum':"$actionInfo.consumeTime"}}},
{"$project":{"_id": 0,"day_time": "$_id.day_time","mac":"$_id.mac","sn": "$_id.sn","duration":"$duration","discount":{
"$cond": {
"if": { "$lt": ['$duration', 600000]},"then": "10分钟内",
"else": {
"$cond": {
"if": {  "$and": [{ "$gte": ["$duration",600000 ]}, { "$lt": ["$duration", 18000000]}]},"then": "10-30分钟",
"else": {
"$cond": {
"if": {  "$and": [{ "$gte": ["$duration", 18000000]}, { "$lte": ["$duration", 48000000]}]},"then" : "30-80分钟",
"else": "80分钟以上"}}}}}}}},
{"$out": "TotalUserAverageDailyLengthRound_temp"}]);

self.db["TotalUserAverageDailyLengthRound_temp"].aggregate([
{"$group": {"_id": {"day_time": '$day_time',"discount": '$discount',}, "countUser": {'$sum': 1}}},
{"$project":{"_id": 0,"day_time": "$_id.day_time","discount": "$_id.discount","countUser": "$countUser"}},
{"$out": self.currentTable()}]);
return temp_result;

#### <span id="head57"> 8、$redact操作符的使用</span>

根据字段所处的document结构的级别，对文档进行“修剪”，它通常和“判断语句if-else”结合使用即“$cond”。$redact可选值有3个：  
1）$$DESCEND：包含当前document级别的所有fields。当前级别字段的内嵌文档将会被继续检测。  
2）$$PRUNE：不包含当前文档或者内嵌文档级别的所有字段，不会继续检测此级别的其他字段，即使这些字段的内嵌文档持有相同的访问级别。  
3）$$KEEP：包含当前文档或内嵌文档级别的所有字段，不再继续检测此级别的其他字段，即使这些字段的内嵌文档中持有不同的访问级别。  

例1：

{$redact:{$cond:{
if: { $gt: [ { $size: { $setIntersection: [ "$tags", userAccess ] } }, 0 ] },  // $setIntersection 多个数组的交集，返回数组
then:"$$DESCEND",  //满足条件则保留对应等级文档的内容
else:"$$PRUNE",  //否则剔除掉该子文档
}}}

{$redact: {
$cond: {
if: { $eq: [ "$level", 5 ] },
then: "$$PRUNE",
else: "$$DESCEND"
}}}

例2：

{_id: 1,tags: [ "G", "STLW" ],year: 2014,
subsections: [{
subtitle: "Section 1",
tags: [ "SI", "G" ],},{
subtitle: "Section 2",
tags: [ "STLW" ],},{
subtitle: "Section 3",
tags: [ "TK" ],
content: {
tags: [ "HCS" ]}}]}

对于语句：

$redact: {$cond: {
if: {$gt: [ { $size: { $setIntersection: [ "$tags", ["STLW","G"] ] } }, 0 ] },
then: "$$DESCEND",
else: "$$PRUNE"}}

输出结果：  
{"_id" : 1,"tags" : [ "G", "STLW" ],"year" : 2014,  
"subsections" : [{  
"subtitle" : "Section 1",  
"tags" : [ "SI", "G" ],  
"content" : "Section 1"},{  
"subtitle" : "Section 2: Analysis",  
"tags" : [ "STLW" ],  
"content" : "Section 2"}]}  

#### <span id="head58"> 9、字段比较</span>

aggregate方法查询 fields1 与 fields2字段值相同:  

db.test.aggregate([
{$project:{fields1:1,fields2:1,difference:{$eq:["$fields1","$fields2"]}}},
{$match:{difference:true}},
{$limit:10}]);
difference=true值相同 false值不相同  
ps:由于aggregate不支持$where,所以需要用$project比较后在用$match进行条件筛选。  

#### <span id="head59"> 10、时间聚合统计</span>

例如时间字段  
mongodb的聚合框架（aggregate）提供了很多修改器用来修改去获取IOSDate类型的字段的年、月、日、时、分、秒、等；同时mongodb也提供了相关的修改器去把IOSDate类型的时间转换为通常我们可以接受的时间格式；  

$dayOfYear: 返回该日期是这一年的第几天。（全年366天）  
$dayOfMonth: 返回该日期是这一个月的第几天。（1到31）  
$dayOfWeek: 返回的是这个周的星期几。（1：星期日，7：星期六）  
$year: 返回该日期的年份部分  
$month： 返回该日期的月份部分（between 1and12.）  
$week： 返回该日期是所在年的第几个星期（between 0and53）  
$hour： 返回该日期的小时部分 $minute: 返回该日期的分钟部分  
$second: 返回该日期的秒部分（以0到59之间的数字形式返回日期的第二部分，但可以是60来计算闰秒。）  
$millisecond：返回该日期的毫秒部分（between 0and999.）  
$dateToString： { $dateToString: { format: formatString, date: dateExpression} }  

formatString：需要返回的日期式，日期格式通常为以：  

格式|说明|示例
:---|:------------|:--
%Y|Year (4 digits, zero padded)|0000-9999
%m|Month (2 digits, zero padded)|01-12
%d|Day of Month (2 digits, zero padded)|01-31
%H|Hour (2 digits, zero padded, 24-hour clock)|00-23
%M|Minute (2 digits, zero padded)|00-59
%S|Second (2 digits, zero padded)|00-60
%L|Millisecond (3 digits, zero padded)|000-999
%j|Day of year (3 digits, zero padded)|001-366
%w|Day of week (1-Sunday, 7-Saturday)|1-7
%U|Week of year (2 digits, zero padded)|00-53
%%|Percent Character as a Literal

以下是案例：  
date1Str: 转换时间格式比标准时间差了8小时，date2Str：转换时间正确。  

db.test.aggregate([{
$project: {timestamp: 1,
date1Str: {$dateToString: {format: "%Y-%m-%d %H:%M:%S:%L", date:{"$add":[new Date(0),"$timestamp"]}}},
date2Str: {$dateToString: {format: "%Y-%m-%d %H:%M:%S:%L", date:{"$add":[new Date(0),"$timestamp",28800000]}}}}}])

"$add":[new Date(0),"$timestamp"] ，这是为了把$timestamp的值转为Date类型。  

#### <span id="head60"> 11、$substr截取字符串</span>

$substr,$substrBytes,$substrCP是aggregate的管道操作符，$substr在版本3.4后最好使用$substrBytes。  
$substr与$substrBytes结果相同，会将汉字的字符长度视为2，$substrCP将汉字的字符长度视为1。  

db.getCollection("a").aggregate({
$project:{
a:{$substr:['article_link这是汉字387540859',5,10]},
b:{$substrBytes:['article_link这是汉字387540859',5,10]},
c:{$substrCP:['article_link这是汉字387540859',5,10]}}})

结果：
{_id:1,a:"le_link这",b:"le_link这",c:"le_link这是汉"}

<!---->

db.getCollection("a").aggregate({
$project:{
url:"$article_link",
a:{$substr:['$article_link',10,10]},
b:{$substrBytes:['$article_link',10,10]},
c:{$substrCP:['$article_link',10,10]}}})

结果：
{_id:1,url:"https:aadoi.org/10.13109/zptm.2019.65.1.1",a:"i.org/10.1",b:"i.org/10.1",c:"i.org/10.1"}

#### <span id="head61"> 12、$lookup实例</span>

db.user.aggregate([{
$lookup: { // 左连接
from: "order", // 关联到order表
localField: "uid", // user 表关联的字段
foreignField: "uid", // order 表关联的字段
as: "orders"}

<!---->

db.getCollection("prodata_18_19_zbgg").aggregate([
{"$lookup":{from: "project_2018_2019_all_1",localField:"company_name",foreignField:"winner",as: "prodata"}},
{"$match":{"prodata.buyer_gov":1,"prodata.bidopentime":{$gte:1546272000,$lt:1577808000},"province":"江西","prodata.area":{$ne:"江西"}}},
{"$group":{"_id":{"province":"$province"},"count":{"$sum":1}}}]).toArray();

表的关联查询，如果没有索引或者数据量太大，就别用了，速度太慢。  

## <span id="head62"> 六、索引</span>

### <span id="head63"> （一）常规索引语法</span>

索引通常能够极大的提高查询的效率，特别在处理大量的数据时。索引是特殊的数据结构，存储在一个易于遍历读取的数据集合中，是对数据库表中一列或多列的值进行排序的一种结构。  

createIndex()方法基本语法格式如下所示：  
>db.collection.createIndex(keys, options)  

语法中 Key 值为你要创建的索引字段，1 为指定按升序创建索引，如果你想按降序来创建索引指定为 -1 即可。  
注意在 3.0.0 版本前创建索引方法为 db.collection.ensureIndex()，之后的版本使用了 db.collection.createIndex() 方法，ensureIndex() 还能用，但只是 createIndex() 的别名。  

createIndex() 方法中你也可以设置使用多个字段创建索引（关系型数据库中称作复合索引）。  
>db.col.createIndex({"title":1,"description":-1})  

在后台创建索引：  
>db.values.createIndex({open: 1, close: 1}, {background: true})  

createIndex()接收可选参数，例如：background，可选参数列表如下：  

Parameter|Type|Description
:---|:------------ |:--
background|Boolean|建索引过程会阻塞其它数据库操作，background可指定以后台方式创建索引，即增加 "background" 可选参数。 "background" 默认值为false。
unique|Boolean|建立的索引是否唯一。指定为true创建唯一索引。默认值为false.
name|string|索引的名称。如果未指定，MongoDB的通过连接索引的字段名和排序顺序生成一个索引名称。
dropDups|Boolean|**3.0+版本已废弃。**  在建立唯一索引时是否删除重复记录,指定 true 创建唯一索引。默认值为 false.
sparse|Boolean|对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档.。默认值为 false.
expireAfterSeconds|integer|指定一个以秒为单位的数值，完成 TTL设定，设定集合的生存时间。
v|index version|索引的版本号。默认的索引版本取决于mongod创建索引时运行的版本。
weights|document|索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重。
default_language|string|对于文本索引，该参数决定了停用词及词干和词器的规则的列表。 默认为英语
language_override|string|对于文本索引，该参数指定了包含在文档中的字段名，语言覆盖默认的language，默认值为 language.

### <span id="head64"> （二）其他索引语法</span>

1.查看集合索引
>db.col.getIndexes()

2.查看集合索引大小
>db.col.totalIndexSize()

3.删除集合所有索引
>db.col.dropIndexes()

4.删除集合指定索引
>db.col.dropIndex("索引名称")

### <span id="head65"> （三）高级索引</span>

{"address": {  
"city": "Los Angeles",  
"state": "California",  
"pincode": "123"},  
"tags": ["music","cricket","blogs"],  
"name": "Tom Benzamin"}  

以上文档包含了 address 子文档和 tags 数组。  

索引数组字段  
假设我们基于标签来检索用户，为此我们需要对集合中的数组 tags 建立索引。  
在数组中创建索引，需要对数组中的每个字段依次建立索引。所以在我们为数组 tags 创建索引时，会为 music、cricket、blogs三个值建立单独的索引。  
使用以下命令创建数组索引：  
>db.users.ensureIndex({"tags":1}  

创建索引后，我们可以这样检索集合的 tags 字段：  
>db.users.find({tags:"cricket"})  

为了验证我们使用使用了索引，可以使用 explain 命令：  
>db.users.find({tags:"cricket"}).explain()  

以上命令执行结果中会显示 "cursor" : "BtreeCursor tags_1" ，则表示已经使用了索引。  

索引子文档字段  
假设我们需要通过city、state、pincode字段来检索文档，由于这些字段是子文档的字段，所以我们需要对子文档建立索引。  
为子文档的三个字段创建索引，命令如下：  
>db.users.ensureIndex({"address.city":1,"address.state":1,"address.pincode":1})  

一旦创建索引，我们可以使用子文档的字段来检索数据：  
>db.users.find({"address.city":"Los Angeles"})  

查询表达不一定遵循指定的索引的顺序，mongodb 会自动优化。所以上面创建的索引将支持以下查询：  
>db.users.find({"address.state":"California","address.city":"Los Angeles"})  

同样支持以下查询：  
>db.users.find({"address.city":"Los Angeles","address.state":"California","address.pincode":"123"})  

### <span id="head66"> （四）索引限制</span>

额外开销  
每个索引占据一定的存储空间，在进行插入，更新和删除操作时也需要对索引进行操作。所以，如果你很少对集合进行读取操作，建议不使用索引。  

内存(RAM)使用  
由于索引是存储在内存(RAM)中,你应该确保该索引的大小不超过内存的限制。  
如果索引的大小大于内存的限制，MongoDB会删除一些索引，这将导致性能下降。  

查询限制  
索引不能被以下的查询使用：  

* 正则表达式及非操作符，如 $nin, $not, 等。  
* 算术运算符，如 $mod, 等。  
* $where 子句  
所以，检测你的语句是否使用索引是一个好的习惯，可以用explain来查看。  

索引键限制  
从2.6版本开始，如果现有的索引字段的值超过索引键的限制，MongoDB中不会创建索引。  

插入文档超过索引键限制  
如果文档的索引字段值超过了索引键的限制，MongoDB不会将任何文档转换成索引的集合。与mongorestore和mongoimport工具类似。  

最大范围  

* 集合中索引不能超过64个  
* 索引名的长度不能超过128个字符  
* 一个复合索引最多可以有31个字段  

## <span id="head67"> 七、高级教程与操作</span>

### <span id="head68"> （一）MongoDB关系</span>

MongoDB 的关系表示多个文档之间在逻辑上的相互联系，文档间可以通过嵌入和引用来建立联系。  
MongoDB 中的关系可以是：  
1:1 (1对1)  
1: N (1对多)  
N: 1 (多对1)  
N: N (多对多)  
关系型数据库有的关系，MongoDB都有。  

#### <span id="head69"> 1、嵌入式关系</span>

{
"_id":ObjectId("52ffc33cd85242f436000001"),
"contact": "987654321",
"dob": "01-01-1991",
"name": "Tom Benzamin",
"address": [
{
"building": "22 A, Indiana Apt",
"pincode": 123456,
"city": "Los Angeles",
"state": "California"
},
{
"building": "170 A, Acropolis Apt",
"pincode": 456789,
"city": "Chicago",
"state": "Illinois"
}]
} 

以上数据保存在单一的文档中，可以比较容易的获取和维护数据。 你可以这样查询用户的地址：  
>db.users.findOne({"name":"Tom Benzamin"},{"address":1})

注意：这种数据结构的缺点是，如果用户和用户地址在不断增加，数据量不断变大，会影响读写性能。  

#### <span id="head70"> 2、引用式关系</span>

{
"_id":ObjectId("52ffc33cd85242f436000001"),
"contact": "987654321",
"dob": "01-01-1991",
"name": "Tom Benzamin",
"address_ids": [
ObjectId("52ffc4a5d85242602e000000"),
ObjectId("52ffc4a5d85242602e000001")
]
}

以上实例中，用户文档的 address_ids 字段包含用户地址的对象id（ObjectId）数组。我们可以读取这些用户地址的对象id（ObjectId）来获取用户的详细地址信息。这种方法需要两次查询，第一次查询用户地址的对象id（ObjectId），第二次通过查询的id获取用户的详细地址信息。  

>var result = db.users.findOne({"name":"Tom Benzamin"},{"address_ids":1})
>var addresses = db.address.find({"_id":{"$in":result["address_ids"]}})

注意这一句中的 findOne 不能写成 find，因为 find 返回的数据类型是数组，findOne 返回的数据类型是对象。  
如果这一句使用了 find，那么下面一句应该改写为:  
>var addresses = db.address.find({"_id":{"$in":result[0]["address_ids"]}})

### <span id="head71"> （二）数据库引用</span>

DBRef的形式：  
{ $ref : , $id : , $db :  }  

三个字段表示的意义为：  
$ref：集合名称  
$id：引用的id  
$db:数据库名称，可选参数  
以下实例中用户数据文档使用了 DBRef, 字段 address：  

{
"_id":ObjectId("53402597d852426020000002"),
"address": {
"$ref": "address_home",
"$id": ObjectId("534009e4d852427820000002"),
"$db": "runoob"},
"contact": "987654321",
"dob": "01-01-1991",
"name": "Tom Benzamin"
}

address DBRef 字段指定了引用的地址文档是在 runoob 数据库下的 address_home 集合，id 为 534009e4d852427820000002。  
以下代码中，我们通过指定 $ref 参数（address_home 集合）来查找集合中指定id的用户地址信息：  
>var user = db.users.findOne({"name":"Tom Benzamin"})  
>var dbRef = user.address  
>db[dbRef.$ref].findOne({"_id":(dbRef.$id)})  

>最后一句，在 MongoDB4.0 版本是这样写：
>db[dbRef.$ref].findOne({"_id":ObjectId(dbRef.$id)})

### <span id="head72"> （三）覆盖索引查询</span>

官方的MongoDB的文档中说明，覆盖查询是以下的查询：  

* 所有的查询字段是索引的一部分  
* 所有的查询返回字段在同一个索引中  

由于所有出现在查询中的字段是索引的一部分，MongoDB 无需在整个数据文档中检索匹配查询条件和返回使用相同索引的查询结果。因为索引存在于RAM中，从索引中获取数据比通过扫描文档读取数据要快得多。  

方法：  
1、创建索引：  
>db.users.createIndex({gender:1,user_name:1})

2、查询：  
>db.users.find({gender:"M"},{user_name:1,_id:0})

上述查询，称为覆盖索引查询。MongoDB不会去数据库文件中查找。相反，它会从索引中提取数据，这是非常快速的数据查询。  
由于我们的索引中不包括 _id 字段，_id在查询中会默认返回，我们可以在MongoDB的查询结果集中排除它。  

下面的实例没有排除_id，查询就不会被覆盖：  
>db.users.find({gender:"M"},{user_name:1})  

最后，如果是以下的查询，不能使用覆盖索引查询：  

* 所有索引字段是一个数组  
* 所有索引字段是一个子文档  

### <span id="head73"> （四）查询分析</span>

MongoDB 查询分析可以确保我们所建立的索引是否有效，是查询语句性能分析的重要工具。  
MongoDB 查询分析常用函数有：explain() 和 hint()。  
explain 操作提供了查询信息，使用索引及查询统计等。有利于我们对索引的优化。  

接下来我们在 users 集合中创建 gender 和 user_name 的索引：  
>db.users.ensureIndex({gender:1,user_name:1})

现在在查询语句中使用 explain ：  
>db.users.find({gender:"M"},{user_name:1,_id:0}).explain()

以上的 explain() 查询返回如下结果：  

{
"cursor" : "BtreeCursor gender_1_user_name_1",
"isMultiKey" : false,
"n" : 1,
"nscannedObjects" : 0,
"nscanned" : 1,
"nscannedObjectsAllPlans" : 0,
"nscannedAllPlans" : 1,
"scanAndOrder" : false,
"indexOnly" : true,
"nYields" : 0,
"nChunkSkips" : 0,
"millis" : 0,
"indexBounds" : {
"gender" : [
[
"M",
"M"
]
],
"user_name" : [
[
{
"$minElement" : 1
},
{
"$maxElement" : 1
}
]
]
}
}

现在，我们看看这个结果集的字段：  

* indexOnly: 字段为 true ，表示我们使用了索引。  
* cursor：因为这个查询使用了索引，MongoDB 中索引存储在B树结构中，所以这是也使用了 BtreeCursor 类型的游标。如果没有使用索引，游标的类型是  BasicCursor。这个键还会给出你所使用的索引的名称，你通过这个名称可以查看当前数据库下的system.indexes集合（系统自动创建，由于存储索引信息，这个稍微会提到）来得到索引的详细信息。  
* n：当前查询返回的文档数量。  
* nscanned/nscannedObjects：表明当前这次查询一共扫描了集合中多少个文档，我们的目的是，让这个数值和返回文档的数量越接近越好。  
* millis：当前查询所需时间，毫秒数。  
* indexBounds：当前查询具体使用的索引。  

使用 hint()  
虽然MongoDB查询优化器一般工作的很不错，但是也可以使用 hint 来强制 MongoDB 使用一个指定的索引。  
这种方法某些情形下会提升性能。 一个有索引的 collection 并且执行一个多字段的查询(一些字段已经索引了)。  
如下查询实例指定了使用 gender 和 user_name 索引字段来查询：  
>db.users.find({gender:"M"},{user_name:1,_id:0}).hint({gender:1,user_name:1})

可以使用 explain() 函数来分析以上查询：  
>db.users.find({gender:"M"},{user_name:1,_id:0}).hint({gender:1,user_name:1}).explain()

### <span id="head74"> （五）原子操作</span>

mongodb不支持事务，所以，在你的项目中应用时，要注意这点。无论什么设计，都不要要求mongodb保证数据的完整性。  
但是mongodb提供了许多原子操作，比如文档的保存，修改，删除等，都是原子操作。  
所谓原子操作就是要么这个文档保存到Mongodb，要么没有保存到Mongodb，不会出现查询到的文档没有保存完整的情况。  

products 文档：

{
"_id":1,
"product_name": "Samsung S3",
"category": "mobiles",
"product_total": 5,
"product_available": 3,
"product_bought_by": [
{
"customer": "john",
"date": "7-Jan-2014"
},
{
"customer": "mark",
"date": "8-Jan-2014"
}
]
}

在本文档中，我们已经嵌入客户买该产品的信息在 product_bought_by 字段中。现在，每当新客户购买的产品，我们会先检查该产品是否仍然可以使用  product_available 字段。如果是的话，我们将减少 product_available 字段的值，并在 product_bought_by 字段插入新客户的嵌入文档。此功能将使用 findAndModify 命令，因为它搜索并更新在同一个文档。  

db.products.findAndModify({ 
query:{_id:1,product_available:{$gt:0}}, 
update:{ 
$inc:{product_available:-1}, 
$push:{product_bought_by:{customer:"rob",date:"9-Jan-2014"}}}})

**以上的意思是，当id为1的商品，available的值大于0时，将执行更新：available - 1 ,并且将product_bought_by:{customer:"rob",date:"9-Jan-2014"}}插入到文档中。**

嵌入式文档并使用 findAndModify 查询的方法可以确保只有当它是提供产品的购买信息时被更新。 而整个此事务在同一个查询中的，所以是一个原子的。  

### <span id="head75"> （六）ObjectId</span>

ObjectId 是一个12字节 BSON 类型数据，有以下格式：  

* 前4个字节表示时间戳  
* 接下来的3个字节是机器标识码  
* 紧接的两个字节由进程id组成（PID）  
* 最后三个字节是随机数。  

MongoDB中存储的文档必须有一个"_id"键。这个键的值可以是任何类型的，默认是个ObjectId对象。  
在一个集合里面，每个文档都有唯一的"_id"值，来确保集合里面每个文档都能被唯一标识。  
MongoDB采用ObjectId，而不是其他比较常规的做法（比如自动增加的主键）的主要原因，因为在多个 服务器上同步自动增加主键值既费力还费时。  

创建新的ObjectId  
使用以下代码生成新的ObjectId：  
>newObjectId = ObjectId()

上面的语句返回以下唯一生成的id：  
ObjectId("5349b4ddd2781d08c09890f3")  

你也可以使用生成的id来取代MongoDB自动生成的ObjectId：  
>myObjectId = ObjectId("5349b4ddd2781d08c09890f4")

创建文档的时间戳  
由于 ObjectId 中存储了 4 个字节的时间戳，所以你不需要为你的文档保存时间戳字段，你可以通过 getTimestamp 函数来获取文档的创建时间:  
>ObjectId("5349b4ddd2781d08c09890f4").getTimestamp()

以上代码将返回 ISO 格式的文档创建时间：  
ISODate("2014-04-12T21:49:17Z")  

ObjectId 转换为字符串  
在某些情况下，您可能需要将ObjectId转换为字符串格式。你可以使用下面的代码：  
>new ObjectId().str

以上代码将返回Guid格式的字符串：  
5349b4ddd2781d08c09890f3

### <span id="head76">（七）Map Reduce</span>

Map-Reduce是一种计算模型，简单的说就是将大批量的工作（数据）分解（MAP）执行，然后再将结果合并成最终结果（REDUCE）。  
MongoDB提供的Map-Reduce非常灵活，对于大规模数据分析也相当实用。  

以下是MapReduce的基本语法：  

db.collection.mapReduce(
function() {emit(key,value);},  //map 函数
function(key,values) {return reduceFunction},   //reduce 函数
{out: collection,
query: document,
sort: document,
limit: number})

使用 MapReduce 要实现两个函数 Map 函数和 Reduce 函数,Map 函数调用 emit(key, value), 遍历 collection 中所有的记录, 将 key 与 value 传递给Reduce 函数进行处理。  
Map 函数必须调用 emit(key, value) 返回键值对。  

参数说明:  
map ：映射函数 (生成键值对序列,作为 reduce 函数参数)。  
reduce 统计函数，reduce函数的任务就是将key-values变成key-value，也就是把values数组变成一个单一的值value。  
out 统计结果存放集合 (不指定则使用临时集合,在客户端断开后自动删除)。  
query 一个筛选条件，只有满足条件的文档才会调用map函数。（query。limit，sort可以随意组合）  
sort 和limit结合的sort排序参数（也是在发往map函数前给文档排序），可以优化分组机制  
limit 发往map函数的文档数量的上限（要是没有limit，单独使用sort的用处不大）  

临时集合参数是这样写的out: { inline: 1 }  
设置了 {inline:1} 将不会创建集合，整个 Map/Reduce 的操作将会在内存中进行。  
注意，这个选项只有在结果集单个文档大小在16MB限制范围内时才有效。  
db.users.mapReduce(map,reduce,{out:{inline:1}});  

更多内容见：https://www.runoob.com/mongodb/mongodb-map-reduce.html  

### <span id="head77"> （八）固定集合</span>

MongoDB 固定集合（Capped Collections）是性能出色且有着固定大小的集合，对于大小固定，我们可以想象其就像一个环形队列，当集合空间用完后，再插入的元素就会覆盖最初始的头部的元素！  
>db.createCollection("cappedLogCollection",{capped:true,size:10000,max:1000})

size 是整个集合空间大小，单位为【KB】  
max 是集合文档个数上线，单位是【个】  
如果空间大小到达上限，则插入下一个文档时，会覆盖第一个文档；如果文档个数到达上限，同样插入下一个文档时，会覆盖第一个文档。两个参数上限判断取的是【与】的逻辑。  

属性  
属性1:对固定集合进行插入速度极快  
属性2:按照插入顺序的查询输出速度极快  
属性3:能够在插入最新数据时,淘汰最早的数据  

用法  
用法1:储存日志信息  
用法2:缓存一些少量的文档  

### <span id="head78"> （九）自定义函数</span>

可以把自己写的js代码保存在某个地方，让MongoDB加载它，然后就可以在MongoDB的命令行里操作它们。  
暂时用不到，不汇总了。  

## <span id="head79"> 八、集合方法大全</span>

方法名|描述
:---|:---
db.collection.aggregate()|聚合，主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果
db.collection.bulkWrite()|批量写入
db.collection.createIndex()|创建一个集合索引
db.collection.count()|返回集合总数或匹配查询的结果集总数
db.collection.deleteOne()|删除集合中的一个文档
db.collection.deleteMany()|删除集合中的多个文档
db.collection.dataSize()|返回集合的大小
db.collection.distinct()|返回具有指定字段不同值的文档（去除指定字段的重复数据）
db.collection.dropIndex()|删除一个集合中的指定索引
db.collection.dropIndexes()|删除一个集合中的所有索引
db.collection.drop()|删除当前数据库中的collection集合
db.collection.explain()|返回各种方法的查询执行信息
db.collection.ensureIndex()|已过时，现使用db.collection.createIndex()
db.collection.findOne()|查询单条数据
db.collection.findOneAndReplace()|查询单条数据并替换
db.collection.findOneAndDelete()|查询单条数据并删除
db.collection.findOneAndUpdate()|查询单条数据并更新
db.collection.find()|查询集合，无参数则查询所有，并返回一个游标对象
db.collection.findAndModify()|查询并修改
db.collection.getIndexes()|返回当前集合的所有索引数组
db.collection.group()|提供简单的数据聚合功能
db.collection.isCapped()|判断集合是否为定容量
db.collection.insert()|在当前集合插入一条或多条数据（或叫文档）
db.collection.insertMany()|在当前集合插入多条数据
db.collection.insertOne()|在当前集合插入一条数据
db.collection.reIndex()|重建当前集合的所有索引
db.collection.renameCollection()|重命名集合名称
db.collection.replaceOne()|替换集合中的一个文档（一条数据）
db.collection.remove()|从当前集合删除数据
db.collection.save()|已插入数据更新
db.collection.stats()|返回当前集合的状态
db.collection.storageSize()|返回当前集合已使用的空间大小
db.collection.totalSize()|返回当前集合的总占用空间，包括所有文件和所有索引
db.collection.totalIndexSize()|返回当前集合所有的索引所占用的空间大小
db.collection.updateMany()|修改集合中的多条数据
db.collection.update()|修改集合中的数据
db.collection.updateOne()|修改集合中的一条数据
db.collection.validate()|执行对集合验证操作

## <span id="head80"> 九、数据库方法大全</span>

方法名|描述
:---|:---
db.cloneDatabase(）|从指定主机上克隆数据库
db.currentOp()|显示当前正在进行的操作
db.commandHelp()|返回数据库命令的帮助信息
db.createCollection()|创建一个聚集集合（table）
db.cloneCollection()|在MongoDB实例之间复制集合数据
db.copyDatabase(）|从指定的机器上复制指定数据库数据到某个数据库
db.dropDatabase();|删除当前使用数据库
db.fsyncLock()|刷新写入磁盘并锁定该数据库，以防止写入操作，并协助备份操作
db.fsyncUnlock()|允许继续进行写入锁住的数据库（解锁）
db.getLogComponents()|返回日志消息详细级别
db.getLastErrorObj()|查看完整的错误结果
db.getMongo()|查看当前db的链接机器地址
db.getCollection(）|得到指定名称的聚集集合（table）
db.getName()|查看当前使用的数据库
db.getPrevError()|返回包含自上次错误复位所有的错误状态文件
db.getCollectionNames()|得到当前db的所有聚集集合
db.getCollectionInfos()|返回当前数据库中的所有集合信息
db.getLastError()|返回上一次错误，如果没有错误则为空
db.hostInfo()|返回当前数据库主机系统的相关信息
db.killOp()|终止指定的操作
db.listCommands()|显示公共数据库的命令列表
db.logout()|注销登录
db.printCollectionStats()|显示当前db所有聚集索引的状态
db.resetError()|重置db.getPrevError()和getPrevError返回的错误信息
db.repairDatabase()|修复当前数据库
db.repairDatabase()|修复当前数据库
db.runCommand()|运行一个数据库命令
db.serverStatus()|返回当前数据库状态的概要
db.setProfilingLevel()|修改当前数据库的分析级别
db.stats()|显示当前db状态
db.shutdownServer()|关闭当前数据库运行实例或安全停止有关操作进程
db.setLogLevel()|设置一个单独的日志信息级别
db.version()|查看当前db版本

## <span id="head81"> 十、Studio3T小技巧</span>

用Studio 3T进行聚合查询时，如果结果太多，容易显示不全。提示“type it for more”。想要查询全部结果，可以在语句后加.toArray()或.forEach(printjson)。区别是：  
.toArray()是标准格式所有结果都在一个数组中，便于用脚本转换成csv表格文件，进一步操作。  
.forEach(printjson)是独立的一条条结果，便于直接查看。  

## <span id="head82"> 十一、忠告</span>

* 对MongoDB的操作，尽量使用MongoDB语句，而不是用python语句，尤其是for循环，太影响效率了。  
* MongoDB自带的语句基本能满足所有对MongoDB的操作，包括根据条件打标签。  
