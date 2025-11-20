from organizer.file_utils import scan_folder
from organizer.classifiers import classify_by_type, classify_by_size, classify_by_date

def main():
    files = scan_folder(path,False)
    #file = classify_by_type(files[len(files)-1])

    

if __name__ == "__main__":
    main()
