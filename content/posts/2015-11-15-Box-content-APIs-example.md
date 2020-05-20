---
layout: post
title: "Box content APIs example"
description: "使用Box API的例子"
categories: 
- Technique
tags:
- Programming
---



今天实现了新建一个box app并通过Box API读取用户box里面文件的程序。记录如下。

## 准备
1. 使用nodejs环境搭建回调服务器
2. 好像没用了。。。。（box账户和developer页面）

## 实现

box 的api实现了oAuth2标准。所以不难使用。参考了网上已有的nodejs实现。
注意box需要的回调地址是加密的https请求，不支持http。所以需要首先实现一个nodejs的https服务器。网上也有。。。

代码


``` Java
const crypto = require('crypto'), fs = require("fs"),
http = require("http");
var privateKey = fs.readFileSync('privatekey.pem').toString(); var certificate = fs.readFileSync('certificate.pem').toString();
var credentials = crypto.createCredentials({key: privateKey, cert: certificate});
var handler = function (req, res) { res.writeHead(200, {'Content-Type': 'text/plain'}); res.end('Hello World\n');
};
var server = http.createServer(); server.setSecure(credentials); server.addListener("request", handler); server.listen(8000);
```

其中生成privatekey.pem 和 certificate.pem 的方法是:

	openssl genrsa -out privatekey.pem 1024
 
	openssl req -new -key privatekey.pem -out certrequest.csr
 
	openssl x509 -req -in certrequest.csr -signkey privatekey.pem -out certificate.pem
 


然后就是找到最新版本的 API document去读一下: https://developers.box.com/docs-overview/

然后去box developer 里面注册一个app，注意选使用content API。然后获取`client_id`, `client_secret`, 和 `redirect_uri`
这里的 `redirect_uri`我填写的是 `https://localhost:3443/boxdemo/redirect` (对照后面的代码)


参考网上实现的代码链接 [github: box-api-ex](https://github.com/mousepotato/box-api-ex.git)















