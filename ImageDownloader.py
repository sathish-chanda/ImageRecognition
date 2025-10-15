# Getting the URL of the image
from duckduckgo_search import DDGS
from fastcore.all import *

# Downloading the imaage from the URL
from fastdownload import download_url

from fastai.vision.all import *

# saving lot of images
import time

def search_images(keywords,max_images = 200): 
    return L(DDGS().images(keywords,max_results = max_images)).itemgot('image')

searches = ['dog','cat']

path = Path('images')

for search in searches:
    dest = (path/search)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest,urls=search_images(f'{search} photo'))
    time.sleep(5)
    resize_images(path/search,max_size=400,dest=path/search)

# Validate the images
failed = verify_images(get_image_files(path))
failed.map(Path.unlink)