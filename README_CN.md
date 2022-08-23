# Lizard

![https://www.python.org](https://img.shields.io/badge/language-python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/features-convenient-informational?style=flat&color=2bbc8a)
![](https://img.shields.io/badge/license-MIT_License-informational?style=flat&logoColor=white&color=2bbc8a)
[](https://img.shields.io/packagist/stars/wr0x00/Lizard?style=flat-square)
[![OSCS Status](https://www.oscs1024.com/platform/badge/wr0x00/Lizard.svg?size=small)](https://www.oscs1024.com/project/wr0x00/Lizard?ref=badge_small)

Lizard一款基于python的web安全渗透测试集成工具，可在多平台快速部署；拥有独立API

功能
----
* 嗅探：端口扫描、IP探测、爆破（目前只支持ssh）、shodan扫描、网站目录后台扫描、whois查询，CMS扫描，poc检测
    * [目前支持的poc](https://github.com/wr0x00/Lizard/wiki/Supported_poc_CN)
* webshell一句话连接（目前只支持模拟终端功能，以后会完善）
* dos攻击，ddos攻击(外接模块，需要python2，python3的正在开发中)
* exp利用
    * [目前支持的exp](https://github.com/wr0x00/Lizard/wiki/Support_EXP_CN)
   
已测试环境
------
* Windows
* kali Linux
* termux(Android)
* Debian
* Arch Linux

安装
--
      git clone https://github.com/wr0x00/Lizard
      cd Lizard
      python.exe -m pip install --upgrade pip
      pip install -r requirement.txt
使用
---
       python lizard.py --help
* -a 启用代理,输入地址,如需使用，在以下选项后面加上此参数
   * 例：python lizard.py -xxx xxx -a https://xxx.xxx.xxx.xxx:xx
* -m 连接MySQL，依次输入地址，用户名，密码
   * 例：python lizard.py -m localhost root 1234
* -sp 扫描端口，输入IP
   * 例：python lizard.py -sp 192.168.1.1
* -whois whois查询，输入网址
   * 例：python lizard.py -whois www.xxx.com
* -shodan shodan关键字批量搜索IP，也可单个扫描端口
   * 例：python lizard.py -shodan abc
   * 例：python lizard.py -shodan www.xxx.com
* -sw 扫描网站目录，输入网址,-d指定字典,默认字典dict.txt,-t指定线程，默认60
   * 例：python lizard.py -sw www.xxx.com (-d xxx.txt)(-t xx)
* -c 进行CMS扫描，输入网址
   * 例：python lizard.py -c www.xxx.com
* -ssh ssh爆破，-rh指定地址，-u指定用户(默认root)，-rp指定端口（默认22），-d指定字典（默认modules\pwddic\password\top1000.txt）
   * 例：python lizard.py -ssh -rp 192.168.1.1 (-u xxx -rp xx -d xxx.txt)
* -webshell 连接php一句话，依次输入网址、密码
   * 例：python lizard.py -webshell www.xxx.com/abc.php 123
* -ddos ddos攻击
   * 例：python lizard.py -ddos
* -poc poc批量扫描 -rp指定端口（默认80）
   * 例：python lizard.py -poc 192.168.1.1 （-rp xx）
* -exp -指定多个exp(漏洞名称去掉cve后面短横，写成cveXXXX-XXXX格式) -expip目标ip -rp指定端口（若不指定则自动扫描）
   * 例：python lizard.py -exp cve2018-9995 -expip xxx.xxx.xxx.xxx -rp xx
   * 例：python lizard.py -exp cve2018-9995 cve2022-21907 -expip xxx.xxx.xxx.xxx -rp xx
* -subdomain 爆破目录子域名, -d指定字典（默认modules\subdomain.txt)
   * 例：python lizard.py -subdomain www.xxx.com (-d xxx.txt)

注:首次使用该程序请选择语言
```shell
choose your local language/选择你的语言(EN|CN):
```
选择CN即可.

API 使用说明
----
Lizard 拥有独有的api,可根据需求自行调用
```python
import modules.~
或
from modules.~ import ~~~ 

#modules下各文件结构及所属功能:
   modules.sniff:
      whois_sniff(URL) #whois查询
      shodan_search(str) #傻蛋(shodan)关键字批量检索IP
      start_dirscan(URL,Dict,thread)  # 扫描网站目录
      isurl(url)->bool #验证该网址是否可以正常连接
      ScanPort(url).start() #扫描端口,注意此类需要后缀start()才能启动
   modules.ssh:
      force_ssh(host,pwddict,users='root',port=22)#爆破ssh
   modules.webshell:
      exp(url,passwd)#webshell一句话连接
   modules.cms:
      cms(url) #CMS扫描
   modules.subdomain:
      subdomain(domain, dictonary)#子域名爆破
   modules.dosattack:
      exp(host:str,port:str,thread:int)#dos攻击
 ```
### 例如
扫描www.xxx.com的目录
```python
from modules.sniff import start_dirscan
start_dirscan(www.xxx.com)
```

法律声明
---
该项目仅用于学习交流目地，使用者所触犯的法律责任与本项目作者无关，一切未经允许的测试行动皆属于违法行为，请保持清醒，自行斟酌

