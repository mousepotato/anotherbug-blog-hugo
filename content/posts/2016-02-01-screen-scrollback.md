---
layout: post
title: "Screen scrollback"
description: "screen scrollback setting"
categories: 
- technique
tags:
- linux
- ubuntu
robotsNoIndex: true  # 低价值/聚合内容，不进搜索索引与 sitemap
build:
  list: never   # 不出现在 /posts/、标签页、RSS；直接 URL 仍可访问
---


## 设置screen支持长scrollback

1. In `~/.screenrc` add or set `defscrollback 50000` use 50000 or any number you want

2. In your screen, checking by `ctrl + a + i`, it will show your current scrollback settings

3. To enter scrollback/copy mode, using `ctrl + a + [`

4. Use `ctrl + u`, `ctrl + d`, `ctrl + f` and `ctrl + b` for happy scolling

Et voila!!

