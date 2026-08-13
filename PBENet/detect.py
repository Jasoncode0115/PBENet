import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO



if __name__ == '__main__':
    # model = YOLO('runs/train/weights/best.pt') # select your model.pt path
    model = YOLO(r'xxxxxx') # select your model.pt path

    # model.predict(source= r'XXXXXX',
    model.predict(source= r'xxxxxx',

                  imgsz=640,
                  project=r'xxxxxx',
                  name='exp',
                  save=True,
                )