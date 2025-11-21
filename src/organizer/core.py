import os
from organizer.file_utils import scan_folder,safe_move
from organizer.classifiers import  pick_classification
from logs.logger import logger

def organize_folder(path_folder, check_subfolders, mode="type"):
        """
    Organize files in a folder based on selected mode.
    Modes: 'type', 'size', 'date'
    """
        #check if path exists or not
        if not os.path.exists(path_folder):
                raise FileNotFoundError(f"The addy {path_folder} does not esist")
        
        files= scan_folder(path_folder, check_subfolders)
        results = {"moved": 0, "skipped": 0, "failed": 0, "details": []}
        logger.info(f"\nOrganizing {len(files)} files by {mode}...\n")
        folder_name=""
        for file in files:
             folder_name = pick_classification(file,mode)
             destination_folder= get_destination_folder(path_folder,folder_name)
             success, msg =safe_move(file, destination_folder)

def get_destination_folder(path_folder,folder_name):
        full_path= os.path.join(path_folder, folder_name)
        if not os.path.exists(full_path):
           os.makedirs(full_path, exist_ok=True)
        return full_path

        