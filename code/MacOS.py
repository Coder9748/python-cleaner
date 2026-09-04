# uses MacOS file paths

import os
import getpass
import shutil
import FileExtensions

# Adapted from:
# https://stackoverflow.com/a/69577512
# Original answer by paxdiablo, licensed CC BY-SA 4.0.
# Modified for checking file extensions and added type hints/documentation.


def extensions_checker(file_name: str, extensions: list) -> bool:
    """
    Checks to see if file_name ends with one of the file extensions
    from the given list
    """
    for extension in extensions:
        if file_name.endswith(extension):
            return True
    return False


def validate_directory(directory_path: str, directory_name: str) -> bool:
    """Checks to see if the directory path is valid"""
    # directory_name is used so that if the directory does not exist,
    # it tells the user which name has caused the error

    # directory does exist
    if os.path.isdir(directory_path):
        return True
    else:
        print(f"An error has occured, your {directory_name} folder should be "
              "here and have this name: {directory_path}")
        return False


def main():
    """Main function of Linux.py"""
    user_name = getpass.getuser()

    path = f"/Users/{user_name}/Downloads"

    validate_directory(path, "Downloads")

    # change the current directory to the downloads folder
    os.chdir(path)

    # create the path for the target directories and validate them
    # stops the code if any directories are invalid

    doc_folder = f"/Users/{user_name}/Documents"
    pictures_folder = f"/Users/{user_name}/Pictures"
    music_folder = f"/Users/{user_name}/Music"

    if not validate_directory(doc_folder, "Documents"):
        raise SystemExit

    if not validate_directory(pictures_folder, "Pictures"):
        raise SystemExit

    if not validate_directory(music_folder, "Music"):
        raise SystemExit

    # stores what files could not be moved
    missing_extensions = []

    # loop through each file in the downloads folder
    for file in os.listdir(path):

        # if a directory is found, move it to the documents folder
        if os.path.isdir(file):
            path_to_file = f"/Users/{user_name}/Downloads/{file}"
            shutil.move(path_to_file, doc_folder)

        # file extension was a document
        elif extensions_checker(file, FileExtensions.doc_file_extensions):
            path_to_file = f"/Users/{user_name}/Downloads/{file}"
            shutil.move(path_to_file, doc_folder)

        # file extension was a picture
        elif extensions_checker(file, FileExtensions.picture_file_extensions):
            path_to_file = f"/Users/{user_name}/Downloads/{file}"
            shutil.move(path_to_file, pictures_folder)

        # file extension was music
        elif extensions_checker(file, FileExtensions.music_file_extensions):
            path_to_file = f"/Users/{user_name}/Downloads/{file}"
            shutil.move(path_to_file, music_folder)

        # file extension was not included in FileExtensions.py
        else:
            missing_extensions.append(file)

    # display files whose extensions were not included in the code
    if len(missing_extensions) >= 1:
        # checks if there were missing file extensions
        for file in missing_extensions:
            print(file)

        print("\nSorry, the above file extensions were not recognised")
        print("Please submit an issue on the GitHub page, "
              "I may be able to add it.")
        print("Alternatively, you can add the extension yourself, "
              "and submit a pull request on Github\n")
