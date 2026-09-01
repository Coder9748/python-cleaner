import os
import getpass


# change the current directory to the Downloads folder

user_name = getpass.getuser() # type: str

path = f"/home/{user_name}/Downloads"

doc_folder = ""
pictures_folder = ""
music_folder = ""



print(os.getcwd()) # test code

os.chdir(path)

# loop through the downloads folder

# ---------------- test code

print(os.getcwd())