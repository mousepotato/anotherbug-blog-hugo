---
layout: post
title: "Linux 下的几个文件"
description: "Linux 下的 /dev/null, /dev/full, /dev/zero文件介绍和使用实例。"
categories: 
- technique
tags:
- linux
- ubuntu
---



Linux 下的几个文件

Unix或者类 Unix系统/dev下有几个很特殊的文件.他们就是:

## 1: /dev/null

这个/dev下放的是系统和用户的设备文件. null是个文件名. 被称为 the null device, `/dev/null` 这个童鞋脾气有点大,听不见别人任何话,所以呢任何话传到他耳朵里都被当成耳旁风了.当然更可恨的是他竟然还假惺惺的点头说听到了.当然他是很诚实地说的.  

/dev/null or the null device is a special file that discards all data written to it, but reports that the write operation succeed.   

所以呢,你心情不好的时候,或者你有个秘密憋的慌想说但是又怕周围人有个big mouth的时候来,可以和这个娃说说. 用程序员的黑话(jargon)说他是个'黑洞'(black hole)或者'位筒'(bit bucket).

![devnull](/assets/images/2013/06/13/dev_null.jpg)

知道了这个,下面几个隔行如隔山的话也就好理解了.

1. Please send complaints to `/dev/null`
2. my mail got archived in `/dev/null`

几个扩展:
1. `cat /dev/null > /var/log/db_log` (清空日志文件的内容)
2. `>/dev/null 2>&1` 的理解  

- `>` 代表重定向到哪里，比方：`echo "123" > /home/123.txt`  
- `>` 输出给这个不听话的娃, `/dev/null`  
- `2>` 表示stderr标准错误   
- `&` 表示等同于的意思，`2>&1`，表示2的输出重定向等同于1  
- `1` 表示stdout标准输出，系统默认值是1，所以`>/dev/null`等同于 `1>/dev/null`

因此，`>/dev/null 2>&1`也可以写成`1> /dev/null 2>&1`  

`1>/dev/null`：首先表示标准输出重定向到空设备文件，也就是不输出任何信息到终端，说白了就是不显示任何信息。  

`2>&1`：接着，标准错误输出重定向 到 标准输出，因为之前标准输出已经重定向到了空设备文件，所以标准错误输出也重定向到空设备文件。  

最常见的写法: `command > file 2>file` 与 `command > file 2>&1`(这个效率更高点,可以从打开文件的次数角度去分析.)


## 2. /dev/full

这个娃天生胃小,整天处于吃饱状态.送啥吃的来都不接受.那你说把这个家伙放在unix里面干嘛.This device is usually used when testing the behaviour of a program when it encounters a disk full error.测试某些程序在磁盘吃饱状态下的错误.

![devfull](/assets/images/2013/06/13/dev_full.jpg) 


## 3. /dev/zero

这哥们有很的0,MS是很有钱.他实际上产生连续不断的null的流（二进制的零流),写入他的东东会丢失不见,然后呢会给你一串的null值,这个一般不好发觉./dev/zero主要的用处是用来创建一个指定长度用于初始化的空文件，就像临时交换文件.

![devzero](/assets/images/2013/06/13/dev_zero.jpg)

 

