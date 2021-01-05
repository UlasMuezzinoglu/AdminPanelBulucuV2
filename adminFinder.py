# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 08:15:10 2020

@author: ULAS
"""

# libs        
from urllib.request import urlopen,Request,HTTPError,URLError
from colorama import Fore, Back, Style, init
flag=True


def panelBul():
    init(autoreset=True)
    f = open("subs.txt","r");
    link = input("Site Linki Giriniz (www zorunlu değil): ")
    print ("\n\nSaptanan linkler : \n")
    while True:
        subLink = f.readline()
        if not subLink:
            break
        reqLink="http://"+link+"/"+subLink
        req=Request(reqLink)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e1:
            print(Back.WHITE+Fore.RED+"Lütfen Geçerli Bir URL Girin YADA internet bağlantınızı kontrol edin")
            break
        except UnicodeEncodeError as e2:
            continue
        except Exception as e3:
            continue
        else:
            try:
                print(Fore.GREEN+"Bulundu !",reqLink)
            except Exception as e4:
                print("Bulundu !",reqLink)

def imza():
    init(autoreset=True)
    print("""
###############################################
#              Admin Paneli Bulucu            #
#                 Coded By Ulaş               #
#                 Versiyon 1.0                # 
#                                             #
###############################################
    """)
    print(Back.WHITE+Fore.RED+"Programın Çalışabilmesi için gerekli Kütüphaneleri Yükleyin. (colorama) \n")

imza()
while True:
    panelBul()
        
	
    
