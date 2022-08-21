'''
 *@author:wr
 *@GitHub:https://github.com/wr0x00/Lizard
 *@date:2022.8.2
 *@description: CMS扫描功能
'''
#!/usr/bin/env python3
# coding:utf-8
import requests
import zlib
import json

'''设置语言'''
if not __name__ == '__main__':
    try:
        x=open("first_sgin.txt",'r+')
        language=x.readline()
        if language=='cn'or language=='CN': #中文
            from .strings import String_CN as Str
        if language=='en'or language=='EN': #英文
            from .strings import String_EN as Str
        x.close()
    except Exception:
        print("ERROR")
        from .strings import String_EN as Str

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
    print(Str.REMAINING_TIMES+request.headers["X-RateLimit-Remaining"])
    print(Str.RESULTS)
    print(request.json())