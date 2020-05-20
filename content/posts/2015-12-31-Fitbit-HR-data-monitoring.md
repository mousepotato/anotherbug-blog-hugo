---
layout: post
title: "Fitbit HR heart rate data monitoring"
description: "Fitbit HR heart rate data monitoring"
categories: 
- Personal
tags:
- Life
- Hacks
- Nodejs
---


## 1. Fitbit HR
Fitbit HR 提供了全天候的心率 (heart rate) 数据。HR数据可以反应很多的指标（健康，活动量），甚至是什么时候洗澡或者...。除了HR数据，还有HRV (Heart Rate Variablity)也很常用。这部分好像Fitbit HR还不支持。需要精确度更好的设备。比如 Garmin HR Run.

一般通过fitbit app不能够得到每天的HR数据。估计需要付费成为会员才可以看到这部分。好在fitbit提供了API，可以自己获取。


## 2. 获取 Fitbit HR 数据

首先去 [Fitbit Dev](https://dev.fitbit.com/apps) 注册一个app,注意如果你想获取到精确到秒级别心率数据，选择app的类型是 personal, fitbit对这个好像有限制。如前面所说，HR数据能反应太多。。。

注册以后拿到`ClientID`, `Client_Secret`然后就是标准的`OAuth 2` 的应用验证。推荐 node js开源的包 [fitbit-oauth2](https://github.com/peebles/fitbit-oauth2)

验证通过获取每天精确到秒级别的心率数据的uri是

    https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec.json



## 3. 显示 Fitbit HR 数据

获得了数据以后，怎么用呢？最简单的办法是plot，可以直观的看。这里推荐 [Plotly](https://plot.ly/) 应用。免费使用，不过作出的图需要公开。注册，获取一个`API_KEY`。
然后在使用 node js 的 plotly库 [plotly-nodej](https://github.com/plotly/plotly-nodejs)。 Then you are good to go...

简单的画图 nodejs 实现:

``` Javascript
app.get('/plot/:bday', function(req, res, next) {
  bday = req.params.bday;
  fs.readFile('./bpm/bpm-' + bday + '.json', 'utf8', function(err, data) {
    if (err) throw err; // we'll not consider error handling for now
    var profile = JSON.parse(data);
    res.send('<pre>' + JSON.stringify(profile[
      'activities-heart-intraday'], null, 2) + '</pre>');

    // plot here
    var x = [];
    var y = [];
    var plotly = require('plotly')('mouse_potato', 'rmoeisc3m8');
    var graphOptions = {
      fileopt: "overwrite",
      filename: "bpm-" + bday
    };

    var intradaydata = profile['activities-heart-intraday'];
    var dataset = intradaydata['dataset'];
    //console.log(dataset.length);
    for (var i = 0; i < dataset.length; i++) {
      x.push(dataset[i]['time']);
      y.push(dataset[i]['value']);
    }

    var data = [x, y];
    plotly.plot(data, graphOptions, function(err, msg) {
      console.log(msg);
     });
  });
});     
```

怎么样，想看看我圣诞节那天的心率么？-:) [bpm-2015-12-24](https://plot.ly/~mouse_potato/24)



## 4. One more thing...

怎么偷懒，实现了一个每天夜里2:30AM 把前天的心率数据读取出来，作好图然后发一封链接邮件到我邮箱。
使用 [nodemailer](https://github.com/nodemailer/nodemailer) 吧。记得如果使用gmail，需要打开 `gmail allow less secure apps`
[Allow less secure apps](https://support.google.com/accounts/answer/6010255?hl=en)

代码是这样，

``` Javascript
      var nodemailer = require('nodemailer');

      // create reusable transporter object using the default SMTP transport
      // Put your email username and password here
      var transporter = nodemailer.createTransport(
        'smtps://MYEMAILUSERNAME%40gmail.com:MYPASSWORD@smtp.gmail.com'
      );

      // setup e-mail data with unicode symbols
      var mailOptions = {
        from: "HR Monitoring <xxx@gmail.com>",
        to: "myusername@gmail.com",
        subject: "Your yesterday's HR is ready",
        text: msg.url,
        html: "Please click <a href=" + msg.url + ">plot</a> for the data."
      };

      // send mail with defined transport object
      transporter.sendMail(mailOptions, function(error, info) {
        if (error) {
          return console.log(error);
        }
        console.log('Message sent: ' + info.response);
      });
```


然后建立一个 cron job, 去执行一个 shell 脚本

``` Shell
#!/bin/bash
TODAY=`date +%F`
YESTERDAY=$(date --date yesterday "+%F")

ACCESS_TOKEN=$(cat fb-token.json |jq ".access_token")
echo $ACCESS_TOKEN

sleep 3
curl -H "Authorization: Bearer $ACCESS_TOKEN" http://yourdomain.com/getbpm/$YESTERDAY
sleep 7
curl --ipv4  "http://yourdomain/plot/$YESTERDAY" -v
```


That's it!!!

