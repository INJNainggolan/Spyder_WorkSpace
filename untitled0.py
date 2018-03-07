#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:05:09 2017

@author: nainggolan
"""

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        return "产生异常"

if __name__=="__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))