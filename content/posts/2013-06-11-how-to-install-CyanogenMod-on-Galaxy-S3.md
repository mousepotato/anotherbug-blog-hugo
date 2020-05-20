---
layout: post
title: "How to install CyanogenMod on Galaxy S3"
description: "CyanogenMod是Android上一个开源的固件（ROM）管理和定制软件。玩转Andorid ROM必备。本文介绍在Galaxy S3如何安装CyanogenMod"
categories: 
- Technique
tags:
- Android
---


----------------

Galaxy S3 安装CyanogenMod

CyanogenMod是Android上一个开源的固件（ROM）管理和定制软件。玩转Andorid ROM必备。下面介绍如何在Galaxy S3上安装CyanogenMod。

### 1. 下载 CyanogenMod
通过这个[链接 http://get.cm/?device=i9300](http://get.cm/?device=i9300)下载，分为三个版本：    

- nightly (最新版，小白鼠专用)  
- test  （测试版本，较稳定）  
- stable  （稳定版本）  

可以根据自己喜好选择。

### 2. 安装 CyanogenMod

将下载好的.zip文件放到S3手机上。有两种方法:

-  直接将手机连接电脑上传

-  将手机连接电脑通过adb上传

  ./adb push ~/Downloads/cm-10.1-20130610-NIGHTLY-i9300.zip /sdcard/0/cmupdater


### 3. 将S3重启进入recovery 模式进行安装

- 同时按住 `VolumnUp + Home + Power`进入恢复模式  
- 首先必须清除 `cache partition`和 `wipe data/factory reset`  

 ![rev1](/assets/images/2013/06/11/recv_1.png)
 
- 之后选择 `install zip from sdcard`  选择 `cm-10.1-20130610-NIGHTLY-i9300.zip`

 ![rev2](/assets/images/2013/06/11/recv_2.png)

- 最后选择 `Advanced-> fix permissions`，然后重启。

![rev_3](/assets/images/2013/06/11/recv_3.png)

### 4. 安装google play等软件
默认由于版权问题CyanogenMod不自带google play等软件。通过这个连接[下载 http://goo.im/gapps](http://goo.im/gapps) 你对应版本的google 软件。将其上传到S3，然后再通过重启到恢复模式选择zip安装。  


### 5. 如何打开开发者设置( {}develop options) 
- 打开`Settings -> About phone->Build number`

![dev_1](/assets/images/2013/06/11/dev_1.png)

- 狂点`build number` 几次以后系统提示 `develop settings`已经开启。

![dev_2](/assets/images/2013/06/11/dev_2.png)


That's it!!

