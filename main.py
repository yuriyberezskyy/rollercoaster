print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride roalercoaster!")
  age = int(input("What is your age?"))
  if age > 18:
    print("You need to pay 15$")
  elif age>12 & age<=18:
    print("You need to pay 12")
  else:
    print("You need to pay 7$")
else:
  print("You can't ride roalercoaster!!!")

