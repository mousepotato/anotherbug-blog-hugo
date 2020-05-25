---
layout: post
title: "How to make presentation using markdown"
description: "本文介绍如何使用Markdown编写报告。"
categories: 
- research
tags:
- markdown
- ubuntu
---


How to make presentation using markdow
如何使用markdown做报告

### 1. 安装 Markdown Presenter
[Markdown Presenter 地址](https://github.com/jsakamoto/MarkdownPresenter)

    git clone https://github.com/jsakamoto/MarkdownPresenter.git  
### 2. 安装Ubuntu下的WebServer-webfs

    sudo apt-get install webfs  

或者使用python自带的web server

    python -m SimpleHTTPServer 

### 3. 新建或者编辑.md文件 presentation.md


		This is a slide  
		Blah blah blah  
		!  
		This is another slide  
		Yada yada yada  

### 4. 将写好的文件放到`MarkdownPresenter`目录下，然后运行

    python -m SimpleHTTPServer  
或者运行

    webfsd -F -p 8888 -r ~/scripts/MarkdownPresenter/ -f Presenter.html

### 5. 注意事项
<font color='red'>The `Presenter.html` fetches the `presentation.md` from the server via Ajax, uses `Showdown.js` to transform it into HTML.</font>
所以.md文件必须命名为 `presentation.md`，然后 webserver必须打开`Presenter.html`.

That's it!!
