# print out the numbers 1 - 10

counter = 1
while(counter <= 10): # or (counter < 11)
  print(counter)
  counter += 1

# print out all even numbers between 0 - 20

counter = 2
while(counter <= 20):
  print(counter)
  counter += 2

# ask the user for a number
# print all the numbers up to the user's number starting at 1

y = int(input("Tell me a number: "))

counter = 1
while(counter <= y):
  print(counter)
  counter += 1

#while () :
#  if (condition)
#    print

counter = 1
while(counter <= 20):
  if(counter % 2 == 0):
    print(counter)
  counter += 1

# print all the numbers between 1-100 that are divisible by 3 or 7
# BUT NOT BOTH

counter = 3
while(counter <= 100):
  if(counter % 3 == 0 or counter % 7 == 0):
    if(counter % 3 != counter % 7):
      print(counter)
  counter += 1

# print all the numbers between 1 - 100
# if the number is divisible by 3, print out "Fizz"
# if the number is divisible by 5, print out "Buzz"
# if the number is divisible by BOTH, print out "FizzBuzz"
# if the number isn't divisble by any, print out the number

counter = 1
while(counter <= 100):
  if(counter % 5 == 0 and counter % 3 == 0):
    print("FizzBuzz")
  elif(counter % 5 == 0):
    print("Buzz")
  elif(counter % 3 == 0):
    print("Fizz")
  print(counter)
  counter += 1
