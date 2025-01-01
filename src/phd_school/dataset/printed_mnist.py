from torch.utils.data import Dataset

import torch

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import glob
import random

import base64
import io


class AddSPNoise(object):
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, tensor):
        sp = (torch.rand(tensor.size()) < self.prob) * tensor.max()
        return tensor + sp

    def __repr__(self):
        return self.__class__.__name__ + "(prob={0})".format(self.prob)


class AddGaussianNoise(object):
    def __init__(self, mean=0.0, std=1.0):
        self.mean = mean
        self.std = std

    def __call__(self, tensor):
        return tensor + torch.randn(tensor.size()) * self.std + self.mean

    def __repr__(self):
        return self.__class__.__name__ + "(mean={0}, std={1})".format(
            self.mean, self.std
        )


class PrintedMNIST(Dataset):
    """Generates images containing a single digit from font"""

    def __init__(self, N, random_state, transform=None):
        """"""
        self.N = N
        self.random_state = random_state
        self.transform = transform

        fonts_folder = "../fonts"

        # self.fonts = ["Helvetica-Bold-Font.ttf", 'arial-bold.ttf']
        self.fonts = glob.glob(fonts_folder + "/*.ttf")

        random.seed(random_state)

    def __len__(self):
        return self.N

    def __getitem__(self, idx):

        color = random.randint(200, 255)

        # Generate image
        img = Image.new("L", (256, 256))
        
        target = random.randint(0, 9)

        size = random.randint(230, 250)
        x = random.randint(50, 70)
        y = random.randint(15, 25)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(random.choice(self.fonts), size)
        draw.text((x, y), str(target), color, font=font)

        img = img.resize((28, 28), Image.BILINEAR)

        if self.transform:
            img = self.transform(img)

        return img, target


import pandas as pd

def base64ToPIL(x):
	return Image.open(io.BytesIO(base64.b64decode(x.encode())))

class ManyFontsDigits(Dataset):
    
    def __init__(self, csv_path, transform=None):
        """"""
        self.transform = transform
        
        self.df = pd.read_csv(csv_path, header=None, names=['font', 'target', 'base64'])

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        img = base64ToPIL(self.df['base64'][idx])
        target = int(self.df['target'][idx])

        if self.transform:
            img = self.transform(img)

        return img, target