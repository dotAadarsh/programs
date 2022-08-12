# To delete a file, you must import the OS module, and run its os.remove() function

import os

# To avoid getting an error, you might want to check if the file exists before you try to delete it
if os.path.exists("nodeletefile.txt"):
    os.remove("nodeletefile.txt")
else:
    print("The file doesnot exist")


os.remove("deletefile.txt") # Remove the file "deletefile.txt"

# To delete an entire folder, use the os.rmdir() method

'''
os.rmdir("FileHandling")
'''