<p align = "right"> :man_teacher: :handshake: :man_student:  &emsp; :pray: &emsp; :point_up_2: :heavy_plus_sign: :star: </p>  

# Markdown常用语法汇总
 
**Markdown语法的版本不止一种，以下仅列举GitHub风格的Markdown(简称GFM)规范语法，本文正文用Markdown语法书写，原始语句及注释放在区块中(tab键、4个空格、```都可以生成区块，而且第三种还支持代码高亮)供参考：**

&emsp;

<!-- code_chunk_output -->

- [一、基础语法](#一-基础语法)
  - [1.1 标题](#11-标题)
  - [1.2 行段](#12-行段)
  - [1.3 标记](#13-标记)
  - [1.4 引用](#14-引用)
  - [1.5 序列](#15-序列)
  - [1.6 分割线](#16-分割线)
  - [1.7 转义符](#17-转义符)
  - [1.8 隐文本](#18-隐文本)

[//]: # (我是来分行的)  

- [二、插入语法](#二-插入语法)
  - [2.1 插入任务](#21-插入任务)
  - [2.2 插入表情](#22-插入表情)
  - [2.3 插入链接](#23-插入链接)
  - [2.4 插入邮箱](#24-插入邮箱)
  - [2.5 插入代码](#25-插入代码)
  - [2.6.1 插入表格](#261-插入表格)
  - [2.6.2 表格合并](#262-表格合并)
  - [2.6.3 格内换行](#263-格内换行)
  - [2.7.1 插入图片](#271-插入图片)
  - [2.7.2 插入带链接图片](#272-插入带链接图片)
  - [2.8.1 图片和链接的标记引用:star:](#281-图片和链接的标记引用star)
  - [2.8.2 连接Github本仓库的URL](#282-连接github本仓库的url)

[//]: # (我是来分行的)  

- [三、排版语法](#三-排版语法)
  - [3.1 缩进](#31-缩进)
  - [3.2 居中](#32-居中)
  - [3.3 文章锚点](#33-文章锚点)
  - [3.4 文字绕图](#34-文字绕图)
  - [3.5 勉强配色](#35-勉强配色)
  - [3.6 保留区块格式](#36-保留区块格式)
  - [3.7 图片大小位置](#37-图片大小位置)  

[//]: # (我是来分行的)  

- [四、One more thing](#四-one-more-thing)
  - [4.1 Github不支持的语法](#41-github不支持的语法)
  - [4.2 VScode Markdown的使用](#42-vscode-markdown的使用)
  - [4.3 Markdown辅助工具](#43-markdown辅助工具)

<!-- /code_chunk_output -->

&emsp;

## 一. 基础语法

### 1.1 标题

	# 一级标题
	## 二级标题
	### 三级标题

	大标题  
	====

	中标题  
	-------

	关于标题需要注意：  
	1、#与标题之间要有空格；  
	2、一篇文章通常只有一个一级标题；  
	3、一级标题和二级标题下会有分割线；  
	4、六级标题默认显示为浅灰色，通常可以用来做非主要信息的补充；  
	5、除了用 # 来表达标题，还可以用=、-来表示，数量通常要大于3个，= 对应一级标题，-对应二级标题。

### 1.2 行段

	两个空格+回车表示换行，或者使用html语言换行标签：<br>或者<br/>
	空行表示分段。

### 1.3 标记

**1.3.1 语义标记**

*斜体*、_斜体_  
**加粗**  
***加粗+斜体***、**_加粗+斜体_**  
~~删除线~~  

**1.3.2 语义标签**

<i>斜体</i>  
<b>加粗</b>  
<em>强调</em>  
<u>下划线</u>   
<del>删除</del>  
Z<sup>a</sup>  
Z<sub>a</sub>  
<kbd>Ctrl</kbd>，`ctrl `

	**1.3.1 语义标记**
	*斜体*、_斜体_  
	**加粗**  
	***加粗+斜体***、**_加粗+斜体_**  
	~~删除线~~  

	**1.3.2 语义标签**
	<i>斜体</i>  
	<b>加粗</b>  
	<em>强调</em>  
	<u>下划线</u>   
	<del>删除</del>  
	Z<sup>a</sup>  
	Z<sub>a</sub>  
	<kbd>Ctrl</kbd>，`ctrl `
	最后一个是行内标记的两种用法，常用第二种，注意那不是单引号，而是1左边的英文下按键,该方法用来标记行内代码或其他需要着重强调的文本。

### 1.4 引用

> hello world!  输入完之后按两次空格键再按一次Enter键即可  
> hello world!  输入完之后按两次空格键再按一次Enter键即可  
> hello world!  输入完之后按两次空格键再按一次Enter键即可  

> aaaaaaaaa
>> bbbbbbbbb
>>> cccccccccc

	> hello world!  输入完之后按两次空格键再按一次Enter键即可  
	> hello world!  输入完之后按两次空格键再按一次Enter键即可  
	> hello world!  输入完之后按两次空格键再按一次Enter键即可  

	> aaaaaaaaa
	>> bbbbbbbbb
	>>> cccccccccc
	在一个引用中换行，按两个空格即可，嵌套引用使用多个大于号就行。

### 1.5 序列

1. one
2. two
3. three

* one
* two
* three

1. one
	1. one-1
	0. two-2
		1. one-1
		2. two-2
2. two
	* two-1
	* two-2

* 一级
	- 二级
		- 三级
			* 四级
				- 五级  

&emsp;

	1. one
	2. two
	3. three

	* one
	* two
	* three

	1. one
		1. one-1
		0. two-2
			1. one-1
			2. two-2
	2. two
		* two-1
		* two-2

	* 一级
		- 二级
			- 三级
				* 四级
					- 五级 

	1.星号后面必须有空格才会变成大圆点，这里*和-同义，还有+都可以，但最好统一；
	2.序列的使用与上行紧挨不空行，二级序列递进缩进；
	3.二级有序序列中的数字有时会被转成罗马数字，三级有序序列中的数字有时会被转成英文字母。

### 1.6 分割线

***
------
___

* * *

- - -

	***
	------
	___

	* * *
	- - -
	可以在一行中使用三个或更多的*，-或_来添加分隔线。

### 1.7 转义符

转义符'\'  
转义符\<br>

	转义符'\'  
	转义符\<br>
	转义符的作用是拒绝语法翻译。

### 1.8 隐文本

[//]: # (1、哈哈我是注释，不会在浏览器中显示。)  
[^_^]: # (2、哈哈我是注释，不会在浏览器中显示。)  
[//]: <> (3、哈哈我是注释，不会在浏览器中显示。)
[comment]: <> (4、哈哈我是注释，不会在浏览器中显示。)
<!--5、哈哈我是注释，不会在浏览器中显示。-->
<!--
6、哈哈我是多段
注释，
不会在浏览器中显示。
-->

	[//]: # (1、哈哈我是注释，不会在浏览器中显示。)  
	[^_^]: # (2、哈哈我是注释，不会在浏览器中显示。)  
	[//]: <> (3、哈哈我是注释，不会在浏览器中显示。)
	[comment]: <> (4、哈哈我是注释，不会在浏览器中显示。)
	<!--5、哈哈我是注释，不会在浏览器中显示。-->
	<!--
	6、哈哈我是多段
	注释，
	不会在浏览器中显示。
	-->
	你什么也没看到，因为这些都是隐藏语法。

## 二. 插入语法

### 2.1 插入任务

- [ ] 选项一
- [x] 选项二
	- [ ] 选项一
	- [x] 选项二

&emsp;

	- [ ] 选项一
	- [x] 选项二
		- [ ] 选项一
		- [x] 选项二

### 2.2 插入表情

:smile:    :laughing:
:blush:    :smiley:
:smirk:    :heart_eyes:

	:smile:    :laughing:
	:blush:    :smiley:
	:smirk:    :heart_eyes:
	Markdown支持添加emoji表情，输入不同的符号码（两个冒号包围的字符）可以显示出不同的表情，但在VScode Github的Markdown预览中不显示。

### 2.3 插入链接

[百度](http://www.baidu.com/ '百度一下')  
www.biadu.com  
http://http://www.baidu.com  

	[百度](http://www.baidu.com/ '百度一下')
	www.biadu.com  
	http://http://www.baidu.com  
	[]中括号中为连接显示的内容，后面引号中'百度一下'在鼠标移到'百度'二字时，会浮动显示，注意：与链接之间有空格。
	Github支持直接写的链接，像这样：www.biadu.com http://http://www.baidu.com  
	点击该链接，会在原窗口打开，Github不支持在新窗口打开链接的语法。

### 2.4 插入邮箱

<xxx@outlook.com>
 
	<xxx@outlook.com>

### 2.5 插入代码

```python
from  pymongo import MongoClient
db = MongoClient('192.168.1.201', 30085).testdb
collection = db.bidding
for item in collection.aggregate([{'$sample': {'size':200}}]):
    print(item["_id"])
    collection2.save(item)
```

	```python
	from  pymongo import MongoClient
	db = MongoClient('192.168.1.201', 30085).testdb
	collection = db.bidding
	for item in collection.aggregate([{'$sample': {'size':200}}]):
		print(item["_id"])
		collection2.save(item)
	```
	需要在代码的上一行和下一行用```标记。``` 不是三个单引号，而是数字1左边，Tab键上面的键，同时在前```后加上你的编程语言即可（忽略大小写）。

```diff
+ 人闲桂花落，
- 夜静春山空。
! 月出惊山鸟，
# 时鸣春涧中。
```

	```diff
	+ 人闲桂花落，
	- 夜静春山空。
	! 月出惊山鸟，
	# 时鸣春涧中。
	```
	diff是Github支持的比较语法，+表示增加行，-表示删除行，!表示有差别，#表示备注。

### 2.6.1 插入表格

|a|b|c|
|:--:|:--|--:|
|居中|左对齐|右对齐|

a  |  b  | c  
:---:|:------------ |--:
居中 |  左对齐 |  右对齐 

	|a|b|c|
	|:--:|:--|--:|
	|居中|左对齐|右对齐|

	a  |  b  | c  
	:---:|:------------ |--:
	居中 |  左对齐 |  右对齐 

	第二行是表头与内容的分割，用':'表示对齐方式，第二种为简约写法，里面的空格不会被显示出来，通常使用空格使语法对齐。

### 2.6.2 表格合并

<table>
    <tr>
        <td>列一</td> 
        <td>列二</td> 
   </tr>
   <tr>
        <td colspan="2">合并行</td>    
   </tr>
   <tr>
        <td>列一</td> 
        <td>列二</td> 
   </tr>
    <tr>
        <td rowspan="2">合并列</td>    
        <td >行二列二</td>  
    </tr>
    <tr>
        <td >行三列二</td>  
    </tr>
</table>
*******************************
<table>
<tr>
    <td rowspan="7"> 文件状态：<br/>
        [√] 草稿<br/>
        [√] 正在修改<br/>
        [√] 正式发布 </td>
    <td>文件标识：</td>
    <td> </td>
</tr>
<tr>
    <td>当前版本：</td>
    <td>2.7</td>
</tr>
<tr>
    <td>作    者：</td>
    <td></td>
</tr>
<tr>
    <td>创建日期：</td>
    <td></td>
</tr>
<tr>
    <td>最后更新：</td>
    <td></td>
</tr>
<tr>
    <td>密    级：</td>
    <td></td>
</tr>
<tr>
    <td>版权说明：</td>
    <td></td>
</tr>
</table>

	<table>
		<tr>
			<td>列一</td> 
			<td>列二</td> 
	</tr>
	<tr>
			<td colspan="2">合并行</td>    
	</tr>
	<tr>
			<td>列一</td> 
			<td>列二</td> 
	</tr>
		<tr>
			<td rowspan="2">合并列</td>    
			<td >行二列二</td>  
		</tr>
		<tr>
			<td >行三列二</td>  
		</tr>
	</table>
	*******************************
	<table>
	<tr>
		<td rowspan="7"> 文件状态：<br/>
			[√] 草稿<br/>
			[√] 正在修改<br/>
			[√] 正式发布 </td>
		<td>文件标识：</td>
		<td> </td>
	</tr>
	<tr>
		<td>当前版本：</td>
		<td>2.7</td>
	</tr>
	<tr>
		<td>作    者：</td>
		<td></td>
	</tr>
	<tr>
		<td>创建日期：</td>
		<td></td>
	</tr>
	<tr>
		<td>最后更新：</td>
		<td></td>
	</tr>
	<tr>
		<td>密    级：</td>
		<td></td>
	</tr>
	<tr>
		<td>版权说明：</td>
		<td></td>
	</tr>
	</table>
	
	<table></table>表示表，<tr></tr>表示行，<th></th>表示表头，<td></td>表示单元格，<td rowspan="7">表示向下占7列，<td colspan="2">表示向右占2列。(一个<table>元素包含多个<tr>元素，一个<tr>元素包含一个或多个<th>或<td>元素)

### 2.6.3 格内换行

| Header1 | Header2                          |
|---------|----------------------------------|
| item 1  | 1. one<br/>2. two<br/>3. three |


	| Header1 | Header2                          |
	|---------|----------------------------------|
	| item 1  | 1. one<br />2. two<br />3. three |
	借助了HTML里的 <br/> 来实现。

### 2.7.1 插入图片

  ![图片](https://github.com/guodongxiaren/README/raw/master/img/csdn.png '描述')

	![图片](https://github.com/guodongxiaren/README/raw/master/img/csdn.png '描述')
	插入图片的代码比链接多了'!'，前面[]中内容正常不显示，仅在图片失效时显示，后面'描述'在鼠标移到图片时，会浮动显示。插入图片最好使用网络图床，比如：Github，七牛。
	如果使用github，需要注意：把图片地址中的blob改为raw，例如：
	图片地址：https://github.com/446020169/open/blob/master/Subscribe_report/Image/1.1.jpg
	图床地址：https://github.com/446020169/open/raw/master/Subscribe_report/Image/3.0.jpg
	Github不支持gif图片的渲染；点击图片会在新窗口打开图片。

### 2.7.2 插入带链接图片

[![CSDN](https://github.com/guodongxiaren/README/raw/master/img/csdn.png 'IT技术社区')](https://www.csdn.net)

	[![CSDN](https://github.com/guodongxiaren/README/raw/master/img/csdn.png 'IT技术社区')](https://www.csdn.net)
	可以理解为这是插入链接嵌套图片的应用，打开方式依然是原窗口。

### 2.8.1 图片和链接的标记引用:star:

[我的知乎][zhihulianjie]
![知乎][zhihutupian]

[zhihulianjie]:https://www.zhihu.com
[zhihutupian]:https://github.com/guodongxiaren/README/raw/master/img/zhihu.png

	[我的知乎][zhihulianjie]
	![知乎][zhihutupian]

	[zhihulianjie]:https://www.zhihu.com
	[zhihutupian]:https://github.com/guodongxiaren/README/raw/master/img/zhihu.png
	我比较喜欢用这种形式插入图片或链接，先在正文中用名称来标记，然后在文章末尾统一给出链接地址。

### 2.8.2 连接Github本仓库的URL

[我的介绍](./example/profile.md)  
![我的图片](./Image/2.2.jpg)

	[我的介绍](./example/profile.md)  
	![我的图片](./Image/2.2.jpg)
	这种方式必须保证图片和md文件地址保持相对不变，好处是简单方便，而且省去了把blob改为raw的繁琐。

## 三. 排版语法

### 3.1 缩进

&ensp; 半角的空格  
&emsp; 全角的空格

	&ensp; 半角的空格  
	&emsp; 全角的空格
	空格符可以单独使用，达到创建空行的目的，还可以用隐文本来达到显示空行的目的，隐文本的空行比空格符的空行窄。

### 3.2 居中

<div align = "center">我是红色居中</div>  
<p align = "center">我是绿色居中</p>  

	<div align = "center">我是红色居中</div>
	<p align = "center">我是绿色居中</p>
	除了居中，还可以`left`居左、`right`居右，不过Markdown默认居左。

### 3.3 文章锚点

[目录中的标题](#head1)  
<span id = "head1"> **下面的正文中的标题**</span>

	[目录中的标题](#head1)
	<span id = "head1"> **下面的正文中的标题**</span>
	点击锚点，跳转至锚点链接的位置，通常用来建立目录，或者文章内部互相跳转。

### 3.4 文字绕图

<img align="right" src="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/>

这是一个示例图片。

图片显示在 N 段文字的右边。

N 与图片高度有关。

刷屏行。

刷屏行。

到这里应该不会受影响了，本行应该延伸到了图片的正下方，所以我要足够长才能确保不同的屏幕下都看到效果。

	<img align="right" src="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/>

	这是一个示例图片。

	图片显示在 N 段文字的右边。

	N 与图片高度有关。

	刷屏行。

	刷屏行。

	到这里应该不会受影响了，本行应该延伸到了图片的正下方，所以我要足够长才能确保不同的屏幕下都看到效果。

	这里是使用 <img> 标签来贴图，然后指定 align 属性。


### 3.5 勉强配色

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) 我是红色  
![#c5f015](https://placehold.it/15/c5f015/000000?text=+) 我是绿色  
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) 我是蓝色  

	![#f03c15](https://placehold.it/15/f03c15/000000?text=+) 我是红色  
	![#c5f015](https://placehold.it/15/c5f015/000000?text=+) 我是绿色  
	![#1589F0](https://placehold.it/15/1589F0/000000?text=+) 我是蓝色  
	1.这是很勉强的配色，是使用占位符图像服务在markdown中添加一些颜色，使整体看起来不那么单调。
	2.链接中f03c15、c5f015、1589F0是颜色的代码。

### 3.6 保留区块格式

<pre>
flag_list = [
	{"医疗1":["医疗","医生"]},
	{"教育2":["教育","学校"]},
	{"政务3":["政务"]},
	{"交通4":["交通"]},
	{"安防":["安防"]}
	]# 标签，值列表
</pre> 

	<pre>
	flag_list = [
		{"医疗1":["医疗","医生"]},
		{"教育2":["教育","学校"]},
		{"政务3":["政务"]},
		{"交通4":["交通"]},
		{"安防":["安防"]}
		]# 标签，值列表
	</pre> 
	被包围在<pre>标签元素中的文本可以保留空格和换行符。

### 3.7 图片大小位置

**图片默认显示效果：**  
![](https://github.com/guodongxiaren/README/raw/master/img/zhihu.png)

**改变尺寸的效果：**  
 <img width = '150' height ='150' src ="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/>

**改变尺寸且居中的效果：**  
<div align=center><img width = '150' height ='150' src ="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/></div>

	**图片默认显示效果：**  
	![](https://github.com/guodongxiaren/README/raw/master/img/zhihu.png)

	**改变尺寸的效果：**  
	<img width = '150' height ='150' src ="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/>

	**改变尺寸且居中的效果：**  
	<div align=center><img width = '150' height ='150' src ="https://github.com/guodongxiaren/README/raw/master/img/zhihu.png"/></div>
	标准的 Markdown 图片标记 ![]() 无法指定图片的大小和位置，只能依赖默认的图片大小，默认居左。有时原图太大，想要缩小一点，或者想将图片居中，就仍需要借助 HTML 的标签来实现。图片居中可以使用 <div> 标签加 align 属性来控制，图片宽高则用 width 和 height 来控制。

## 四. One more thing

### 4.1 Github不支持的语法

1. 不支持解释行；  
2. 不支持Latex数学公式；  
3. 不支持uml流程图、时序图；  
4. 不支持注脚，加注后文章末尾显示注脚；  
5. 不支持`[TOC]`用于放在文章开头生成目录；  
6. 不支持`<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->`生成目录；  
7. 不支持插入在新窗口打开的链接，  
`<a href="http://blog.csdn.net/qq_39422642" target="_black">跳到自己博客列表</a>`  
`<a href="http://blog.csdn.net/qq_39422642" target="_blank">跳到自己博客列表</a>`  
注意：target="_blank"意为每次点击都打开新的窗口；target="_black"意为当新标签已经打开，点击第二次就不会再打开新标签了，而是刷新之前的那个标签；
8. 不支持插入音乐，  
`<div align=center><iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=30375690&auto=1&height=66"></iframe></div>`
如果不想自动播放，可以把auto改为1，不同音乐外链的方式可能不同；  
9. 不支持插入视频，
`<iframe height=498 width=510 src='http://player.youku.com/embed/XMjgzNzM0NTYxNg==' frameborder=0 'allowfullscreen'></iframe>`
这里是插入HTML的iframe框架，地址可以通过网站自带的分享功能获取。当然，Github可以通过点击伪造播放界面图片从而跳转到视频界面；  
10. 不支持文字背景色，  
`<table><tr><td bgcolor=orange>我是背景色</td></tr></table>`  
`<table><tr><td bgcolor=#FFB6C1>我是背景色</td></tr></table>`  
这是借助html的table, tr, td 等表格标签的 bgcolor 属性来实现背景色的功能。但是对rgb、hsv、cmyk颜色的显示总是错误，所以只能用16进制颜色值，或颜色英文名称。背景色代码会自动换行，无法对一行内的部分文字加底色；  
11. 不支持字体字号颜色，  
`<font face="黑体"> 我是黑体字 </font>`  
`<font face="微软雅黑"> 我是微软雅黑 </font>`  
`<font face="STCAIYUN"> 我是华文彩云 </font>`  
`<font face="黑体" color=#0099ff size=7> 你好hello word </font>`  
`<font color=#00ffff size=72> 你好hello word </font>`  
`<font color=gray size=72> 你好hello word </font>`  
这是内嵌HTML的方法；  
`<div align="center" style="color:red;font-size:30px;font-family:'黑体';">我是红色居中</div>`  
`<p align="center" style="color:#76EE00;font-size:30px; font-family:'黑体';">我是绿色居中</p>`  
这是直接使用HTML标签和内嵌CSS样式，感人的是`align="center"`还是有效的，Github支持居中语法。  

### 4.2 VScode Markdown的使用

1. `VScode`中的`Markdown Preview Enhanced`插件，功能强大，但和其他Markdown的语法兼容性一般，不过可以作为辅助工具来使用，比如：  
	* 上面Github不支持的目录功能，可以使用上面6的代码生成带链接目录，然后再上传Github；  
	* 可以导入其他Markdown文档，这个功能可以将碎片的Markdown文本进行集中汇总展示；  
	* 至于其他功能，诸如Markdown内画图、跑程序的骚操作就算了。
2. 用VScode写Markdown，如果有很多波浪线，可能是安装了`Markdownlint`插件，该插件的好处就是规范化你的Markdown语法，坏处就是逼死强迫症，鲁迅说“没有限制就没有创造力”，哈哈。建议还是开启着，可以规范化自己的语法结构。

### 4.3 Markdown辅助工具

[本文部分素材来源](https://github.com/guodongxiaren/README/blob/master/README.md)

[在线Markdown编辑器](https://markdown.lovejade.cn/?markdown.lovejade.cn&pid=main-title)  

[Markdown表情符号(中文粗分类)](https://github.com/zhouie/markdown-emoji/blob/master/README.md)  

[Markdown表情符号(英文细分类)](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)  

[颜色名称及代码](http://www.yuangongju.com/color)  


<div align = "right"> 如需转载，请注明出处 https://github.com/446020169 </div>
