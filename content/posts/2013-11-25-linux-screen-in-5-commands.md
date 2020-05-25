---
layout: post
title: Screen 使用之无废话5行命令
description: "Linux screen in 5 command lines"
categories: 
- technique
tags:
- ubuntu
- linux
---



 Linux screen in 5 command lines

----------------

## 1. 建立一个 screen shell 窗口

	screen

## 2. 退出刚建立的窗口

	ctrl+ a d

## 3. 查看已有 screen 窗口
	
	screen -ls

## 4. 重新进入已有 screen 窗口
	
	screen -r sessionid

`sessionid` can be found by looking `screen -ls`

## 5. 退出已有 screen 窗口
	
	exit

## 6. 退出全部 detached sessions

	screen -ls | grep Detached | cut -d. -f1 | awk '{print $1}' | xargs kill
	
	
That's it!!!

