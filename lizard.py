'''
 BLUE        = '\033[94m'
 GREEN       = '\033[32m'
 RED         = '\033[0;31m'
 DEFAULT     = '\033[0m'
 ORANGE      = '\033[33m'
 WHITE       = '\033[97m'
 BOLD        = '\033[1m'
 BR_COLOUR   = '\033[1;37;40m'
 '''
import argparse
import modules.sniff
import argparse

def connect_mysql(host,user,pwd):
    import mysql.connector
    try:
        mydb = mysql.connector.connect(
          host=host,
          user=user,
          passwd=pwd
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
        
        parser.add_argument("-m","--mysql",type=str,nargs="+", help="mysql host and mysql user,port")
        parser.add_argument("-sp", "--scanportIP",type=str, help="scan ports IP address")
        parser.add_argument("-whois", "--whois",type=str, help="IP whois info")
        parser.add_argument("-shodan", "--shodan",type=str, help="shodan search")
        parser.add_argument("-sw", "--scanwebdirURL",type=str, help="web address which be scaned dictionary")
        parser.add_argument("-c", "--cms",type=str, help="cms url")
        parser.add_argument("-d", "--directory",type=str, help="dictionary which be need")
        parser.add_argument("-t", "--thread",type=int, help="threads which be need",default=60)
        parser.add_argument("-poc", "--poc",type=str, help="poc ip")
        #EXP                
        parser.add_argument("-a", "--agent",type=str, help="agent,Add according to the other option instructions")
        parser.add_argument("-rp", "--rport",type=int, help="target port,Add according to the other option instructions")
        parser.add_argument("-rh", "--rhost",type=str, help="target host,Add according to the other option instructions")
        parser.add_argument("-lp", "--lport",type=int, help="local port,Add according to the other option instructions")
        parser.add_argument("-lh", "--lhost",type=str, help="local host,Add according to the other option instructions")
        parser.add_argument("-u", "--user",type=str, help="target username,Add according to the other option instructions")
        parser.add_argument("-url", "--url",type=str, help="target web's url,Add according to the other option instructions")
        
        parser.add_argument("-ssh", "--ssh",action='store_true',help="ssh force~,use with -rh,-d('modules\pwddic\password\top1000.txt'),-u(root),-rp(22)") 
        parser.add_argument("-dos", "--dos",action='store_true',help="dos attack")        
        parser.add_argument("-ws", "--webshell",type=str, nargs="+",help="webshell url and passwd")      
        parser.add_argument("-ddos", "--ddos",action='store_true', help="ddos exploit,don't need other option,need python2 environment")
        parser.add_argument("-exp", "--exp",type=str, nargs="+", help="exploit Vulnerability number,such as'cve2018-9995'")
        parser.add_argument("-expip", "--expip",type=str, help="exploit Vulnerability target ip")
    
        args = parser.parse_args()
        if args.agent:
            import socks,modules.dosattack
            agent={'http':args.agent}   
            http,socks5_proxy_host,socks5_proxy_port = args.agent.split(":")
            socks5_proxy_host=http+":"+socks5_proxy_host
            # 设置代理       
            socks.set_default_proxy(socks.SOCKS5,socks5_proxy_host,socks5_proxy_port)
            modules.sniff.set_agent(agent,socks)
            modules.dosattack.set_agent(agent,socks)
        else:
            agent=None
        
        
        if args.mysql:
            t=0
            for i in args.mysql:
                if not i:
                    break
                if t==0:
                    host=i
                if t==1:
                    user=i
                if t==2:
                    pwd=i
                t+=1  
            connect_mysql(host,user,pwd)

        if args.scanportIP:
            while not modules.sniff.isIP(args.scanportIP):
                args.scanportIP = input('地址不正确或未在线，请输入正确的IP地址:\n')
            
            modules.sniff.ScanPort(args.scanportIP).start()
        if args.whois:
            modules.sniff.whois_sniff(args.whois)
        if args.scanwebdirURL:
            if args.directory:
                modules.sniff.start_dirscan(args.scanwebdirURL,args.directory,args.thread)
            else: 
                modules.sniff.start_dirscan(args.scanwebdirURL,"modules/dict.txt",args.thread)
        if args.cms:
            import modules.cms as cms
            cms.set_agent(agent)
            cms.cms(args.cms)
        if args.shodan:
            modules.sniff.shodan_search(args.shodan)
        if args.poc:
            import os
            os.system("python modules/ws.py -t"+args.poc)

        #EXP
        if args.dos and args.rhost and args.rport:
            import modules.dosattack as y
            y.exp(args.rhost,args.rport,args.thread)

        if args.webshell:
            import modules.webshell as w
            w.set_agent(agent)
            t=0
            for i in args.webshell:
                if t==0:
                   url=i
                if t==1:
                    passwd=i
                t+=1
            w.exp(url,passwd)   
        if args.ssh:
            import modules.ssh as s
            if args.directory:
                s.force_ssh(args.rhost,args.directory,args.user,args.rport)
            else:
                s.force_ssh(args.rhost,'modules\pwddic\password\_top19576.txt',args.user,args.rport)
        if args.ddos==True:
            import os
            os.system("python2 modules/ddos.py")
        if args.exp and args.expip:
            for exp in args.exp:
                exp=exp.replace("-","_")
                exp=exp.replace("cve","C")
                exec("import modules.exp."+exp+"_EXP as t\n")
                exec(f"t.set_agent(agent)\n")
                exec(f"t.exp('{args.expip}',{args.rport})")

#end
