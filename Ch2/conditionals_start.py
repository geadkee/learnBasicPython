#
# Example file for working with conditional statements
#

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
    result = "equal" if x == y else "not equal";
    print(result);

    # match-case makes it easy to compare multiple values
    match y:
        case "one":
            result = 1;
        case "two":
            result = 2;
        case "three" | "four":
            result = (3, 4);
        case 5 | 6:
            result = ("five", "six");
        case _:
            result = "can't detect, out of bounds"
    print(result);


if __name__ == "__main__":
    main(3, 5)
