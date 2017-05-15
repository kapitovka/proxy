#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import ipaddress
import threading
import sys
import time

max = 15
sem = threading.Semaphore(max)       
def check_proxy(ip,port):
    
       
        ip = str(ip) + ":" + port
        proxy = urllib.request.ProxyHandler({'http':ip})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
    
        try:
            
            ret = urllib.request.urlopen('http://www.google.com')
            
        except urllib.error.URLError as e:

                if(500):
                    write_result(ip,'500')
                    print(ip+'----- 500')
                else:    
                    write_result(ip,'e')
                    print(ip+'----- error.URLError')
                
        except urllib.request.URLError as e:
                write_result(ip,'e')
                print(ip+'----- request.URLError')
                
        else:
            write_result(ip,'proxy')
            print (ip+'-------------- Proxy')
        
        
def start_thread(st_ip,end_ip,port):
    
    
    while(st_ip<=end_ip):
        if(threading.active_count()<max):
           
            try:
                threading.Thread(target=check_proxy,args=(st_ip,port)).start()
               
            except:
                print(str(st_ip)+'------ThreadError')
                
            st_ip = st_ip + 1
            
        else:
            time.sleep(5)
            
def write_result(ip,result):
    
    f = open(result+'.txt', 'at')
    
    
    
    str = time.strftime('%X %x %z |||')+'ip:'+ip+'\n'
    
    f.write(str)
    f.close()
    
def main(st_ip,end_ip,port):
    
    
    end_ip = ipaddress.ip_address(end_ip)
    st_ip = ipaddress.ip_address(st_ip)
    
    
    start_thread(st_ip,end_ip,port)
    
    # 1.Получение диапазона ip адресов
             
       
    
opt = sys.argv   
opt = list(opt)
#res = main(opt[1],opt[2],opt[3])       
res = main(opt[1],opt[2],opt[3])      
#print (res)
         
#print check_head(get_head('37.59.77.217',80));