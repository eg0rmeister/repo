#!/usr/bin/python3

import os
import subprocess
from getpass import getpass
date = subprocess.check_output(["date", "+%F-%H:%M:%S"]).decode("utf-8")
print(date)
os.system("git commit -m " + date)
print("enter password:",end='')
passwd = getpass()
print(branch)
os.system("git push origin " + branch)