import shutil
import time
import os
# Move Files to a New Directory
def move_file(src, des):
    time.sleep(0.4)
    
    # Ensure the full name of the path and destinations 
    filename = os.path.basename(src)
    des_path = os.path.join(des, filename)
    shutil.move(src, des_path)
    
def handler(src, ext):
    print(ext)
    if ext == ".txt":
        print("Moving the File to Documents -> Texts!")   
        des = r"C:\Users\Ishan\Desktop\Manager\documents"
        move_file(src,des)
        
    elif ext == ".png":
        print("Moving the File to Pictures !")
        des = r"C:\Users\Ishan\Desktop\Manager\app\pictures"
        move_file(src, des)
        
    elif ext == ".mp4":
        print("Moving the File to Pictures !")
        des = r"C:\Users\Ishan\Desktop\Manager\app\videos"
        move_file(src, des)
        
    elif ext == ".py":
        print("Moving the File to Pictures !")
        des = r"C:\Users\Ishan\Desktop\Manager\app\projects"
        move_file(src, des)
    
    else:
        print("Moving the file to Miscallenous!")
        
