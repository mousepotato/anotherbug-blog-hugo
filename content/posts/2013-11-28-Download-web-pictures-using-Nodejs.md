---
layout: post
title: 使用 Node JS 批量下载网站的图片
description: "介绍如何使用Node Js 批量下载网站上的图片，使用的技术包括Node Js插件的使用，编码转换，HTML DOM处理，Javascript 闭包等等。"
categories: 
- technique
tags:
- nodejs
- programming
---


## 1. 起因

最近看到 [网站 fhl.net](http://photo.fhl.net/main/holy/index.html) 上有一系列《圣地旅游》的照片，个人很喜欢，想把它下载下来保存。问题是该网站上有67页，每页有35张照片，也就是总共有2345张照片，同时我还想讲网页上照片的介绍作为照片的名称保存，这样方便以后查看。所以，问题是如何做呢？

## 2. 所需 tools
鉴于最近爱上了 [Node.js](http://nodejs.org/) 这一神奇的工具。打算用它试试。

2.1 用到的插件有

- request `npm install request`  处理http request
- cheerio `npm install cheerio`  Html DOM 处理
- iconv-lite `npm install iconv-lite`  处理中文字符转码
- wget `npm install wget`  图片下载工具


## 3. 代码 Code 


```Javascript
var request = require("request");
var cheerio = require("cheerio");
var iconv = require('iconv-lite');
var wget = require('wget');

// loop through all 67 html pages
for(var i = 1; i < 67; i++){

  (function(i){request({
      uri: "http://photo.fhl.net/main/holy/"+i+"index.html",
    encoding:null
  }, function(error, response, body) {
    var str = iconv.decode(new Buffer(body), "big5");
      var $ = cheerio.load(str);
     
      $('table a').each(function() {
          var link = $(this);
          var text = link.text();
          var href = link.attr("href");
          // href = "holy2351.html"
          // http://photo.fhl.net/img/holy/2351.jpg
          // console.log(text + "http://photo.fhl.net/img/holy/" + href.substr(4,4) + ".jpg");

      var src = "http://photo.fhl.net/img/holy/" + href.substr(4,4) + ".jpg";
      // var output ="/Users/shuangjiang/playpen/holypic/"+text.replace(/\s+/g,"");
      var output ="/Users/shuangjiang/playpen/holypic/"+text+".jpg";
      var download = wget.download(src,output);
      download.on('end', function(output) {
        console.log("download all the pics");
      });
    });
  });})(i); // closure
}
```

That's it!!


