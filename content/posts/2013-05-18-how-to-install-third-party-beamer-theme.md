---
layout: post
title:  "How to install third party beamer theme"
description: "如何安装第三方的Beamer theme"
categories: 
- technique
tags:
- latex
---
 

如何安装第三方的Beamer theme
How to install third party beamer theme 


为了安装`Beamer` theme 文件不破坏原有的TDS (Tex Directory Structure) ，可以将需要的第三方theme安装到如下目录：

    ~/Library/texmf/tex/latex/beamer/


使用时，比如theme的文件名是 `beamerthememy1.sty`，那么在tex文件中可以如下引用：
    
    \usetheme{my1}

因为所有的beamer theme文件默认以`beamertheme` 开头。


That's it!!
