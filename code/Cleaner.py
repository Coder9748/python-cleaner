# calls the main functions for the different operating systems depending on the users operating system

import platform
import Linux
import MacOS
import Windows

user_OS = platform.system()

if user_OS == "Linux":
    Linux.main()

elif user_OS == "Darwin":
    MacOS.main()

elif user_OS == "Windows":
    Windows.main()

else:
    print(f"Sorry, your operating system {user_OS} is not supported.")


