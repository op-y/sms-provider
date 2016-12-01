#! /usr/bin/env python
#-*- coding:utf-8 -*-
#
# Author: ye.zhiqin@outlook.com
# Date  : 2016/11/30

import time
import requests
from urllib import quote

class SmsSender:
    def __init__(self, sms):
        data=sms.split('&')
        tos=''
        content=''
        for item in data:
            if 'tos' in item:
                value=item.split('tos=')[1]
                tos=value.replace(',', ';')
            elif 'content' in item:
                value=item.split('content=')[1]
                content=value
            else:
                continue
        self.sms_api_url="http://127.0.0.0:4000/sender/sms"
        self.sms_api_user="username"
        self.sms_api_password="password"
        self.destmobile=tos
        self.message_sign="signature"
        self.message_text=content+self.message_sign
        self.data={'account':self.sms_api_user,'password':self.sms_api_password,'destmobile':self.destmobile,'msgText':self.message_text}

    def send(self):
        response = requests.post(self.sms_api_url, data=self.data)
        code = response.status_code
        text = response.text
	return code


# __main__
if __name__=='__main__':
    print 'Test in main'
    sms="tos=13838389438,13900000000&content=TEST"
    sender = SmsSender(sms)
    sender.send()
