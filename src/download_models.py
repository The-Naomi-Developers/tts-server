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
from os import system
from speech_service import MODELS

for i in MODELS.keys():
    model_save_path = MODELS[i][0]
    model_download_link = MODELS[i][-1]

    system(f"curl -L '{model_download_link}' -o {model_save_path}")
    
    model_download_link = model_download_link.replace(".onnx", ".onnx.json")
    model_save_path = model_save_path.replace(".onnx", ".onnx.json")

    system(f"curl -L '{model_download_link}' -o {model_save_path}")

