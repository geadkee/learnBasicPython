#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  myfile = open("textfile.txt", "w+")       # will overwrite all content in existing file

  # write some lines of data to the file
  for i in range(10):
    myfile.write("Lane "+ str(i)+ "\n");
  
  # close the file when done
  myfile.close()
  
  # Open the file back up and read the contents

    
if __name__ == "__main__":
  main()
