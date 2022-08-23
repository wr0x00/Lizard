# Lizard
English|[简体中文](https://github.com/wr0x00/Lizard/blob/main/README_CN.md)

![https://www.python.org](https://img.shields.io/badge/language-python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/features-convenient-informational?style=flat&color=2bbc8a)
![](https://img.shields.io/badge/license-MIT_License-informational?style=flat&logoColor=white&color=2bbc8a)
[](https://img.shields.io/packagist/stars/wr0x00/Lizard?style=flat-square)
[![OSCS Status](https://www.oscs1024.com/platform/badge/wr0x00/Lizard.svg?size=small)](https://www.oscs1024.com/project/wr0x00/Lizard?ref=badge_small)

Lizard is a python-based network security penetration testing tool,integrate multiple functions and it can even run on termux(Android).

Function
----
* Sniffing: port scanning, IP probing, blasting, shodan scanning, website directory background scanning, whois query, CMS scanning, poc detection
    * [Currently supported pocs](https://github.com/wr0x00/Lizard/wiki/supported_poc_EN)
    
* Webshell connection (currently only supports analog terminal function, will be improved in the future)
* dos attack, ddos attack (external module, python2 required, python3 is under development)
* exp utilization
    * [Currently supported exps](https://github.com/wr0x00/Lizard/wiki/Support_EXP_EN)
 
Tested environment
------
* Windows
* kali Linux
* termux(Android)
* Debian
* Arch Linux

Installing
------
      git clone https://github.com/wr0x00/Lizard
      cd Lizard
      python.exe -m pip install --upgrade pip
      pip install -r requirement.txt

Usage
----
       python lizard.py --help
* -a Enable proxy, enter the address, and if necessary, add this parameter after the following options
   * Example: python lizard.py -xxx xxx -a https://xxx.xxx.xxx.xxx.xxx:xx
* -m Connect to MySQL, enter the address, username, password in turn
   * Example: python lizard.py -m localhost root 1234
* -sp Scan open ports, enter target IP
   * Example: python lizard.py -sp 192.168.1.1
* -whois whois lookup, enter the URL
   * Example: python lizard.py -whois www.xxx.com
* -shodan shodan keyword batch search IP, can also scan the port individually
   * Example: python lizard.py -shodan abc
   * Example: python lizard.py -shodan www.xxx.com
*-sw scans the website directory, enters the URL, -d specifies the dictionary, the default dictionary dict .txt, -t specifies the thread, defaults to 60
   * Example: python lizard.py -sw www.xxx.com (-d xxx.txt)(-t xx)
* -c Perform a CMS scan, enter the URL
   * Example: Python lizard.py -c www.xxx.com
* -ssh ssh Brute force cracking, -rh specifies the address, -u specifies the user (default root), -rp specifies the port (default 22), -d specifies the dictionary (default modelespwddicpasswordtop1000.txt)
   * Example: python lizard.py -ssh -rp 192.168.1.1 (-u xxx -rp xx -d xxx.txt)
* - Webshell Connect php one sentence, enter the URL, password in turn
   Example: python lizard.py -webshell www.xxx.com/abc.php 123
* -ddos ddos attack
   * Example: Python lizard.py -ddos
* -poc poc batch scan -rp specified port (default 80)
   * Example: python lizard.py -poc 192.168.1.1 (-rp xx)
* -exp - Specify multiple exp (vulnerability name with short horizontal strips after cve and written in cveXXXX-XXXX format) - expip target ip -rp specify port (automatically scan if not specified)
   * Example: python lizard.py -exp cve2018-9995 -expip xxx.xxx.xxx.xxx -rp xx
   * Example: python lizard.py -exp cve2018-9995 cve2022-21907 -expip xxx.xxx.xxx.xxx -rp xx
* -subdomain blast directory subdomain, -d specifies dictionary (default modulessubdomain.txt)
   * Example: python lizard.py -subdomain www.xxx.com (-d xxx.txt)
 
Tip:The first time you use the program, you will be asked to select the language
 ```shell
   choose your local language/选择你的语言(EN|CN):
 ```
 choose EN.
 
API usage
----
Lizard has Python API that can be invoked by importing lizard's modules to your code.

```python
import modules.~

#Modules' files and functions:
   modules.sniff:
      whois_sniff(URL) #whois lookup
      shodan_search(str) #shodan keyword batch search IP
      start_dirscan(URL,Dict,thread)  # scans the website directory
      isurl(url)->bool #determine if the address is online
      ScanPort(url).start() #scan opened port
   modules.ssh:
      force_ssh(host,pwddict,users='root',port=22)#ssh Brute force cracking
   modules.webshell:
      exp(url,passwd)#webshell connect
   modules.cms:
      cms(url) #Perform a CMS scan
   modules.subdomain:
      subdomain(domain, dictonary)#blast directory subdomain
   modules.dosattack:
      exp(host:str,port:str,thread:int)#dos attack
 ```
 ### Example
 scan www.xxx.com directory
 ```python
 from modules.sniff import start_dirscan
 start_dirscan(www.xxx.com)
 ```
 
 Legal Notices
 ----
 The project is only used for the purpose of learning and communication, Any legal liability violated by the user has nothing to do with the author of this project, and all unauthorized test actions are illegal, please stay sober.
