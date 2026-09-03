import os
import getpass
import shutil
import FileExtensions



def extensions_checker(file_name: str, extensions: list) -> bool:
    """Checks to see if file_name ends with one of the file extensions from the given list"""
    for extension in extensions:
        if file_name.endswith(extension):
            return True
    return False


def validate_directory(directory_path: str, directory_name: str) -> None:
    """Checks to see if the directory path is valid"""
    # directory_name is used so that if the directory does not exist,
    # it tells the user which name has caused the error
    if os.path.isdir(directory_path):
        pass # directory does exist, so exit from function
    else:
        print(f"An error has occured, your {directory_name} folder should be here and have this name: {directory_path}")
        raise SystemExit 


user_name = getpass.getuser() 

path = f"/home/{user_name}/Downloads"

validate_directory(path, "Downloads")

os.chdir(path) # change the current directory to the downloads folder

# create the path for the target directories and validate them

doc_folder = f"/home/{user_name}/Documents"
pictures_folder = f"/home/{user_name}/Pictures"
music_folder = f"/home/{user_name}/Music"

validate_directory(doc_folder, "Documents")
validate_directory(pictures_folder, "Pictures")
validate_directory(music_folder, "Music")


missing_extensions = [] # stores what files could not be moved


# loop through each file in the downloads folder
for file in os.listdir(path):

    # if a directory is found, move it to the documents folder
    if os.path.isdir(file):
        path_to_file = f"/home/{user_name}/Downloads/{file}"
        shutil.move(path_to_file, doc_folder)

    elif extensions_checker(file, FileExtensions.doc_file_extensions): # file extension was a document
        path_to_file = f"/home/{user_name}/Downloads/{file}"
        shutil.move(path_to_file, doc_folder)

    elif extensions_checker(file, FileExtensions.picture_file_extensions): # file extension was a picture
        path_to_file = f"/home/{user_name}/Downloads/{file}"
        shutil.move(path_to_file, pictures_folder)

    elif extensions_checker(file, FileExtensions.music_file_extensions): # file extension was music 
        path_to_file = f"/home/{user_name}/Downloads/{file}"
        shutil.move(path_to_file, music_folder) 

    else:
        missing_extensions.append(file) # file extension was not included in FileExtensions.py

# display files whose extensions were not included in the code

for file in missing_extensions:
    print(file)

print("\nSorry, the above file extensions were not recognised")
print("Please submit an issue on the GitHub page, I may be able to add it.")
print("Alternatively, you can add the extension yourself, and submit a pull request on Github\n")

