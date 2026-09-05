---
layout: post
title: "How to revert github source code to a specific commit"
description: "如何将github的代码回退到某一个指定的提交版本"
categories: 
- technique
tags: 
- git
robotsNoIndex: true  # 低价值/聚合内容，不进搜索索引与 sitemap
build:
  list: never   # 不出现在 /posts/、标签页、RSS；直接 URL 仍可访问
---


----------------
如何将Github的代码回退到某一个指定的提交版本  

How to revert Github source code to a specific commit


	git reset --hard "old-commit-id"
	git push -f



