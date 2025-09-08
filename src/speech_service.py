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
from typing import Literal
from asyncio import to_thread
from json import load
from io import BytesIO
from piper import PiperVoice
from wave import open as wav_open
import onnxruntime

onnxruntime.preload_dlls()

with open("./models.json") as fp:
    MODELS = load(fp)

MODELS_TYPE = Literal["ru_ruslan", "en_ryan"]

VALID_MODELS = list(MODELS.keys())

# model_name -> PiperVoice
states: dict[str, PiperVoice] = {}

def _text_to_speech(text: str, model: str):
    state = states.get(model)

    if not state:
        state = PiperVoice.load(
            MODELS[model][0],
            use_cuda=cuda_version != ''
        )
        states[model] = state

    file_io = BytesIO()

    with wav_open(file_io, "wb") as fp:
        state.synthesize_wav(text, fp)

    file_io.seek(0)

    return file_io.read()

async def text_to_speech(text: str, model: str):
    return await to_thread(_text_to_speech, text, model)
