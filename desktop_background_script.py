import requests
import json
import ctypes
import os
from PIL import Image, ImageOps


url = "http://rammb.cira.colostate.edu/ramsdis/online/images/latest_hi_res/himawari-8/full_disk_ahi_true_color.jpg"

# Download image
image_data = requests.get(url).content
with open('himawari.jpg', 'wb') as handler:
    handler.write(image_data)

#reopen image

abspath = os.path.abspath("himawari.jpg")
img = Image.open(abspath)

# make copy and edit
new_img = img.rotate(220)
new_img = new_img.crop((0, 0, 5500, 4000))

new_path = os.path.dirname(abspath) + r"\\himawari_mod.jpg"
ImageOps.expand(new_img, border=1000,fill='black').save(new_path)

SPIF_UPDATEINIFILE = 1

# update wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, new_path, SPIF_UPDATEINIFILE)