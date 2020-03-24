import time
import os

time.sleep(2)
os.system("clear")
print("\033[31m[\033[94m*\033[31m] \033[92mInstalling Apache2")
os.system("apt install apache2")
os.system("clear")
print("\033[31m[\033[94m*\033[31m] \033[92mStarting Apache2")
os.system("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
os.system("apachectl start")
os.system("clear")
os.system("ls")
os.system("clear")


