from watchdog.events import FileSystemEventHandler
from app.organizer.organizer import created
class Sniffer(FileSystemEventHandler):
    def on_created(self, event): 
        src = event.src_path
        print(f"File created: {src}")
        created(src)
        
    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")
    
    def on_modified(self, event):
        print(f"File modified: {event.src_path}")
        
    
    