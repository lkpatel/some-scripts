#!/usr/bin/python

#This code check which proxies are working in a given list of proxies
#you need to provide proxy usernamd and password


import argparse
import requests
parser = argparse.ArgumentParser()
parser.add_argument('--username', help='Give your user name',required=True)
parser.add_argument('--password', help='Give your password',required=True)
args = vars(parser.parse_args())
bare_proxy_list = ['192.168.2.5','192.168.2.6','192.168.2.7','192.168.2.8','192.168.2.9','192.168.2.10']
proxy_list = {}
error_guide ="""
General Error Code Information :- 
 
1xx -- Informational
2xx -- Success
3xx -- Redirection
4xx -- client error
5xx -- Server error; 503 = Service unavailable, 504 = Gateway timeout
"""
print error_guide
for proxy in bare_proxy_list: 
    my_proxy = "http://"+args['username']+":"+args['password']+"@"+proxy+":8080"
    proxy_list['http']=my_proxy
    proxy_list['https']=my_proxy
    try:
      result = requests.get("http://google.co.in", proxies=proxy_list) 
      if result.status_code == 200:
         print proxy + " is working"
      else:
         print proxy + " is not working with response code = "+str(result.status_code)
    except IOError: pass

