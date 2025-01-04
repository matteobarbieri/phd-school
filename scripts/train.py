from phd_school.models.lightning import LitClassification, ClassificationData
import lightning as L

from lightning.pytorch.loggers import WandbLogger

from lightning.pytorch.callbacks import ModelCheckpoint, EarlyStopping

import fire

def train(max_epochs: int = 15, lr=1e-3):

    model = LitClassification(lr=lr)
    data = ClassificationData()

    checkpoint_callback = ModelCheckpoint(dirpath='home/artifacts/', monitor='val_acc', mode='max')
    early_stopping_callback = EarlyStopping(monitor='val_acc', mode='max', patience=3)

    wandb_logger = WandbLogger(log_model="all")
    trainer = L.Trainer(max_epochs=max_epochs, logger=wandb_logger, callbacks=[checkpoint_callback, early_stopping_callback])
    trainer.fit(model, data)

if __name__ == '__main__':
    fire.Fire(train)