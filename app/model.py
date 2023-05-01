from keras.models import load_model
from efficientnet.tfkeras import EfficientNetB4
import cv2
import numpy as np

def create_datasets(fname, img_width, img_height):
    imgs = []
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img_width, img_height))
    imgs.append(img)
        
    imgs = np.array(imgs, dtype='float32')
    return imgs

def analysis(fname):
    model = load_model('./app/model/model.h5')
    IMG_HEIGHT = 192
    IMG_WIDTH = 256
    #fname="./app/img/0_left.jpg"

    val_img = create_datasets(fname, IMG_WIDTH, IMG_HEIGHT)
    val_img = val_img/255

    preds = model.predict(val_img[0:1])
    idx = -1
    mx = -1
    for i in range(4):
        if mx < preds[0][i]:
            idx = i
            mx = preds[0][i]
    result = [idx,preds[0]]
    return result
