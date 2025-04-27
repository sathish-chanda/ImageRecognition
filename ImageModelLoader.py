from fastcore.all import *
from fastai.vision.all import *
import time

# learn = Learner.load('ImageLearner.pkl')
learn = load_learner('ImageLearner.pkl')

# Testing the model
imageFile = 'test-images/bird.jpg' 
pred_class,pred_idx,probs = learn.predict(PILImage.create(imageFile))
print(f"Predicted: {pred_class}, Probability: {probs[pred_idx]:.4f}")
Image.open(imageFile).to_thumb(256,256)

imageFile = 'test-images/forest.jpg' 
pred_class,pred_idx,probs = learn.predict(PILImage.create(imageFile))
print(f"Predicted: {pred_class}, Probability: {probs[pred_idx]:.4f}")
Image.open(imageFile).to_thumb(256,256)

imageFile = 'test-images/cat.jpg' 
pred_class,pred_idx,probs = learn.predict(PILImage.create(imageFile))
print(f"Predicted: {pred_class}, Probability: {probs[pred_idx]:.4f}")
Image.open(imageFile).to_thumb(256,256)

imageFile = 'test-images/horse.jpg' 
pred_class,pred_idx,probs = learn.predict(PILImage.create(imageFile))
print(f"Predicted: {pred_class}, Probability: {probs[pred_idx]:.4f}")
Image.open(imageFile).to_thumb(256,256)

imageFile = 'test-images/ant.jpg' 
pred_class,pred_idx,probs = learn.predict(PILImage.create(imageFile))
print(f"Predicted: {pred_class}, Probability: {probs[pred_idx]:.4f}")
Image.open(imageFile).to_thumb(256,256)