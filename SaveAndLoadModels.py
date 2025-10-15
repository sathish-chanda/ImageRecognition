from fastcore.all import *
from fastai.vision.all import *
import time

path = Path('images')

dls = DataBlock(
    blocks=(ImageBlock,CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192,method='squish')]
).dataloaders(path, bs=32)

dls.show_batch(max_n=6)

# Training
learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(3)

# Saving the model
learn.export('CatDogClassifierModel.pkl')

# Test
# - Get the test image
img = PILImage.create('test-images/dog.jpg')
img.thumbnail((192,192))
img

# Test the prediction
learn.predict(img)

# Loading the saved model and test it model
catDogLearner = load_learner('CatDogClassifierModel.pkl')
catDogLearner.predict(img)