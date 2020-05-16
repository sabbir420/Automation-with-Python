#!/usr/bin/env python
import subprocess
import multiprocessing
from multiprocessing import Pool
import os

home = os.path.expanduser('~')

src = home + "/data/prod/"
dest = home + "/data/prod_backup/"
#subprocess.call(["rsync", "-arq", src, dest])
pool = Pool(multiprocessing.cpu_count())
pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))