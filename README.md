# Image Recognizer

This project is based on the fast ai library. We will be downloading the images from the internet and feed the images to train the model. 

The images will be downloaded into the **images** folder. The images will be downloaded by the script `ImageDownloader.py`. We need to specify what needs to be downloaded in the images folder.

After finishing the download, For sanity check we do the cleanup of downloaded images by running the `ImageCleaner.py`

The training will be done by running the `ImageModelTrainer.py`. It will save the trained model into `ImageLearner.pkl`.

The trainer model will be loaded for testing the **test-images** using the `ImageModelLoader.py`

## Follow the below steps to build the project

1. Docker needs to be installed in the system
2. `clone` this repository
3. `cd` into this project
4. RUN `docker build -t fastai-ubuntu .`
5. RUN `docker run -it --rm -p 8888:8888 -v $(pwd):/workspace fastai-ubuntu`
6. Follow the link which will be shown after running the above step. eg. http://127.0.0.1:8888/tree?token=01439bbc4d873e3d86859f931f870fed2e084bfb8a7f42e4
7. ![alt text](<Screenshot from 2025-04-27 00-52-21.png>)
