import os
from src import models as net

WEIGHTS_IN_PATH = os.environ.get("WEIGHTS_IN_PATH") # should be the fullpath of the pre-trained weights
IN_HEIGHT = int(os.environ.get("IN_HEIGHT"))
IN_WIDTH = int(os.environ.get("IN_WIDTH"))
LABELS_FILE = os.environ.get("LABELS_FILE")
MODEL = os.environ.get("MODEL")
BACKBONE = os.environ.get("BACKBONE")
is_pretrained = False if os.environ.get("PRE_TRAINED") == "False" else True
with open(LABELS_FILE, 'r') as file:
    CLASSES = len(list(file))
if not CLASSES:
    raise Exception("Unable to load label file")


MODELS = {
    'unet': net.unet(pre_trained=is_pretrained,
                        # weights_path=WEIGHTS_IN_PATH, # uncomment if load pre-trained weights
                        n_classes=CLASSES,
                        input_h=IN_HEIGHT,
                        input_w=IN_WIDTH,
                        model_name=f"{MODEL}_{BACKBONE}"),

    'bcd_unet_d1': net.bcd_unet_d1(pre_trained=is_pretrained,
                                        # weights_path=WEIGHTS_IN_PATH, # uncomment if load pre-trained weights
                                        n_classes=CLASSES,
                                        input_h=IN_HEIGHT,
                                        input_w=IN_WIDTH,
                                        model_name=f"{MODEL}_{BACKBONE}"),
    'bcd_unet_d3': net.bcd_unet_d3(pre_trained=is_pretrained,
                                      # weights_path=WEIGHTS_IN_PATH, # uncomment if load pre-trained weights
                                      n_classes=CLASSES,
                                      input_h=IN_HEIGHT,
                                      input_w=IN_WIDTH,
                                      model_name=f"{MODEL}_{BACKBONE}"),
    }