import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    with open(event.src_path, "r") as msg:
        contents = msg.read()
        print(f"hey, {contents}!")
    os.remove(event.src_path)
    os.remove(contents)

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created

    path = "/home/joao/source/pythonStreamingUpload/messaging"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()