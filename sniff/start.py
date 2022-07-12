
import argparse
from logging import exception
import re
import string
from tkinter import E
import modules.sniff
import argparse

def start_portscan(ip):
    while not modules.sniff.isIP(ip):
        ip = input('地址不正确或未在线，请输入正确的IP地址:\n')
    modules.sniff.ScanPort(ip).start()
def _2018_9995():
    import modules.C2018_9995_EXP as a
    url=input("地址: ")
    door=input("p：")
    a.exp(url,door)
    
def connect_mysql(host,user):
    import mysql.connector
    try:
        mydb = mysql.connector.connect(
          host=host,
          user=user,
          passwd=input('Enter password:')
        )
        mycursor = mydb.cursor()
    except:
        print("连接错误")
        pass
    while True:
        try:
            str=input(host+"'s MySql>")
            if str=='exit':
                print("Bey")
                break
            mycursor.execute(str)
            for x in mycursor:
              print(list(x))
        except mysql.connector.errors.ProgrammingError:
            print("命令错误")


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("-mh","--mysqlhost",type=str, help="mysql host")
        parser.add_argument("-mu", "--mysqluser",type=str, help="mysql username")
        parser.add_argument("-sp", "--scanportIP",type=str, help="scan ports IP address")
        parser.add_argument("-whois", "--whois",type=str, help="IP whois info")
        parser.add_argument("-shodan", "--shodan",type=str, help="shodan search")
        parser.add_argument("-sw", "--scanwebdirURL",type=str, help="web address which be scaned dictionary")
        parser.add_argument("-d", "--directory",type=str, help="dictionary which be need",default="modules/dict.txt")
        parser.add_argument("-t", "--thread",type=int, help="threads which be need",default=60)
        #EXP
        parser.add_argument("-agent", "--agent",action='store_true', help="start agent")
        parser.add_argument("-rp", "--rport",type=int, help="target port,Add according to the other option instructions")
        parser.add_argument("-rh", "--rhost",type=str, help="target host,Add according to the other option instructions")
        parser.add_argument("-lp", "--lport",type=int, help="local port,Add according to the other option instructions")
        parser.add_argument("-lh", "--lhost",type=str, help="local host,Add according to the other option instructions")
        parser.add_argument("-url", "--url",type=str, help="target web's url,Add according to the other option instructions")
        
        parser.add_argument("-SMB", "--SMBboom",type=str, help="SMBboom exploit number,could use with -agent")
        parser.add_argument("-ddos", "--ddos",action='store_true', help="ddos exploit,don't need other option")
        parser.add_argument("-cve-2018-9995", "--cve2018_9995",action='store_true', help="cve-2018-9995 exploit,use with -rp and -rh")
        parser.add_argument("-cve-2022-21907", "--cve2022_21907",action='store_true', help="cve-cve-2022_21907 exploit,use with -rh or -url")
        
        args = parser.parse_args()
        
        if args.mysqlhost and args.mysqluser:
            connect_mysql(args.mysqlhost,args.mysqluser)
        if args.scanportIP:
            start_portscan(args.scanportIP)
        if args.whois:
            modules.sniff.whois_sniff(args.whois)
        if args.scanwebdirURL:
            modules.sniff.start_dirscan(args.scanwebdirURL,args.directory,args.thread)
        if args.shodan:
            modules.sniff.shodan_search(args.shodan)
        
        #EXP
        if args.SMBboom:
            if args.agent:
                import os
                os.system("python modules/SMSBoom_master/smsboom.py -e -p "+args.SMBboom)
            else:
                import os
                os.system("python modules/SMSBoom_master/smsboom.py -p "+args.SMBboom)

        if args.ddos==True:
            import os
            os.system("python2 modules/ddos.py")
        if args.cve2018_9995==True and args.rport and args.rhost:
            import modules.C2018_9995_EXP as e
            e.exp(args.rhost,args.rport)
        if args.cve2022_21907==True and (args.url or args.rhost):
            if args.url:
                target=args.url
            else:
                target=args.rhost
            import modules.C2022_21907_EXP as e
            e.exp(target)

#end