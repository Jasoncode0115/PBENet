import warnings, os

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('xxxxxxx.yaml')

    model.load('xxxxxxx.pt') # loading pretrain weights
    model.train(data='xxxxxxx.yaml',
                epochs=200,
                )