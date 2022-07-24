#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
import zipfile

def main():
  # make a duplicate of an existing file
  if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    source = path.realpath("textfile.txt")
    print(source)
    
    # # let's make a backup copy by appending "bak" to the name
    # destination = source + ".bak"
    # shutil.copy(source, destination)
    
    # # copy over the permissions, modification times, and other info

    
    # # rename the original file
    # os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    root_dir, tail = path.split(source)
    shutil.make_archive("archieveChp4Folder", "zip", root_dir)


    # more fine-grained control over ZIP files

      
if __name__ == "__main__":
  main()
