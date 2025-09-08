FROM python:3.13-bookworm

RUN useradd -ms /bin/bash speech-service

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt upgrade -y
RUN apt install curl -y

ENV LANG=C.UTF-8

USER speech-service
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./src /app

RUN python3 download_models.py

CMD ["python3", "-m", "fastapi", "run", "app.py"]
