---
layout: post
title: "Linux 下的查看系统内存信息"
description: "Linux下查看系统内存的方法"
categories: 
- technique
tags: 
- linux
- ubuntu
---


Linux查看系统内存信息可以有如下方法：

- `free`  
- `free -m`  
- `cat /proc/meminfo`

如果要查询详细到RAM规格，DDR2，DDR3可以使用：

- `sudo lshw`

![meminfo](/assets/images/2013/06/14/meminfo.png)
