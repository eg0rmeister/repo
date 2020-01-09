#!/usr/bin/python3

import os
import subprocess
date = subprocess.check_output(["date", "+%F-%H:%M:%S"]).decode("utf-8")
print(date)
#os.system("git add *")
os.system("git commit -m " + date)