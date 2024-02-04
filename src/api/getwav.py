from fastapi import APIRouter, Query, Response
from config import Config
from enums import ModelName, SampleRate, Speakrs
import os

from utils.model_utils import get_filename, load_model

router = APIRouter()

_config = Config()

@router.get("/getwav", responses={200: {"content": {"audio/wav": {}}}}, response_class=Response)
async def getwav(      
    text_to_speech: str = Query(..., description="Текст для озвучки"),
    model_name: ModelName = Query(..., description="Выбор модели"),
    speaker: Speakrs = Query(default=Speakrs.xenia, description="Спикеры"),
    sample_rate: SampleRate = Query(default=SampleRate.bit24000, description="Выходной битрейт"),
    put_accent: bool = Query(default=True, description="Простановка акцентов в тексте"),
    put_yo: bool = Query(default=True, description="Простановка 'ё' в тексте")

):
    """
       Return WAV file with rendered text\n
       :return: WAV file
    """
    
    global _config
    
    if (model_name != _config.current_model):
        load_model(model_name)
    
    path = _config.model.save_wav(
        text=text_to_speech,
        speaker=speaker.value,
        put_accent=(put_accent==1),
        put_yo=(put_yo==1),
        sample_rate=int(sample_rate.value)
    )

    # перемещаем wav на новое место
    wavfile = get_filename(model_name, speaker, sample_rate)
    if os.path.exists(wavfile):
        os.unlink(wavfile)
    os.rename(path, wavfile)

    in_file = open(wavfile, "rb") # opening for [r]eading as [b]inary
    data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
    in_file.close()

    return Response(content=data, media_type="audio/wav")