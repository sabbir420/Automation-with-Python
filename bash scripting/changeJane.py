#!/usr/bin/env python3
import sys
import subprocess
with open(sys.argv[1]) as file:
    line = file.readlines()
    for value in line:
        line_strip = value.strip()
        new_line = line_strip.replace('jane','jdoe')
        subprocess.run(["mv",line_strip,new_line])
file.close()
