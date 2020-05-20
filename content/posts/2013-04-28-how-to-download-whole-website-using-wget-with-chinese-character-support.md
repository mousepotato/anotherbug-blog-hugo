---
layout: post
title:  How to download a whole website using wget with chinese character support 
description: "如何使用wget下载整个网站同时支持中文命名"
categories: 
- Technique
tags:
- Linux
- Ubuntu
---


如何使用wget下载整个网站同时支持中文命名

## wget 下载整个网站
使用命令：

    wget -r -p -E -k -nH -np --cut-dirs=1 -P /path/to/save/  Website URL

## 支持中文

    vi ~/.wgetrc

添加如下内容：

    --restrict-file-names=nocontrol
    --trust-server-names=on
    --content-disposition=on

That's it!!

