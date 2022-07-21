#
# Read and write files using the built-in Python file methods
#

def main():

    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+")      #"a" == append data to the file

    for i in range(10):
        myfile.write("new Lane " + str(i) + "\n")

    myfile.close()



if __name__ == "__main__":
    main();