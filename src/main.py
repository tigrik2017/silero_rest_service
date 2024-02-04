
# ----------

import multiprocessing
from fastapi import FastAPI
import uvicorn
from api.getwav import router as wav_router
from utils.model_utils import load_model
from config import Config
from enums import ModelName

app = FastAPI()
app.include_router(wav_router)

version = "0.1"

@app.on_event("startup")
async def startup_event():
    load_model(ModelName.v4ru)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    print("Running silero_rest_service server v{0}...".format(version))
    uvicorn.run("main:app", host="0.0.0.0", port=5010, log_level="info")