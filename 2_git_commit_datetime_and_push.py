#!/usr/bin/python3

import os
import subprocess
from getpass import getpass
date = subprocess.check_output(["date", "+%F-%H:%M:%S"]).decode("utf-8")
print(date)
os.system("git add *")
os.system("git commit -m " + date)
branch = subprocess.check_output(["git", "status"]).decode("utf-8").split("\n")[0].split()[2]
print(branch)
os.system("git push origin " + branch)
