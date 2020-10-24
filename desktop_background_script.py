import requests
import json
import ctypes
import os
from PIL import Image, ImageOps

# Sources (via http://downlinkapp.com/sources.json):
source_dict = {"GOES-East": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg",
               "GOES-West": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/latest.jpg",
               "Himawari-8": "http://rammb.cira.colostate.edu/ramsdis/online/images/latest_hi_res/himawari-8/full_disk_ahi_true_color.jpg",
               "Continental US": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg",
               "Tropical Atlantic": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/taw/GEOCOLOR/latest.jpg",
               "Tropical Pacific": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/tpw/GEOCOLOR/latest.jpg",
               "US West Coast": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/CONUS/GEOCOLOR/latest.jpg",
               "Northern Pacific": "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/np/GEOCOLOR/latest.jpg",
               "Northern South America": "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/nsa/GEOCOLOR/latest.jpg",
               "Southern South America": 	"https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/ssa/GEOCOLOR/latest.jpg"}


url = source_dict["Himawari-8"]

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
