---
layout: post
title: "Bash pattern match"
description: "Bash pattern match"
categories: 
- Technique
tags:
- Linux
- Ubuntu
---


## 1. 起因：Shell 获取文件名和后缀名


``` shell
[_posts] ==>> file="A-Tale-Of-Two-Cities.pdf"
[_posts] ==>> echo "${file%.*}"
A-Tale-Of-Two-Cities
[_posts] ==>> echo "${file##*.}"
pdf
```

## 2. 基于 Pattern Matching 的子串替换

`${str/$old/$new}`  替换第一个。
`${str//$old/$new}` 替换所有。

注意：不能使用正则表达式，只能使用 ?* 的Shell扩展。只能用shell通配符如 `*?  [list] [!list] [a-z]`。

`${str/#$old/$new}` 替换开头。如果str以old串开头，则替换。
`${str/%$old/$new}` 替换结尾。如果str以old串结尾，则替换。

**[note]** `#`和`%`一个是替换开头，一个是替换结尾。可以这么记忆。键盘上`#`在`%`前面。所以`#`是替换开头，`%`是替换结尾。

``` shell
[_posts] ==>> str="Hello World"
[_posts] ==>> echo ${str/o/O}
HellO World
[_posts] ==>> echo ${str//o/O}
HellO WOrld

[_posts] ==>> str="Hello World"
[_posts] ==>> echo ${str/#He/he}
Hello World
[_posts] ==>> echo ${str/#o/he}
Hello World

[_posts] ==>> str="Hello World"
[_posts] ==>> echo ${str/%He/he}
Hello World
[_posts] ==>> echo ${str/%ld/lD}
Hello WorlD
```

一个例子: 将环境变量PATH的各个目录分开，每行显示一个。就是讲`:`转换成`\n`就可以实现。

``` shell
[_posts] ==>> echo -e ${PATH//:/"\n"}
/Library/Frameworks/Python.framework/Versions/3.5/bin
/Library/Frameworks/Python.framework/Versions/2.7/bin
/usr/local/bin
/usr/sbin
...
```

## 3. 基于 Pattern Matching 的子串删除
子串删除是一种特殊的替换

`${str/$sub}`     将str中第一个sub子串删除
`${str//$sub}`    将str中所有sub子串删除
`${str#$prefix}`  去头，从开头去除最短匹配前缀
`${str##$prefix}` 去头，从开头去除最长匹配前缀
`${str%$suffix}`  去尾，从结尾去除最短匹配后缀
`${str%%$suffix}` 去尾，从结尾去除最长匹配后缀

``` shell
[_posts] ==>> str="Hello World"
[_posts] ==>> echo ${str#He}
llo World
[_posts] ==>> echo ${str#He*o}
World
[_posts] ==>> echo ${str##He*o}
rld

[_posts] ==>> prefix="*o"
[_posts] ==>> echo ${str#$prefix}
World
[_posts] ==>> echo ${str##$prefix}
rld

[_posts] ==>> suffix="o*"
[_posts] ==>> echo ${str%$suffix}
Hello W
[_posts] ==>> echo ${str%%$suffix}
Hell
```
一个例子：获取文件扩展名,如最前面的介绍。

``` shell
[_posts] ==>> filename="A-cat.jpg"
[_posts] ==>> echo ${filename##*.}
jpg
```


