import os
import getpass
import shutil

def extensions_checker(file_name: str, extensions: list) -> bool:
    """Checks to see if file_name ends with one of the file extensions from the given list"""
    for extension in extensions:
        if file_name.endswith(extension):
            return True
    return False

# change the current directory to the Downloads folder

user_name = getpass.getuser() # type: str

path = f"/home/{user_name}/Downloads"

os.chdir(path)


doc_folder = f"/home/{user_name}/Documents"
pictures_folder = f"/home/{user_name}/Pictures"
music_folder = f"/home/{user_name}/Music"


doc_file_extensions = []
picture_file_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
music_file_extensions = []


# loop through the downloads folder

for file in os.listdir(path):
    # look at the file extension and move to the correct folder 
    if extensions_checker(file, doc_file_extensions):
        path_to_file = f"/home/{user_name}/Downloads/{file}"
        shutil.move(path_to_file, doc_folder)
    
