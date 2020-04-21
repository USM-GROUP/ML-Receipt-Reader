import os

from c_point import point
import functions as func

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./config/vision_config.json"

func.detect_text('./images/receipt.jpg')