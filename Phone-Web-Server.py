import time
import os

time.sleep(2)
os.system("clear")
print("[*] Installing Apache2")
os.system("apt install apache2")
print("[*] Setting Up Apache2")
time.sleep(3)
print("[*] Starting Apache2")
os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
os.system("apachectl start")


