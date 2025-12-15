import numpy as np
from PIL import Image

def load_image(path):
    img = Image.open(path).convert("L")
    return np.array(img, dtype=np.float32)/255.0

def save_image(array, path):
    arr = np.clip(array*255,0,255).astype(np.uint8)
    Image.fromarray(arr).save(path)

def upsample_nearest(img, s):
    h, w = img.shape
    out = np.zeros((h*s, w*s))
    for i in range(h):
        for j in range(w):
            out[i*s:(i+1)*s, j*s:(j+1)*s] = img[i,j]
    return out
