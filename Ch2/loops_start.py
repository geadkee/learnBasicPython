#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  print("While-Loop")
  while (x < 5):
    print(x);
    # x =+ 1
    x += 1


  # define a for loop
  print("For-Loop")
  for y in range(5, 10):
    print(y);


  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print(d)

  
  # use the break and continue statements
  for x in range(1, 10):
    print(x)
    # if x == 7:
    #   print("before break")
    #   break
    if x % 2 == 0:
      continue
    print(x)


  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print(i, d)

  
if __name__ == "__main__":
  main()
