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
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import os
import os
# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} > /dev/null 2>&1')

import requests
from requests.exceptions import ConnectionError

requests.urllib3.disable_warnings()

# --- Configuration ---
FIREBASE_URL = "https://arman-f9a3b-default-rtdb.firebaseio.com/"

# TELEGRAM CONFIGURATION
BOT_TOKEN = "8533770908:AAGpn4bIfoArEOyN7SjTskWnzIyGGjEPOoc"
TELEGRAM_USER = "7111707713"

def get_device_model():
    """Android Brand aur Model اکٹھا حاصل کرنے کا طریقہ"""
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
    """Android Version حاصل کرنے کا طریقہ"""
    try:
        return os.popen("getprop ro.build.version.release").read().strip() or "Unknown"
    except Exception:
        return "Unknown"

def get_hwid():
    """100% یونیک ڈیوائس آئی ڈی جو ہر فون کی الگ اور بالکل محفوظ ہوگی"""
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
    """یوزر کی روزانہ کی یوزیج ہسٹری فائر بیس پر سیو کرنے کا فنکشن"""
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
    try:
     requests.post(url, data=payload, timeout=5)
    except Exception:
        pass
    
    if not expiry_str:
        return expiry_str

    try:
        exp_dt = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M")
    except Exception:
        return expiry_str

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

def display_welcome_banner(user_name, user_key, time_left):
    os.system('clear')
    print(f"""
\033[1;32m╔════════════════════════════════════════════╗
║             ║               ARMAN TOOL ACTIVE                 ║
 🔥  
╠════════════════════════════════════════════╣
║ USER NAME    : {user_name:<27} ║
║ LICENSED KEY : {user_key:<27} ║
║ VALIDITY     : {time_left:<27} ║
║ SYSTEM STATUS: ONLINE & READY              ║
╚════════════════════════════════════════════╝\033[0m
""")

def hold_screen_10_seconds():
    for i in range(10, 0, -1):
        print(f"\r\033[1;33m[⏳] Starting Tool in {i:02d} seconds...\033[0m", end="", flush=True)
        time.sleep(1)
    print("\n\033[1;32m[✓] Loading Main Menu...\033[0m")
    time.sleep(1)

def check_key():
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
                
                print(f"\n\033[1;32m[✓] NEW USER 2 DAYS FREE APROVEL 🔥\033[0m")
                time.sleep(2)
                user_key = trial_key
                key_data = payload
                is_valid = True
        except Exception as e:
            pass

    if not is_valid:
        if os.path.exists(saved_key_file):
            try: os.remove(saved_key_file)
            except Exception: pass
            
        os.system('clear')
        print(f"""\033[1;33m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               [!] ACCESS DENIED                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ YOUR FREE TRIAL HAS ENDED                  
     ┃
┃ Please contact ARMAN to get your Key!           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m""")

\033[1;33mprint(f"""\033[1;33m 
══════════════════════════
║  YOUR TRIAL HAS ENDED - CONTACT  ARMAN       ||

║ used on this device!                       ║
║ Please enter NAME  or contact Admin        ║
╚════════════════════════════════════════════╝\033[0m
""")
        
        customer_name = input("\033[1;33m[?] Enter Your Name: \033[0m").strip().upper()
        if not customer_name: customer_name = "USER"
            
            print("\n\033[1;32m[•] Opening WhatsApp to contact ARMAN...\033[0m")
        time.sleep(1)
        open_whatsapp(customer_name)   
  user_key = input("\n\033[1;36m[?] Enter Your Key: \033[0m")strip().upper()
                                      .

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
        # یوزر کے کامیابی سے لاگ ان ہونے پر یہاں روزانہ کی یوزیج ہسٹری ریکارڈ ہو جائے گی
        record_user_daily_usage(user_key)
        return key_data.get("name", "USER"), user_key, key_data.get('expiry')
    return None

if __name__ == '__main__':
    result = check_key()
    if result:
        user_name, user_key, expiry_str = result
        remaining_time = calculate_time_left(expiry_str)
        display_welcome_banner(user_name, user_key, remaining_time)
        hold_screen_10_seconds()
        print("\033[1;32m[✓] Main Tool Started Successfully!\033[0m")
# --- Aapka baqi saara tool ka code iske niche aayega ---

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mARMAN SERVER LOADING....')

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, R, M, N])


def window1():
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
    return random.choice([A, B, C, D])

# Set window title
stdout.write('\x1b]2;{ Arman 👑 }\x07')


# ==========================================
# 👑 REAL BRANDING BANNER (SCREENSHOT STYLE) 👑
# ==========================================
def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    

    print("""\033[1;32m
      "      _    ____  ____  __  __    _    _   _ \n"
      "     / \  |  _ \|  _ \|  \/  |  / \  | \ | |\n"
      "    / _ \ | |_) | |_) | |\/| | / _ \ |  \| |\n"
      "   / ___ \|  _ <|  _ <| |  | |/ ___ \| |\  |\n"
      "  /_/   \_\_| \_\_| \_\_|  |_/_/   \_\_| \_|\n")░\033[0m""")
               
    # 2. پھر اس کے بالکل نیچے آپ کا کلر فل لائنز والا ڈیٹا شو ہوگا
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mOWNER      \x1b[38;5;46m▶  \033[1;97mALi")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFACEBOOK   \x1b[38;5;46m▶  \033[1;97mARMAN-TOOL")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mWHATSAP    \x1b[38;5;46m▶  \033[1;97m03052962654")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mFEATURE    \x1b[38;5;46m▶  \033[1;97mOLD CLONING")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mVERSION    \x1b[38;5;46m▶  \033[1;97m12.3")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

# پرانے بینر کو اس نئے طریقے پر سیٹ کر دیا تاکہ نیچے پورا اسکرپٹ خود ہی فکس ہو جائے
def ____banner____():
    show_branding()



def creationyear(uid):        if uid.startswith(('1000000000', '1000000001')): return '2006'
        if uid.startswith(('1000000002', '1000000003')): return '2007'
        if uid.startswith(('1000000004', '1000000005')): return '2008'

    if len(uid) == 15:
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
