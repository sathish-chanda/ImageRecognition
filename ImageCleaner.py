from fastcore.all import *
from fastai.vision.all import *
import time

path = Path('images')

badImages = verify_images(get_image_files(path))
badImages.map(Path.unlink)
print("Bad Images Count: " + str(len(badImages)))