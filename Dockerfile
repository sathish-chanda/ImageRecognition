FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    python3 \
    python3-pip \
    python3-dev \ 
    build-essential \ 
    ca-certificates \ 
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \ 
    libxft-dev \ 
    libgl1-mesa-glx \ 
    && apt-get clean

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install --upgrade pip

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install fastai

RUN pip install jupyter matplotlib pandas 

RUN pip install -U duckduckgo_search==5.3.1b1

RUN pip install nano

RUN pip install nbdev

RUN pip install gradio

WORKDIR /workspace

EXPOSE 8888

EXPOSE 7860

CMD ["jupyter","notebook","--ip=0.0.0.0","--port=8888","--allow-root","--no-browser"]
