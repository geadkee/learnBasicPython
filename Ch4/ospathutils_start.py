#
# Example file for working with os.path module
#
from distutils.text_file import TextFile
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  print("File exists: ", str(path.exists("textfile.txt")))
  print("It is a File: ", path.isfile("textfile.txt"))
  print("It is a Directory: ", path.isdir("textfile.txt"))

  # Work with file paths
  print("Item's path: ", path.realpath("txtfile.txt"))
  print("Item's path & name: ", path.split(path.realpath("txtfile.txt")))
  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  md = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("It has been ", md, "since the file was modified..")
  print("or, ", md.total_seconds(), " seconds")

  
if __name__ == "__main__":
  main()
