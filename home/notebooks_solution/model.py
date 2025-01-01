from phd_school.dataset import PrintedMNIST, AddGaussianNoise, AddSPNoise, ManyFontsDigits

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


# DEFAULT_TRANSFORM = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Resize((224, 224)),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])

class LitClassification(L.LightningModule):
    def __init__(self):
        super().__init__()
        # self.model = create_model('resnet34', num_classes=10)
        self.model = create_model('resnet101', num_classes=10)



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

    def training_step(self, batch):
        images, targets = batch
        outputs = self.model(images)
        loss = self.loss_fn(outputs, targets)
        self.log("train_loss", loss)
        return loss

    def forward(self, x):
        return self.model(x)
        

    def configure_optimizers(self):
        return torch.optim.AdamW(self.model.parameters(), lr=0.005)
    
    
class ClassificationData(L.LightningDataModule):

    def train_dataloader(self):
        ManyFontsDigits
        train_dataset = ManyFontsDigits("../data/printed_digits.csv", transform=train_transform)
        # train_dataset = PrintedMNIST(320, -666, transform=train_transform)
        
        return torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=5)
    