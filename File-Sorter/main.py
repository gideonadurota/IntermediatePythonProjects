"""The program sorts files within a folder and its subfolders and sorts them into their respective folders based on their extensions"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog

def create_folder(path: str, extension: str) -> str:
    """Creates folder if it doesn't exist"""
    folder_name:str = extension[1:]
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

def sort_files(source_path: str):
    """Sorts files by button clicking"""

    for root_dir, sub_dirs, files in os.walk(source_path):
        for file in files:
            file_path = os.path.join(root_dir, file)
            extension:str = os.path.splitext(file)[1]

            if extension:
                target_folder:str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, file)

                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str):
    """Removes empty folders"""

    for root_dir, sub_dirs, files in os.walk(source_path, topdown=False):
        for current_dir in sub_dirs:
            folder_path = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                shutil.rmtree(folder_path)

def main():
    #User input using command line input
    # user_input: str = input("Enter the path of the folder you want to sort: ")

    # create a tkinter root window
    root = tk.Tk()

    # hide the main root window
    root.withdraw()

    # user input by selecting folder from the UI
    user_input = filedialog.askdirectory(parent=root)
    if user_input:
        if os.path.exists(user_input):
            sort_files(user_input)
            remove_empty_folders(user_input)
            print("Files sorted successfully!")
        else:
            print("Folder not found")

    else:
        print("Folder not found")

    # destroy the tkinter root window to terminate the application
    root.destroy()

if __name__ == "__main__":
    main()

