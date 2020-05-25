---
layout: post
title:  "How to create Schulte Grid using Excel"
descript: "如何使用Excel制作一个建议的舒尔特方格"
categories: 
- personal
tags:
- life
---


----------------

如何用Excel做舒尔特方格


## 什么是舒尔特方格

舒尔特方格 (Schulte Grid) 是在一张方形卡片上画上 1cm × 1cm 的 25 个方格，格子内任意填写上阿拉伯数字 1 ~ 25 等共 25 个数字。训练时，要求被测者用手指按 1 ~ 25 的顺序依次指出其位置，同时诵读出声，施测者一旁记录所用时间。数完 25 个数字所用时间越短，注意力水平越高。

## 如何用Excel做舒尔特方格
1. 新建一个Excel文件；在sheet2 的A1到A25单元格中输入1-25各数;B1到B25单元格中输入随机数公式：	`=Rand()`

	![Schulte Grid](/assets/images/2013/04/29/shulte-grid_1.jpg)


2. 在sheet1的A1到E5单元格中分别用等号引用sheet2 A列中的25个单元格数据；Excel中从一个sheet引用另外一个sheet单元格的方式如下：

	`=Sheet2!A1`

	![Schulte Grid](/assets/images/2013/04/29/shulte-grid_2.jpg)


3. 在sheet2 中对数据进行排序操作，排序依据为B列，这样在sheet1 中就得到了随机排列的1-25各数。

	![Schulte Grid](/assets/images/2013/04/29/shulte-grid_3.jpg)


That's it!!

