import calendar
from logging import config
import time
import torch
import os
from config import Config
from enums import ModelName, SampleRate, Speakrs

def load_model(model_name: ModelName):
    _config = Config()
    if _config.generations_root != model_name:
        _config.current_model = model_name
        modelurl = 'https://models.silero.ai/models/tts/ru/' + model_name.value

        torch.set_num_threads(1)
        local_file = f'{_config.models_root}/{model_name.value}'

        if not os.path.isfile(local_file):
            print("Downloading Silero model...")
            torch.hub.download_url_to_file(modelurl, local_file)

        _config.model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        _config.model.to(_config.device)
        print(f"Model {model_name} loaded")


def get_filename(model: ModelName, speaker: Speakrs, bitrate: SampleRate):
    _config = Config()
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    modelname = os.path.splitext(model.value)[0]
    return f'{_config.generations_root}/{modelname}-{speaker.value}-{bitrate.value}-{ts}.wav'
