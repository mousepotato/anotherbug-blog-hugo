---
title: "Test post using Hugo"
date: 2020-05-18T11:24:40-07:00
draft: false
categories:
- technique
tags:
- test
---

- This is a test post generated using Hugo.

- 打算把博客从 Hexo 迁移到 Hugo。原因是因为看到 Hugo 的 Theme 比较好看。又折腾了一下，虽然不长写博客，但是还是保留想写博客的时候有个好看的博客可以写的权利。

- 记录一点：我的每个博文格式都是 「yyyy-MM-dd-xxx.md」 的形式，Hugo 的 archetypes 模板里面需要调整一些 title，去掉日期。具体做法： `title: "{{ substr (replace .TranslationBaseName "-" " ") 11 | title }}"`

- 另外新版博客新增了 [好物](https://anotherbug.com/tools/)，记录一下自己败家的经历吧。
