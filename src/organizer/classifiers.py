#**classify_by_type(file)** → Return folder name (e.g., `Images`, `Documents`).
# **classify_by_size(file)** → Sort by thresholds: Small / Medium / Large.
# **classify_by_date(file)** → Group by creation date (e.g., `2025-11`).
import os
from datetime import datetime

def get_default_extension_map():
    """Return default mapping of file extensions to categories."""
    return {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
        "Others": []  # fallback
    }
 
def get_default_size_thresholds():
    """Return default file size thresholds in bytes."""
    return {
        "small": 1 * 1024 * 1024,        # < 1 MB 1 KB = 1024 bytes  megabyte  means 1 MB = 1024 KB.
        "medium": 100 * 1024 * 1024,     # < 100 MB  
        "large": float("inf")            # >= 100 MB
    }

def classify_by_type(file_info):
    """Return category name based on file extension."""
    extension = file_info["ext"].lower()
    print(extension)
    ext_map = get_default_extension_map()
    for category in ext_map:
        print()
        if extension in ext_map[category]:
            return category
    return "Others"

def classify_by_size(file_info):
    size= file_info["size"]
    thresholds = get_default_size_thresholds()
    if size <= thresholds["small"]:
        return "small"
    elif size <= thresholds["medium"]:
        return "medium"
    else:
        return "large"
    
def classify_by_date(file_info):
    date = file_info["ctime"]
    strTime = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    listTime = strTime.split(" ")
    return str(listTime[0])
