---
title: "Export Flomo" # remove yyyy-MM-dd prefix in the filename 
date: 2021-09-12T00:00:52-07:00
draft: false
hidedate: true 
tags: []
categories: [""]
featured_image:
description:
---

Flomo 是一个好的应用，我曾写文章介绍[怎么从 Todo 里面把内容导入到 Flomo](https://anotherbug.com/2021/06/30/import-microsoft-todo-notes-to-flomo/)，

- 但是 Flomo 的隐私政策 (Privacy Policy)让我无法接受，我决定不再使用它。

- 另外由于 Flomo 里面的笔记和我 Obsidian 里面的日志无法一起集中起来做搜索，所以我决定也不再使用 Todo。

- 本着统一的原则，也使用 Obsidian 来保存笔记。如何把 Flomo 笔记导入 Obsidian。具体是通过 Flomo 的网上导出 HTML 功能，然后写程序解析一下，这里面做了几个事情：

- A. 设计上使用一个大文件，命名为 `Scibbles.md`，所有笔记内容都在这个文件里面。

- B. 新增一个 `#Scribble-edit-later`  标签，统一管理无标签笔记，方便后面整理。

- C. 增加了时间属性。笔记的三要素（时间、地点、内容）。地点暂时没有考虑。

- D. 解决了一些格式问题：包括标签无法显示，多行内容简化，增加盘古之白等。

- 代码基于 go，如下：

```go
package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strings"

	"github.com/PuerkitoBio/goquery"
	"github.com/vinta/pangu"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func parseFlomo() {
	content, err := ioutil.ReadFile("202109.html")
	check(err)

	doc, err := goquery.NewDocumentFromReader(strings.NewReader(string(content)))
	check(err)

	// Find the memo items
	f, err := os.Create("09.md")
	w := bufio.NewWriter(f)
	check(err)
	defer f.Close()
	doc.Find(".memos .memo").Each(func(i int, memo *goquery.Selection) {
		content := memo.Find(".content").Find("p").Text()
		space := regexp.MustCompile(`\s+`)
		content = space.ReplaceAllString(content, " ")
		ts := memo.Find(".time").Text()
		fmt.Printf("- %s  [%s]\n", content, ts)
		// 处理 Tag 1) 如果没有 Tag，增加 #Scribble-edit-later 标签 2) 如果已经有 Tag，在 # 前面加个空格，防止 Obsidian 识别不了。
		var formatedScribble string = ""
		idx := strings.Index(content, "#")
		switch idx > 0 {
		case true:
			var formatedContent string = ""
			for i, ch := range content {
				if string(ch) == "#" {
					formatedContent = content[:i] + " " + content[i:]
					break
				}
			}
			formatedScribble = fmt.Sprintf("- %s  [%s]\n", formatedContent, ts)
		case false:
			formatedScribble = fmt.Sprintf("- %s  #Scribble-edit-later  [%s]\n", content, ts)
		}
		// 恩，在增加 盘古之白
		w.WriteString(pangu.SpacingText(formatedScribble))
		w.Flush()
	})

}

func main() {
	parseFlomo()
}

```