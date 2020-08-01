---
title: "Samsung S6 Edge Install Lineage OS 17.1"
date: 2020-07-31T00:23:26-07:00
draft: false
categories:
- technique
tags:
- android
- random-thoughts
---

- 又开始折腾 Android ROM 了。上次是 7 年前在 [Galaxy S3 上基于 CyanogenMod](https://anotherbug.com/2013/06/11/how-to-install-cyanogenmod-on-galaxy-s3/) 进行的。这次主要是 Samsung S6 Edge 自带的 Android 7.0 版本太老了。

![s6-os](/assets/images/2020/07/s6-original-os.jpg)

- 基本信息 Samsung S6 Edge 的 Model 是 `SM-G925F`开头，想刷版本 `LineageOS 17.1` 基于 Android 10。

### 步骤

0. 确保你的 Windows 电脑已经有了 Samsung S6 Edge 的 USB 驱动，，下载： `SAMSUNG_USB_Driver_for_Mobile_Phones_v1.5.25.0-retail.exe`。这里会影响后面刷机。
   
1. root 你的机器，基于 `Odin v3.09.zip` 软件，下载对应的压缩包 `CF-Auto-Root-zerolte-zeroltexx-smg925f.zip`，注意型号是含有 `zeroltexx-smg925f`。

![odin3](/assets/images/2020/07/odin3.png)

2. 安装大名鼎鼎的 `TWRP (Team Win Recovery Project)`。安装版本 `twrp-3.3.1-0-zerolte.img.tar`，注意我这里踩了一个坑，最开始安装了一个老的版本 `twrp-3.1.0-0-zerolte.img.tar` 后面刷 ROM 的时候报错。

![twrp](/assets/images/2020/07/twrp.jpg)

3. 下载 Samsung S6 Edge 对应的 ROM 和 GApps，分别是 `lineage-17.1-20200504-UNOFFICIAL-zeroltexx.zip`，`open_gapps-arm64-10.0-micro-20200801.zip`。注意这里花了不少时间确定版本。如果你的机器和我的不一样，务必在这里先查清楚对应的软件。切记。

![opengapps](/assets/images/2020/07/opengapps.jpg)

4. boot 进入 TWRP 界面，然后 Install Image，可以同时把 Lineage 17.1 和 open gapps 选中。然后开心刷机。最后 Reboot System。这里不要勾选 更新 TWRP 和另外一个选项。切记，否则 ROM 启动不起来。

5. 最后就是基于 Android 10 的清爽的 LineageOS 17.1 啦。注意这里有一个冲突，最新的 `LineageOS 17.1` 的 Launcher `Trebuchet` 与 Gapps自带的 `Pixel Launcher`有冲突，导致 trebuchet keeps stopping。暂时切换到默认使用 `Pixel Launcher` 解决。

![lineage17](/assets/images/2020/07/lineage17.jpg)

![Linage_Pixel_Launcher](/assets/images/2020/07/Linage_Pixel_Launcher.jpg)


### 后记

- 这里仅仅记录一个流程，省略了很对细节，比如如何使用 Odin 来 root 机器，如何进入 TWRP Recovery Mode 等等。你既然都想刷机了，希望这是你的一个必备（可以快速自学）能力，就不赘述了。
- 新手的感觉会是步骤太多，软件（版本）太多，每一步的目的以及每一个操作的作用需要花时间了解清楚。我也是差不多 7 年前折腾了一会。今天又重新折腾了一下。花了 3-4 个小时，原因是上面说的踩了一些坑，以及学习和查找一些资料花了些时间。
- 如何查资料是一个重要的能力，尤其是如何在中文，英文环境的网站、教程、论坛帖子以及热心网友们的**只言片语中快速定位并且找到重要关键细节然后解决自己遇到的实际问题**的能力。这一点的训练相对于简单的折腾更有意义。有空我在分享我两次修车的经历。如何在不提前拆开车，先花几个小时在网上查找和定位根因，最后实际操作只花 10 分钟修好的例子。
- 再多说一句吧，关于『越狱、折腾与创造』。不管是 Android 也好，iOS 也好，网络上存在大批的资料和组织，美其名曰 「HACK」。大部分人应该只是停留在折腾阶段，使用别人的越狱工具来回折腾，浪费时间和精力。我在学生时期也干过。也建议学生们多做做，可以提高动手能力。但是你要尽早思考和明白 『折腾与创造』 的区别。有空我再写写。
