from phd_school.models.lightning import LitClassification, ClassificationData
import lightning as L

from lightning.pytorch.loggers import WandbLogger



def main():

    model = LitClassification()
    data = ClassificationData()

    wandb_logger = WandbLogger(log_model="all")
    trainer = L.Trainer(max_epochs=2, logger=wandb_logger)
    trainer.fit(model, data)

    model = LitClassification.load_from_checkpoint("best_model.ckpt")
    
if __name__ == '__main__':
    main()
