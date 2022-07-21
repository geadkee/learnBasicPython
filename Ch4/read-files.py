#
# Read and write files using the built-in Python file methods
#

def main():

    myfile = open("textfile.txt", "r")
    if myfile.mode == "r":              #to check if the file is being opened correctly
        readContents = myfile.read()
        print(readContents)








if __name__ == "__main__":
    main()