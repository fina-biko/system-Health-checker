import os
import logging
from utilites.create_logger import create_logger

logger=logging.basicConfig(level=logging.INFO)

# lists the files and folders structure and creates them
root="src"


files=[
f".gitignore",
f"app.py",
f"requirements.txt",
f"Readme.md",


f"src/__init__.py",

f"src/system_health/__init__.py",
f"src/system_health/cpu.py",
f"src/system_health/memory.py",
f"logs/app.log",
f"utilites/create_logger.py",
f"utilites/exception.py",
f"utilites/__init__.py"

]




folders=[f"src",
         f"src/system_health",
         f"utilites",
         f"logs"]


def create_directories(path):
    """
    creates directories and files where they are non existent 
    and skips where they are existent

    args: None

    returns: created files and folders
    returns None if the files and folders are present
    
    
    """
    for dir in folders:
        
        try:
            os.makedirs(dir,exist_ok=True)
        except Exception as e:
            raise e
        
def create_files(path):
    log=create_logger()
    for file in files:
        if not(os.path.exists(file) ) or os.path.getsize(file==0):
            with open (file, "w") as f:
                
                #once we create the logger object, we call the info method to log messages
                log.info("logger created successfully")
                pass
        else:
            log.error(f" {file} already exists")

          


if __name__ == "__main__":
    create_directories(folders)
    create_files(files)
