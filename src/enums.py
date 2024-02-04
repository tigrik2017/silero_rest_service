from enum import Enum

class ModelName(str, Enum):
    v4ru = "v4_ru.pt"
    v31ru = "v3_1_ru.pt"

class SampleRate(str, Enum):
    bit8000 = 8000
    bit24000 = 24000
    bit48000 = 48000
    
class Speakrs(str, Enum):
    aidar = "aidar"
    baya = "baya"
    kseniya = "kseniya"
    xenia = "xenia"
    eugene = "eugene"
    random = "random"