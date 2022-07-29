#!/usr/bin/env python3
# coding:utf-8
import requests
import zlib
import json

proxy=None
def set_agent(p):#设置代理
    global proxy
    proxy=p

def whatweb(url):
    if url.find('://') == -1:
        url='http://'+url
    response = requests.get(url,verify=False,proxies=proxy)
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data,params=proxy)#脚本小子建的站，接口不稳定

def cms(url):
    request = whatweb(url)
    print(u"今日剩余次数"+request.headers["X-RateLimit-Remaining"])
    print(u"识别结果:")
    print(request.json())