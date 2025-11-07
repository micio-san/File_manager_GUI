
#Scan a folder for files
import os
from logs.logger import logger

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
    """Return metadata for a file."""
    status = os.stat(file_path)
    return {
        "name":os.path.basename(file_path),
        "path":  file_path,
        "ext": os.path.splitext(file_path)[1],
        "size": status.st_size,
        "ctime": status.st_mtime
    }

#Move files safely (handle duplicates, permissions, etc.)cd..
