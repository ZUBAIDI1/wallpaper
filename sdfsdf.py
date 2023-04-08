import ctypes
import requests
from io import BytesIO
from PIL import Image

# Function to set wallpaper
def set_wallpaper_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img_path = 'cat_wallpaper.jpg'
    img.save(img_path, 'JPEG')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, 3)

# URL of the cat picture
url = 'https://cataas.com/cat'

# Create a simple GUI with a button to set the wallpaper
import tkinter as tk

root = tk.Tk()

def set_wallpaper():
    set_wallpaper_from_url(url)

button = tk.Button(root, text='Set Wallpaper', command=set_wallpaper)
button.pack()

root.mainloop()
