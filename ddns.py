#!/usr/bin/env python
#-*- coding:utf-8 -*-

import httplib, urllib
import socket
import time
import datetime

params = dict(
    login_email="your email address", # replace with your email
    login_password="your password", # replace with your password
    format="json",
    domain_id=12345678, # replace with your domain_od, can get it by API Domain.List
    record_id=123456789, # replace with your record_id, can get it by API Record.List
    sub_domain="www", # replace with your sub_domain
    record_line="默认",
)
domain="www.xxx.xxx"    #replace with your domain

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)
    
    response = conn.getresponse()
    #print response.status, response.reason
    data = response.read()
    #print data
    conn.close()
    return response.status == 200

def get_host_ip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    sock.settimeout(10)
    ip = sock.recv(16)
    sock.close()
    return ip

def local_log(file_name,text):
    fo = open(file_name,"a")
    strTime = time.asctime(time.localtime(time.time()))
    #print strTime
    fo.write(strTime+" ip:"+text)
    fo.close()



if __name__ == '__main__':
    host_ip = get_host_ip()
    domain_ip = socket.gethostbyname(domain)
    if  host_ip != domain_ip :
        ddns(host_ip)
        #print "current host ip:",host_ip
        #print "domain  ip:",domain_ip
        #print "domain:",domain


