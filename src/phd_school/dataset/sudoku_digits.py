from torch.utils.data import Dataset
from pathlib import Path

from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw

# import glob
# import random

# import base64
# import io

import pandas as pd

class SudokuDigits(Dataset):
    """
    Manually extracted sudoku digits from actual scanned pages
    """

    
    def __init__(self, csv_path, transform=None):
        """"""
        self.transform = transform
        
        self.csv_path = csv_path
        
        self.df = pd.read_csv(csv_path)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):

        img = Image.open(Path(self.csv_path).parent / self.df['path'][idx])
        target = int(self.df['target'][idx])

        if self.transform:
            img = self.transform(img)

        return img, target