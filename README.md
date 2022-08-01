# Lizard

![https://www.python.org](https://img.shields.io/badge/language-python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/features-convenient-informational?style=flat&color=2bbc8a)
![](https://img.shields.io/badge/license-MIT_License-informational?style=flat&logoColor=white&color=2bbc8a)
[](https://img.shields.io/packagist/stars/wr0x00/Lizard?style=flat-square)

Lizard是一款基于python的全自动化渗透脚本，小巧轻便，功能丰富，可在多平台快速部署；整体采用模块化设计，可自行调用

功能
----
* 嗅探：端口扫描、IP探测、爆破（目前只支持ssh）、shodan扫描、网站目录后台扫描、whois查询，CMS扫描，poc检测
    * 目前可支持的poc有：
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
    * （不断更新中）
* webshell一句话连接（目前只支持模拟终端功能，以后会完善）
* dos攻击，ddos攻击(外接模块，需要python2，python3的正在开发中)
* exp利用
    * 目前支持的exp有：
    * cve-2022-21907
    * cve-2018-9995
    * （不断更新中）

已测试环境
------
* Windows
* kali Linux
* termux(Android)
* Debian

安装
--
      git clone https://github.com/wr0x00/Lizard
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
* -poc poc批量扫描
   * 例：python lizard.py -poc 192.168.1.1
* -exp -指定多个exp(漏洞名称去掉cve后面短横，写成cveXXXX-XXXX格式) -expip目标ip -rp指定端口（若不指定则自动扫描）
   * 例：python lizard.py -exp cve2018-9995 -expip xxx.xxx.xxx.xxx -rp xx
   * 例：python lizard.py -exp cve2018-9995 cve2022-21907 -expip xxx.xxx.xxx.xxx -rp xx
 
法律声明
---
该项目仅用于学习交流目地，使用者所触犯的法律责任与本项目作者无关，一切未经允许的测试行动皆属于违法行为，请保持清醒，自行斟酌


