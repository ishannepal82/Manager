from watchdog.observers import Observer
from app.sniffer.sniffer import Sniffer

def start_sniffer(path: str):
    event_handler  = Sniffer()
    observer = Observer()
    observer.schedule(event_handler,path, recursive=True)
    observer.start()
    print(f"Started sniffer on path: {path}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()