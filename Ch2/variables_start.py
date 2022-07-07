# 
# Example file for variables
#

from xmlrpc.client import boolean


# Declare a variable and initialize it
num = 5;
float1 = 1.45;
string1 = "Collection of characters";
boolean1 = True;
list1 = [1, False, 34.67, "two", 4, "five"];
tuple1 = (0, 1, 2);
dictionary1 = {"one": 1, "two": 2, "three": 33};

print(num);
print(float1);
print(string1);
print(list1);
print(tuple1);
print(dictionary1);


# re-declaring the variable works
num = "abc";
print(num);

# to access a member of a sequence type, []
print(tuple1[1]);
print(list1[2]);

# use slices to access part of the sequence
print(list1[1:4])
print(list1[1:5:2]) #step value of ":2"

# use slices to reverse sequence
print(list1[::-1]) #no specific START & END value, but have "-1" for STEP value


# dictionaries are accessed via keys
print(dictionary1["one"]);


# ERROR: variables of different types cannot be combined
print("String type " + str(123)); # print("String type" + 123);


# Global vs. local variables in functions
def aFunction():
    global string1;
    string1 = "String in function";
    float1 = 5.789;
    print(string1 + str(float1));

aFunction();
print(string1 + str(float1))

# del string1;
# print (string1)

