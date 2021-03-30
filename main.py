from fastapi import FastAPI, HTTPException
from typing import Optional
from model import Song
from model import Podcast
from model import Audiobook

import json

import database as db

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the Audio book API."


@app.put("/create/{type}/")
def insert_song(type: str, meta: dict):
    if (type=='song'):
        temp = Song(meta)
    elif (type=='podcast'):
        temp = Podcast(meta)
    elif (type=='audiobook'):
        temp = AudioBook(meta)

    id = db.insert_file("song", temp.convert_dict())
    return {"id": id}

@app.put("/delete/{type}/{id}")
def delete_item(type: str, id: int):
    db.delete_instance(type, id)
    return {"response": 'Delete successful!'}

@app.put("/update/{type}/{id}")
def update_item(type: str, id: int, meta: dict):
    db.update_instance(type, id, meta)
    return {"response": 'Update successful!'}

@app.put("/get/{type}")
def get_item(type: str, id: int):
    return db.get_instance(type, id)
