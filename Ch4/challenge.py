import os;
from os import  path ;



def main():

    countFile = ("challenge.txt", "w+")

    path1, path2 = path.split(path.realpath("challenge.txt"))

    countFile.write("Byte count: ")
    countFile.write("Total listing: \n")
    countFile.write("-------------\n")
    for files in os.listdir():
        countFile.write(files + "\n")



if __name__ == "__main__":
    main()