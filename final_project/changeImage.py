#!/usr/bin/env python3

import os,glob
from PIL import Image

for files in glob.glob("/home/student-04-e1a4e4b25306/supplier-data/images/*.tiff"):
	im = Image.open(files)
	out_name = os.path.basename(files)[:3]
	#resize image to 600x400 and save it as jpeg format
	size = 600, 400
	im_resized = im.resize(size, Image.ANTIALIAS)
	im_resized = im_resized.convert('RGB')
	im_resized.save("/home/student-04-e1a4e4b25306/supplier-data/images/" + out_name + ".jpeg", "JPEG")