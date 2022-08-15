# Lizard
English|[简体中文](https://github.com/wr0x00/Lizard/blob/main/README_CN.md)

![https://www.python.org](https://img.shields.io/badge/language-python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/features-convenient-informational?style=flat&color=2bbc8a)
![](https://img.shields.io/badge/license-MIT_License-informational?style=flat&logoColor=white&color=2bbc8a)
[](https://img.shields.io/packagist/stars/wr0x00/Lizard?style=flat-square)

Lizard is a python-based fully automated infiltration script,feature-rich and can run on termux(Android).

function
----
* Sniffing: port scanning, IP probing, blasting, shodan scanning, website directory background scanning, whois query, CMS scanning, poc detection
    * Currently supported pocs are:
    * cve_2016_0638
    * cve_2016_3510
    * cve_2017_10271
    * cve_2017_3248
    * cve_2017_3506
    * cve_2018_2628
    * cve_2018_2893
    * cve_2018_2894
    * cve_2018_3191
    * cve_2018_3245
    * cve_2018_3252
    * cve_2019_2618
    * cve_2019_2725
    * cve_2019_2729
    * cve_2019_2888
    * cve_2019_2890
    * cve_2020_14750
    * cve_2020_14882
    * cve_2020_14883
    * cve_2020_2551
    * cve_2020_2555
    * cve_2020_2883
    * CNVD_2021_30167
    * CVE_2021_21907
    * (Updating...)
* Webshell connection (currently only supports analog terminal function, will be improved in the future)
* dos attack, ddos attack (external module, python2 required, python3 is under development)
* exp utilization
    * Currently supported exps are:
    * cve-2022-21907
    * cve-2018-9995
    * WLAN-AP-WEA453e
    * (Updating...)
 
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
* -ssh ssh blasting, -rh specifies the address, -u specifies the user (default root), -rp specifies the port (default 22), -d specifies the dictionary (default modelespwddicpasswordtop1000.txt)
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
 
 Legal Notices
 ----
 The project is only used for the purpose of learning and communication, the legal responsibility of the user has nothing to do with the author of the project, and all unauthorized test actions are illegal, please stay sober and consider it yourself.
