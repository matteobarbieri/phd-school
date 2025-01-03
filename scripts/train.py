from phd_school.models.lightning import LitClassification, ClassificationData
import lightning as L

from lightning.pytorch.loggers import WandbLogger

import fire

def train(max_epochs: int = 15):

    model = LitClassification()
    data = ClassificationData()

    wandb_logger = WandbLogger(log_model="all")
    trainer = L.Trainer(max_epochs=max_epochs, logger=wandb_logger)
    trainer.fit(model, data)

if __name__ == '__main__':
    fire.Fire(train)