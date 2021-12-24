# Team: Life Of Programmer
# Mod By: Iqbalz Noobs
# klo gak ada passion jangan jadi programmer, ngoding itu berat kamu gk akan kuat...

import os
import sys
import time
import json
import requests


w = "\033[90;1m" # White dark
r = "\033[91;1m" # red
g = "\033[92;1m" # green
y = "\033[93;1m" # yellow
p = "\033[94;1m" # pink
bl = "\033[96;1m"

pu = "\033[97;1m" # white light


def runntxt(s):
                for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(10. / 100)
def banner_noobs():
                os.system('clear')
                print " "
                os.system('toilet -f small "RAMA-XD" -F gay')
                os.system('date | lolcat')
                print " "
                runntxt(bl+"     T H E  N E W B I E  T E R M U X E R'S     ")
                print g+"\==========================================/"
                print y+"\ Mod By: RAMADHANI                        /"
                print y+"\ Github: https://www.github.com/RAMA-XD   /"
                print g+ "\==========================================/"
                
                print ">_ INGFO : SCRIPT INI 90% ANTI CP "
                
                print r+ "#############################################"
                print g+"L O G I N   DI   B A W A H"
                
                print "U N T U K   M E N D A P A T K A N   T O K E N"
                print r+ "#############################################"
                 
banner_noobs()

user_noobs = raw_input(r+'[?] \033[96mInput Email Todz\033[97m   : ')
passwordlu = raw_input(g+'[?] \033[95mInput Pasword Todz\033[97m : ')
iqbalz_noobs = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_noobs+'&locale=en_US&password='+passwordlu+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

lop = iqbalz_noobs.content
bacot = json.loads(lop)
if "session_key" in lop:
                print " "
                runntxt(w+" Loanjing....")
		print pu+"[+] Token Telah Berhasil Di Ambil. \033[91m=>\033[92m " + bacot["access_token"]
		open(user_noobs+"iqbalz_token.txt", 'a').write(bacot["access_token"])
		print " "
		print w+"        T O K E N  S U C C E S S "
                print w+"                  T O D"
                print pu+" "
                runntxt(bl+' JANGAN DI RECODE !')
                print pu+" "
else:
		print r+"Login Gagal Tod...."
		print " "
                print w+" "
