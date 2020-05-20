---
layout: post
title:  "How to use wget to donwload the whole web folder"
description: "如何使用wget下载整个网站的文件夹"
categories: 
- Technique
tags:
- Ubuntu
- Linux
---


如何使用wget下载整个网站的文件夹
How to use wget to donwload the whole web folder

使用如下命令：
    
    wget -r -p -E -k -nH -np --cut-dirs=1 -P ~/Downloads/  http://99.198.110.38/Chinese/MP3s/13%E6%97%A7%E7%BA%A6%E8%AE%B2%E9%81%93/


That's it!!
