import sys

try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("Error: Invalid input.")
  sys.exit(1)

try:
  result = x/y
except ZeroDivisionError:
  print("Error: Cannot divide by 0.")
  sys.exit(1) # exit the program with code 1


print (f"{x} / {y} = {result}")

# instead of letting the program crash, try and except is able to handle the error nicely, display a nice erro message to the user