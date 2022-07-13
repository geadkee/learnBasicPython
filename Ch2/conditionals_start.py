#
# Example file for working with conditional statements
#


from unittest import result


def main(x, y):

    # conditional flow uses if, elif, else
    if(x < y):
        result = "x less than y"
    elif(x == y):
        result = "x equal y"
    else:
        result = "x greater than y"

    print(result)

    # conditional statements let you use "a if C else b"
    result = "equal" if x ==y else "not equal";
    print(result);

if __name__ == "__main__":
    main()
