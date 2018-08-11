#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
def feedback_mail(body):
    # 第三方 SMTP 服务
    mail_host = "smtp.gmail.com" # 设置服务器
    mail_user = "shaubou@gmail.com"  # 用户名
    mail_pass = "TwTw091754"  # 口令
    sender = 'shaubou@gmail.com'
    receivers = ['shaubou@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = Header("禾韻藥局FB", 'utf-8')
    message['To'] = Header("JasonPan", 'utf-8')
    subject = '禾韻藥局使用者意見回饋'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP(mail_host,587)
        #smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("郵件發送成功")
    except smtplib.SMTPException:
        print("Error: 無法發送郵件")
    return


