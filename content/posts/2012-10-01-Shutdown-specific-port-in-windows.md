---
layout: post
title: "Windows 下如何关闭特定端口"
description: 
categories: 
- Technique
tags:
- Windows
---


- `netstat -aon|findstr "9050"`

    TCP: 127.0.0.1:9050 0.0.0.0 LISTENING 2016

    tasklist|findstr "2016"

-  `tor.exe 2016 Console 0 16,064`


- `ctrl+alt+delete` 打开任务管理器，找到tor.exe右键end process。


That's it!!
