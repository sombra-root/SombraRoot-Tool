#!/usr/bin/env python3

-- coding: utf-8 --

import os, socket, time, platform, hashlib, random, string, ssl, json
import urllib.request, urllib.parse

===== COLORS =====

GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"
CYAN="\033[96m"; PURPLE="\033[95m"; RESET="\033[0m"

def clear(): os.system("clear")

===== BANNER =====

def banner():
clear()
print(CYAN + """⠀⠀⢀⣴⣶⣿⣿⣷⡶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢶⣿⣿⣿⣿⣶⣄⠀⠀
⠀⢠⡿⠿⠿⠿⢿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡿⠿⠿⠿⠿⣦⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⡿⠆⠀⠀⠀⠀⠰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
""" + RESET)
print(PURPLE + "   SombraRoot Multi-Tool Framework\n" + RESET)

===== MENUS =====

def pause(): input("\nPress Enter...")

def main_menu():
print("""
[1] Scanner
[2] IP / OSINT
[3] DNS
[4] Web / Security
[5] Awareness
[6] Utilities
[0] Exit
""")

def scanner_menu():
print("""
[1] Port Scan
[2] Web Status
[3] Response Time
[4] Common Paths
[5] Ping Scan
[0] Back
""")

def ip_menu():
print("""
[1] IP Info
[2] Geolocation
[3] Reverse DNS
[4] ISP / ASN
[0] Back
""")

def dns_menu():
print("""
[1] Resolve Domain
[2] Reverse Lookup
[3] MX Lookup
[4] NS Lookup
[5] DNS Test
[0] Back
""")

def web_menu():
print("""
[1] HTTP Headers
[2] SSL Certificate Info
[3] robots.txt
[4] sitemap.xml
[5] Tech Detection
[0] Back
""")

def util_menu():
print("""
[1] Hash Text
[2] Hash File
[3] Password Generator
[4] Wordlist Generator
[5] System Info
[0] Back
""")

===== SCANNER =====

def port_scan():
host=input("Host: ")
for p in range(1,101):
s=socket.socket(); s.settimeout(0.3)
if s.connect_ex((host,p))==0:
print(GREEN+f"Port {p} OPEN"+RESET)
s.close()

def web_status():
url=input("URL: ")
try:
r=urllib.request.urlopen(url,timeout=5)
print("Status:",r.status)
except: print("Offline")

def response_time():
url=input("URL: ")
start=time.time()
try:
urllib.request.urlopen(url)
print("Response:",round(time.time()-start,2),"s")
except: print("Error")

def common_paths():
url=input("Base URL: ")
for p in ["/admin","/login","/.env","/config","/dashboard"]:
try:
urllib.request.urlopen(url+p)
print(GREEN+"FOUND "+p+RESET)
except: pass

def ping_scan():
host=input("Host: ")
os.system(f"ping -c 4 {host}")

===== IP / OSINT =====

def ip_info():
ip=input("IP: ")
data=json.loads(urllib.request.urlopen(f"http://ip-api.com/json/{ip}").read())
for k,v in data.items():
print(f"{k}: {v}")

def reverse_dns():
ip=input("IP: ")
try: print(socket.gethostbyaddr(ip))
except: print("No PTR")

===== DNS =====

def resolve_domain():
d=input("Domain: ")
print(socket.gethostbyname(d))

def dns_test():
socket.gethostbyname("google.com")
print("DNS OK")

===== WEB =====

def headers():
url=input("URL: ")
r=urllib.request.urlopen(url)
for k,v in r.getheaders(): print(f"{k}: {v}")

def ssl_info():
host=input("Domain: ")
ctx=ssl.create_default_context()
with ctx.wrap_socket(socket.socket(),server_hostname=host) as s:
s.connect((host,443))
cert=s.getpeercert()
print(cert)

===== UTILITIES =====

def hash_text():
t=input("Text: ").encode()
print("SHA256:",hashlib.sha256(t).hexdigest())

def password_gen():
l=int(input("Length: "))
chars=string.ascii_letters+string.digits+"!@#$%"
print("Password:","".join(random.choice(chars) for _ in range(l)))

===== MAIN LOOP =====

while True:
banner()
main_menu()
o=input(">> ")

if o=="1":  
    scanner_menu(); s=input(">> ")  
    if s=="1": port_scan()  
    elif s=="2": web_status()  
    elif s=="3": response_time()  
    elif s=="4": common_paths()  
    elif s=="5": ping_scan()  
    pause()  

elif o=="2":  
    ip_menu(); s=input(">> ")  
    if s=="1": ip_info()  
    elif s=="3": reverse_dns()  
    pause()  

elif o=="3":  
    dns_menu(); s=input(">> ")  
    if s=="1": resolve_domain()  
    elif s=="5": dns_test()  
    pause()  

elif o=="4":  
    web_menu(); s=input(">> ")  
    if s=="1": headers()  
    elif s=="2": ssl_info()  
    pause()  

elif o=="6":  
    util_menu(); s=input(">> ")  
    if s=="1": hash_text()  
    elif s=="3": password_gen()  
    pause()  

elif o=="0":  
    break
