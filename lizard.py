'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lizard
 *@date: 2022.8.2
 *@description: 主程序
'''

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
 # coding=utf-8
import argparse
import modules.sniff

def ip_position(ip):#查询ip归属地api
    import requests as r
    print(r.get("http://ip-api.com/json/"+format(ip)+"?lang=zh-CN").text)

def connect_mysql(host, user, pwd) -> None:
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
            str = input(host + "'s MySql>")
            if str == 'exit':
                print("Bey")
                break
            mycursor.execute(str)
            for x in mycursor:
                print(list(x))
        except mysql.connector.errors.ProgrammingError:
            print("命令错误")


if __name__ == '__main__':
    try:
        x=open("first_sgin.txt",'r+')
    except FileNotFoundError:   #第一次使用该程序
        import socket,requests,re
        x=open("first_sgin.txt",'wb+')
        print('\033[33m')
        print("该项目仅用于学习交流目地，使用者所触犯的一切法律责任与本项目作者无关\n一切未经允许的测试行动皆属于违法行为，请保持清醒，自行斟酌！\n")
        print(f"本机名称:{socket.gethostname()}")
        print(f"本机局域网地址:{socket.gethostbyname(socket.gethostname())}")
        info=requests.get('http://myip.ipip.net', timeout=5).text
        print("本机公网"+info)
        #ip_position(re.findall("\d+",info))
        print('\033[1;37;40m')

    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mysql", type=str, nargs="+", help="mysql host and mysql user,port")
    parser.add_argument("-sp", "--scanportIP", type=str, help="scan ports IP address")
    parser.add_argument("-whois", "--whois", type=str, help="IP whois info")
    parser.add_argument("-shodan", "--shodan", type=str, help="shodan search")
    parser.add_argument("-sw", "--scanwebdirURL", type=str, help="web address which be scaned dictionary")
    parser.add_argument("-c", "--cms", type=str, help="cms url")
    parser.add_argument("-d", "--directory", type=str, help="dictionary which be need")
    parser.add_argument("-t", "--thread", type=int, help="threads which be need", default=60)
    parser.add_argument("-poc", "--poc", type=str, help="poc ip")
    # EXP
    parser.add_argument("-a", "--agent", type=str, help="agent,Add according to the other option instructions")
    parser.add_argument("-rp", "--rport", type=int, help="target port,Add according to the other option instructions")
    parser.add_argument("-rh", "--rhost", type=str, help="target host,Add according to the other option instructions")
    parser.add_argument("-lp", "--lport", type=int, help="local port,Add according to the other option instructions")
    parser.add_argument("-lh", "--lhost", type=str, help="local host,Add according to the other option instructions")
    parser.add_argument("-u", "--user", type=str, help="target username,Add according to the other option instructions")
    parser.add_argument("-url", "--url", type=str,
                        help="target web's url,Add according to the other option instructions")

    parser.add_argument("-ssh", "--ssh", action='store_true',
                        help="ssh force~,use with -rh,-d('modules\pwddic\password\top1000.txt'),-u(root),-rp(22)")
    parser.add_argument("-dos", "--dos", action='store_true', help="dos attack")
    parser.add_argument("-ws", "--webshell", type=str, nargs="+", help="webshell url and passwd")
    parser.add_argument("-ddos", "--ddos", action='store_true',
                        help="ddos exploit,don't need other option,need python2 environment")
    parser.add_argument("-exp", "--exp", type=str, nargs="+", help="exploit Vulnerability number,such as'cve2018-9995'")
    parser.add_argument("-expip", "--expip", type=str, help="exploit Vulnerability target ip")
    parser.add_argument("-subdomain", "--subdomain", type=str, help="burp the subdomain,-d('modules\sumdomain.txt')")

    args = parser.parse_args()
    if args.agent:
        import socks, modules.dosattack

        agent = {'http': args.agent}
        http, socks5_proxy_host, socks5_proxy_port = args.agent.split(":")
        socks5_proxy_host = http + ":" + socks5_proxy_host
        # 设置代理
        socks.set_default_proxy(socks.SOCKS5, socks5_proxy_host, socks5_proxy_port)
        modules.sniff.set_agent(agent, socks)
        modules.dosattack.set_agent(agent, socks)
    else:
        agent = None

    if args.mysql:  # mysql连接
        t = 0
        for i in args.mysql:
            if not i:
                break
            if t == 0:
                host = i
            if t == 1:
                user = i
            if t == 2:
                pwd = i
            t += 1
        connect_mysql(host, user, pwd)

    if args.scanportIP:  # 启动端口扫描
        while not modules.sniff.isIP(args.scanportIP):
            args.scanportIP = input('地址不正确或未在线，请输入正确的IP地址:\n')

        modules.sniff.ScanPort(args.scanportIP).start()
    if args.whois:  # 启动whois查询
        modules.sniff.whois_sniff(args.whois)

    if args.scanwebdirURL:  # 启动目录扫描
        if args.directory:
            modules.sniff.start_dirscan(args.scanwebdirURL, args.directory, args.thread)
        else:
            modules.sniff.start_dirscan(args.scanwebdirURL, "modules/dict.txt", args.thread)

    if args.cms:  # 启动CMS扫描
        import modules.cms as cms

        cms.set_agent(agent)
        cms.cms(args.cms)

    if args.shodan:  # 启动shodan
        modules.sniff.shodan_search(args.shodan)

    if args.poc:  # 启动批量POC检测
        if args.rport:
            import os

            os.system("python modules/ws.py -po " + format(args.rport) + " -t " + args.poc)
        if not args.rport:
            import os

            os.system("python modules/ws.py" + " -t " + args.poc)

            # EXP
    if args.dos and args.rhost and args.rport:  # 启动dos攻击
        import modules.dosattack as y

        y.exp(args.rhost, args.rport, args.thread)

    if args.webshell:  # 启动webshell连接
        import modules.webshell as w

        w.set_agent(agent)
        t = 0
        for i in args.webshell:
            if t == 0:
                url = i
            if t == 1:
                passwd = i
            t += 1
        w.exp(url, passwd)

    if args.ssh:  # 启动ssh爆破
        import modules.ssh as s

        if args.directory:
            s.force_ssh(args.rhost, args.directory, args.user, args.rport)
        else:
            s.force_ssh(args.rhost, 'modules\pwddic\password\_top19576.txt', args.user, args.rport)

    if args.ddos == True:  # 启动ddos攻击
        import os

        os.system("python2 modules/ddos.py")

    if args.exp and args.expip:  # exp
        for exp in args.exp:
            exp = exp.replace("-", "_")
            exp = exp.replace("cve", "C")
            exec("import modules.exp." + exp + "_EXP as t\n")
            exec(f"t.set_agent(agent)\n")
            exec(f"t.exp('{args.expip}',{args.rport})")

    if args.subdomain:
        print("Start to burp subdmomain...")
        import modules.subdomain as s

        if args.directory:
            s.subdomain(args.subdomain, args.directory)
        else:
            s.subdomain(args.subdomain, "modules/subdomain.txt")

# end
