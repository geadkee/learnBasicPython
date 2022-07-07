#
# Example file for HelloWorld
#

def main(): 
    print("Hello World!!");
    name = input("Whats ur name?");
    print("Nice to meet u, ", name);
    age = input("How old are you?");
    print("So u are ", age, "yrs old, and called ", name);

if __name__ == "__main__":      # for the terminal to check if this program is the right one before executing the function 
    main();
