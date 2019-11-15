# Wechat_Bot
微信自动回复机器人 
## Dependencies
[Mac or Ubuntu or Windows]

Python 3.7 

wxpy

smtplib

email


## Description

本微信机器人，实现了自动回复，特别关心功能。

其中特别关心是将特别关心的人的消息转接至邮箱。所以初次使用前需要设置 setting.py

自动回复功能的实现主要是用来wxpy库，该库是对微信网页版的封装，所以登陆时是需要扫码的。

需要注意的是 文件传输助手 负责查看输入的指令情况；给自己发相应的消息，相当于输入指令；初次登陆会文件传输助手会显示现支持的所有指令

同时初次使用及更新数据库后的60s内无法自动回复，因为有自动回复时间的间隔，时间间隔根据自身情况可在手机微信上设置

## How to run

第一步 编辑 setting.py 这设置自己邮箱号、密码、STMP

第二步 终端输入 python3 autochat.py , 会出现一个二维码，扫码即可

后台挂起终端输入【mac / linux】: nohup python3 -u chabot.py>bot.log& , 然后cat bot.log ,关闭进程请kill

第三步 查看微信的 文件传输助手 会获得使用的help，所有使用的命令请通过给自己发消息使用【是发给自己，不是文件助手】

## About Me

Call me Amber , A University Student, Boy

【小白，非大佬！！！】

Love Coding

Love DeepLearning CV

Love Sharing

欢迎同各位大佬交流

wxchat : amberzdh