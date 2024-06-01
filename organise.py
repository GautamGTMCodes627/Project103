import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/gautammahesh/Downloads/P102_assets-main"
to_dir = "/Users/gautammahesh/Downloads/documents"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    #print(name)
   # print(ext)
    if ext==" ":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        pathone = from_dir+'/'+file_name
        pathtwo = to_dir+'/'+"document_files"
        paththree = to_dir+'/'+"document_files"+'/'+file_name
        #print("pathone", pathone)
        #print("paththree", paththree)
        if os.path.exists(pathtwo):
            print("moving "+file_name+" ...")
            shutil.move(pathone, paththree)
        else: 
            os.makedirs(pathtwo)
            print('moving '+file_name+" ...")
            shutil.move(pathone,paththree)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey,{event.src_path} has been created")
    def on_deleted(self,event):
        print(f"Oops, someone deleted{event.src_path}!")
    def on_modified(self,event):
        print(f"Someone modified{event.src_path}.")
    def on_moved(self,event):
        print(f"Someone moved{event.src_path}...")

#Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()