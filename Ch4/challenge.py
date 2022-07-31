import os;
from os import  path ;



def main():

    countFile = ("challenge.txt", "w+")

    path1, path2 = path.split(path.realpath("challenge.txt"))

    countFile.write("Byte count: ")



if __name__ == "__main__":
    main()