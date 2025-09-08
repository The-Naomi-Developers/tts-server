"""
Copyright (C) 2025 The-Naomi-Developers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from fastapi import FastAPI, responses
from pydantic import BaseModel
from speech_service import MODELS_TYPE, VALID_MODELS, text_to_speech


class SpeechRequest(BaseModel):
    model: MODELS_TYPE
    text: str

app = FastAPI()

@app.get("/models")
async def models():
    return {"models": VALID_MODELS}

@app.post("/tts")
async def tts(req: SpeechRequest):
    _ = await text_to_speech(req.text, req.model)

    return responses.Response(
        _,
        media_type="audio/wav"
    )
