import os
from app.organizer.handler import handler

def created(src):
    ext = os.path.splitext(src)[1].lower()
    handler(src, ext)
    
    
    