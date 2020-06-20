# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhot
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhot")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER MEHEDI >
 \033[1;96m ------------------------
\033[1;91m  ____   ___ _____ ___  _     
\033[1;92m | __ ) / _ \_   _/ _ \| |    
\033[1;91m |  _ \| | | || || | | | |    
\033[1;92m | |_) | |_| || || |_| | |___ 
\033[1;91m |____/ \___/ |_| \___/|_____|
           \033[1;93m  ____    _    ____    _    
            \033[1;92m| __ )  / \  | __ )  / \   
            \033[1;91m|  _ \ / _ \ |  _ \ / _ \  
          \033[1;92m  | |_) / ___ \| |_) / ___ \ 
           \033[1;91m |____/_/   \_\____/_/   \_\                                             
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : MEHEDI HASAN ARIYAN
 FACEBOOK   : FACEBOOK.COM/THEMEHTAN
 YOUTUBE    : YOUTUBE.COM/MASTERTRICK1
 GITHUB     : GITHUB.COM/BOTOLMEHEDI
\033[1;32m
--------------------------------------------------
                                """

cusr = "botolbaba"
cpwd = "botolbaba"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : botolbaba (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : botolbaba (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : botolbaba (correct)")
    print(" TOOL PASSWORD : botolbaba (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Chacking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
