#
# Example file for working with functions
#

# define a basic function
def function1():
    print("A basic function.");


# function that takes arguments
def function2(r):
    total = 5 + r;
    print(total);
    

# function that returns a value
def function3(s, t):
    total = s + t;
    return(print(total));
    # return s + t;


# function with default value for an argument
def function4(p, q = 1):
    result = 1;
    for i in range(q):
        result = result + q;
    return result;

def function5(p, q = 1):
    result = 1;
    for i in range(q):
        result = result * p;
    return result;


#function with variable number of arguments
def function6(*arg):
    result = 0;
    for i in arg:
        result = result + i;
    return result;

# function1();
# print(function1());
# print(function1);

# function2(6);
# function3(3, 7);
# print(function3(3, 7));

print(function4(4));
print(function4(4, 5));

print(function5(4, 5));

print(function6(4, 5, 10, 4, 10));