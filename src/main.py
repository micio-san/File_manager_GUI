from organizer.core import organize_folder
from tkinter import *

m = Tk()
m.title("Folder Organizer")
m.geometry("500x300")

type_set = StringVar()
type_set.set("type")

def set_type():
    print("Selected mode:", type_set.get())

Label(m, text="Enter folder path:").pack()
path_input = Entry(m, width=50)
path_input.pack(pady=10)

Radiobutton(m, text="Type", value="type", variable=type_set, command=set_type).pack()
Radiobutton(m, text="Size", value="size", variable=type_set, command=set_type).pack()
Radiobutton(m, text="Date", value="date", variable=type_set, command=set_type).pack()

def on_organize():
    folder_path = path_input.get()
    mode = type_set.get()
    print("Folder:", folder_path)
    print("Mode:", mode)

    organize_folder(folder_path, False, mode)

button = Button(
    m,
    text="Organize!",
    width=20,
    height=3,
    background="red",
    command=on_organize
)
button.pack(pady=15)

def main():
    m.mainloop()

if __name__ == "__main__":
    main()
