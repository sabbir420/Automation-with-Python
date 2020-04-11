#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20
def check_cpu_usage():
    cp = psutil.cpu_percent(1)
    return cp < 70

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is okay!")
