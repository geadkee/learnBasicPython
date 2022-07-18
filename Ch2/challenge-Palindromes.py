def isPalindrome(x):
    
    xy = ""
    for y in x:
        if y.isalnum():
            xy += y

            if xy == xy[::-1]:
                return True
            else:
                return False

run = True

while (run):
    x = input("Enter ur palindrome or 'exit' to exit: ").lower()

    if x == "exit":
        run = False
        break

    isPalindrome(x)


# print(isPalindrome());