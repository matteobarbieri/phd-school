# from phd_school.dataset import PrintedMNIST, AddGaussianNoise, AddSPNoise, ManyFontsDigits
from phd_school.dataset import AddSPNoise, ManyFontsDigits
from phd_school.dataset.sudoku_digits import SudokuDigits

from torchmetrics.classification import Accuracy

import torch
from timm import create_model
from torchvision import transforms, datasets
import lightning as L
import torch.nn as nn

train_transform = transforms.Compose([
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    # AddGaussianNoise(0, 1.0),
    AddSPNoise(0.1),
])

val_transforms = transforms.Compose([transforms.ToTensor()])


class LitClassification(L.LightningModule):
    def __init__(self, lr: float = 0.001):
        super().__init__()
        # self.model = create_model('resnet34', num_classes=10)
        self.model = create_model('resnet101', num_classes=10)

        self.lr = lr

        # Replace 1st layer to use it on grayscale images
        self.model.conv1 = nn.Conv2d(
            1,
            64,
            kernel_size=(7, 7),
            stride=(2, 2),
            padding=(3, 3),
            bias=False,
        )

        
        self.loss_fn = torch.nn.CrossEntropyLoss()

        self.accuracy = Accuracy(task="multiclass", num_classes=10)

    def training_step(self, batch):
        images, targets = batch
        outputs = self.model(images)
        loss = self.loss_fn(outputs, targets)
        
        _, y_hat = torch.max(outputs, dim=1)
        acc = self.accuracy(y_hat, targets)

        self.log("train_loss", loss)
        self.log("train_acc", acc)

        return loss

    def validation_step(self, batch):
        images, targets = batch
        outputs = self.model(images)
        loss = self.loss_fn(outputs, targets)

        _, y_hat = torch.max(outputs, dim=1)
        acc = self.accuracy(y_hat, targets)

        self.log("val_acc", acc)

        self.log("val_loss", loss)
        return loss

    def forward(self, x):
        return self.model(x)
        

    def configure_optimizers(self):
        return torch.optim.AdamW(self.model.parameters(), lr=self.lr)
    
    
class ClassificationData(L.LightningDataModule):

    def train_dataloader(self):
        # train_dataset = ManyFontsDigits("../data/printed_digits.csv", transform=train_transform)
        train_dataset = ManyFontsDigits("home/data/printed_digits.csv", transform=train_transform)
        # train_dataset = PrintedMNIST(320, -666, transform=train_transform)
        
        return torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=7)

    def val_dataloader(self):
        # any iterable or collection of iterables
        val_dataset = SudokuDigits("home/data/sudoku_digits/sudoku_digits.csv", transform=val_transforms)
        return torch.utils.data.DataLoader(val_dataset, num_workers=7)
    