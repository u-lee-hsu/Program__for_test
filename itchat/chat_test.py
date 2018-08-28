#coding=utf8
import requests
import itchat
import time
import random

KEY = '96d6f52c0d3b464ebad1db7ac2a15de9'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
 
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    print(defaultReply)
    reply = get_response(msg['Text'])
    ra=random.randint(1,6)
    time.sleep(ra)
    return reply or defaultReply
 
itchat.auto_login(hotReload=False)
itchat.run()

