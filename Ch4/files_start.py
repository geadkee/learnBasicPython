#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  myfile = open("textfile.txt", "w+")
  
  # Open the file for appending text to the end


  # write some lines of data to the file
  for i in range(10):
    # myfile.write("Lane ", i);
    print("Lane ", i);
  
  # close the file when done

  
  # Open the file back up and read the contents

    
if __name__ == "__main__":
  main()
