#
# Example file for learning execptions
#

# Errors can hapen in programs, and wee need a clean way to handle them
# TODO: this code will cause an error, because we can't devide ZERO
x = 10/0


# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    y = 10/0
except:
    print("Well, it doesn't work.")


# TODO: You can also catch specific exceptions
try:
    answer = input("Please tell me number can be divided by 10. ")
    numAns = int(answer)
    print(10/numAns)

except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("Please insert an appropriate answer!")
    print(e)
finally:
    # in "finally", we can end the execution of the process, or 
    # close the opened files used throughout the whole process.
    print("This code always runs.")

