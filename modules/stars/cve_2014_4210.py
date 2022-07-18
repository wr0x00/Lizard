#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# CVE-2014-4210
# updated 2019/10/23
# by 0xn0ne

import sys
from multiprocessing.managers import SyncManager
from typing import Any, Dict, List, Mapping, Tuple, Union

from utils import http

# 有漏洞的情况
# 端口不存在
# An error has occurred
# weblogic.uddi.client.structures.exception.XML_SoapException: Tried all: '1' addresses, but could not connect over HTTP to server: 'x.x.x.x', port: '80'
# 端口存在
# An error has occurred
# weblogic.uddi.client.structures.exception.XML_SoapException: Received a response from url: http://x.x.x.x:7001 which did not have a valid SOAP content-type: text/html.
from stars import target_type, Star


# @universe.groups()
class CVE_2014_4210(Star):
    info = {
        'NAME': 'webLogic server server-side-request-forgery',
        'CVE': 'CVE-2014-4210',
        'TAG': []
    }
    type = target_type.MODULE

    def light_up(self, dip, dport, force_ssl=None, *args, **kwargs) -> (bool, dict):
        r, data = http(
            'http://{}:{}/uddiexplorer/SearchPublicRegistries.jsp'.format(dip, dport), ssl=force_ssl)
        if r and r.status_code == 200:
            return True, {'url': r.url}
        return False, {}

def run(queue: SyncManager.Queue, data: Dict):
    obj = CVE_2014_4210()
    result = {
        'IP': data['IP'],
        'PORT': data['PORT'],
        'NAME': obj.info['CVE'] if obj.info['CVE'] else obj.info['NAME'],
        'MSG': '',
        'STATE': False
    }
    result['STATE'], result['MSG'] = obj.light_and_msg(
        data['IP'], data['PORT'], data['IS_SSL'])

    queue.put(result)
