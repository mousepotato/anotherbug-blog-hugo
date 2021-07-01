---
title: "How to import Microsoft To Do Notes to Flomo" # remove yyyy-MM-dd prefix in the filename 
date: 2021-06-30T04:53:52-07:00
draft: false
hidedate: true 
tags: ["hacks"]
categories: ["Product"]
featured_image:
description:
---


- 一直使用 Microsoft To Do 来做一些随手记的东西。不知不觉已经攒了 1200 多条. 用的最多的是基于 Tag （标签）的方式来管理。一直在找替代的东西，因为 To Do 的 Tag 不是很好用。（它的整体产品设计就不是基于这个考虑的）

- 最近看到 Flomoapp（浮墨）笔记，设计思想和我想要的很一致： 
	- 基于 Tag 
	- 可以回顾 
	- 产品设计简单简洁（定位不是一个长篇大论的笔记 app，更不是另外一款 read it later 工具，因为 read it later --> read it never)

- 当然缺点也是有的，现阶段主要是日志的导出能力和格式以及开放兼容性。已经有开源版本 [neno](https://github.com/Mran/neno) 是基于 svelte + tailwindcss 构建的 PWA 应用，数据自主可控（可以写到 Github)。

- 考虑付费使用，并且把现有的 To Do 记录的东西转过来。自己写个程序通过 API 方式倒腾一下吧。
	- 去 [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) 拿到你的 access token
	- 浮墨 提供了简单的 POST API （不过每天 100 条限制，不过他们的 rate limiter 好像不是实时的，一次性有几百条记录的话测试是可以导入的）

- 代码基于 node + axios，没有做任何优化，使用时候记得替换里面的 token 和 flomoUrl：


```javascript
const axios = require('axios')
const token = 'EwCAA======='
const config = {
  headers: { Authorization: `Bearer ${token}` }
};


const taskId = 'AQMkA======='
const baseURL = 'https://graph.microsoft.com/beta/me/todo/lists/' + taskId + '/tasks'
const flomoUrl = 'https://flomoapp.com/iwh/MTE2/======='


const getTasks = async (url) => {
  try {
    return await axios.get(
      url,
      config
    )
  } catch (error) {
    console.error(error)
  }
}

const getAllTasks = async () => {
  const ret = await getTasks(baseURL);
  ret.data.value.forEach((entry) => {
    console.log(entry.title);
    axios.post(flomoUrl, {
      'content': entry.title
    })
  });

  nextUrl = ret.data['@odata.nextLink']
  while (nextUrl != undefined) {
    res = await getTasks(nextUrl)
    res.data.value.forEach((entry) => {
      axios.post(flomoUrl, {
        'content': entry.title
      })
    });

    nextUrl = res.data['@odata.nextLink']
  }
}

getAllTasks()

```


