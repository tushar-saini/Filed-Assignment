from pydantic import BaseModel
from datetime import date
from typing import Optional

class Song:
    id: int
    name: str
    duration: int
    uploadtime: date

    def __init__(self, meta):
        self.id = meta['id']
        self.name = meta['name']
        self.duration = meta['duration']
        self.uploadtime = meta['uploadtime']


    def convert_dict(self):
        dict = {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'uploadtime': str(self.uploadtime)
        }
        return dict

class Podcast(BaseModel):
    id: int
    name: str
    duration: int
    uploadtime: date
    host: str
    participants: Optional[list] = None

    def convert_dict(self):
        dict = {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'uploadtime': str(self.uploadtime),
            'host': self.host,
            'participants': str(self.participants)
        }
        return dict

class Audiobook(BaseModel):
    id: int
    title: str
    author: int
    narrator: str
    duration: int
    uploadtime: date

    def convert_dict(self):
        dict = {
            'id': self.id,
            'title': self.name,
            'author': self.duration,
            'narrator': str(self.uploadtime),
            'duration': self.host,
            'uploadtime': str(self.participants)
        }
        return dict
