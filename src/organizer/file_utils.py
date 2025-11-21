
#Scan a folder for files
import os
from logs.logger import logger
import shutil

# {
#     "name": "photo.jpg",
#     "path": "C:/Users/Me/Downloads/photo.jpg",
#     "ext": ".jpg",
#     "size": 203451,
#     "ctime": 1730795857.0
# }

def scan_folder(path, include_subfolders=True):
    files = []
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")
    """
    os.walk() is overkill for non-recursive scans — it creates extra generator overhead.
    os.scandir() is faster and cleaner when you only want the current directory.
    """
    if include_subfolders:
        for root, _, filenames in os.walk(path):
            for name in filenames:
                full_path = os.path.join(root, name)
                files.append(get_file_info(full_path))
    else:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(get_file_info(entry.path))

    return files
            
    
    
#Retrieve file metadata (size, extension, creation date)
def get_file_info(file_path):
    """stat() is a Unix system call that queries the file system for metadata about a file"""
    status = os.stat(file_path)
    return {
        "name":os.path.basename(file_path),
        "path":  file_path,
        #Split the extension from a pathname.
        "ext": os.path.splitext(file_path)[1],
        "size": status.st_size,
        "ctime": status.st_mtime
    }

#Move files safely (handle duplicates, permissions, etc.)cd..

def safe_move(src, dest_folder):
    """
    Move a file safely to a destination folder.
    Avoids overwriting by renaming if necessary.
    """
    file_name = os.path.basename(src["path"])
    dest_path = os.path.join(dest_folder, file_name)
    if os.path.exists(dest_path):
         name, ext = os.path.splitext(file_name)
         counter = 1
         while os.path.exists(dest_path):
             new_name = f"{name} ({counter}){ext}"
             dest_path = os.path.join(dest_folder, new_name)
             counter += 1
    try:
        shutil.move(src["path"], dest_path)
        return True, dest_path
    except Exception as e:
        return False, str(e)
    
def format_size(size_bytes):
    """Convert bytes to KB, MB, or GB."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"