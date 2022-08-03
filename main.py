print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride roalercoaster!")
  age = int(input("What is your age?"))
  if age > 18:
    print("You need to pay 15$")
    bill+= 15
  elif age>12 and age<=18:
    print("You need to pay 12")
    bill+= 12
  elif age >= 45 and age <=55:
    print("Everything is okay. Free ride on us")
  else:
    print("You need to pay 7$")
    bill+= 7

  wants_photo = input("Do you want a photo taken? Y or N.")

  if wants_photo == "Y":
    print("We added 3$ to your bill")
    bill+=3

  print(f"Your final bill is {bill}")
else:
  print("You can't ride roalercoaster!!!")

