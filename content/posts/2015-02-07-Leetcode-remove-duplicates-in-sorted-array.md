---
layout: post
title: "Leetcode remove duplicates from sorted array"
description: "Leetcode 刷题有感 Leetcode remove duplicates from sorted array"
categories: 
- Technique
tags:
- Algorithm
- Leetcode
---



Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example, Given input array A = [1,1,2], Your function should return length = 2, and A is now [1,2]



写了几次，每一次都有不同的感受。

版本一：

```Java
public int removeDuplicates(int [] A){
	   if (A == null || A.length == 0) {
		return 0;
	   }		      
        int i = 0, j = 0;
        while (j < A.length) {
           if (A[i] != A[j++]) {
               A[++i] = A[j];
           }
       }
       return i + 1;
}

```

这个版本有错误，原因是数组越界，虽然while循环判断数字长度，但是在if判断里面使用了j++，这个其实没事，但是后面的A[++i] = A[j]，要访问A[j]，此时可能导导致IndexOutOfBound。无经验造成的。


版本二：

```Java
public int removeDuplicates(int [] A){
 		if (A == null || A.length == 0) {
			return 0;
		}
		int size = 0;
		int i = 0;
		while (i < A.length){
			if (A[size] != A[i]) {
				A[++size] = A[i];
			}
			i++;
		}
	
	    return size + 1;		
}

```
版本二通过测试，也使用了有意义的变量size作为输出。但是这个代码还是反应不出作者的思想和对题目的理解。

版本三：

```Java
	public int removeDuplicates(int[] A) {
		if (A == null || A.length == 0) {
			return 0;
		}

		int walker = 0;
		int runner = 0;
		while (runner < A.length) {
			if (A[runner] != A[walker]) {
				A[++walker] = A[runner];
			}
			runner++;
		}
		return walker + 1;
	}
```
版本三，变量使用了runner和walker，一看就明白是写代码者理解题目的快慢指针的思想。堪称完美。

此乃刷题者三种境界，共勉！








