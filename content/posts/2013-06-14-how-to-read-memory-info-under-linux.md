---
layout: post
title: "Linux 下的查看系统内存信息"
description: "Linux下查看系统内存的方法"
categories: 
- technique
tags: 
- linux
- ubuntu
robotsNoIndex: true  # 低价值/聚合内容，不进搜索索引与 sitemap
build:
  list: never   # 不出现在 /posts/、标签页、RSS；直接 URL 仍可访问
---


Linux查看系统内存信息可以有如下方法：

- `free`  
- `free -m`  
- `cat /proc/meminfo`

如果要查询详细到RAM规格，DDR2，DDR3可以使用：

- `sudo lshw`

![meminfo](/assets/images/2013/06/14/meminfo.png)
