from fastcore.all import *
from fastai.vision.all import *
import time
import gradio as gr

learn = load_learner('CatDogClassifierModel.pkl')

categories = ('Dog','Cat')

def classify_image(im):
    pred,idx,probs = learn.predict(im)
    return dict(zip(categories,map(float,probs)))

image = gr.Image(height=192,width=192)
label = gr.Label()
examples = ['cat.jpg','dog.jpg']

intf = gr.Interface(fn=classify_image, inputs = image, outputs = label, examples = examples)
intf.launch(inline=False)
