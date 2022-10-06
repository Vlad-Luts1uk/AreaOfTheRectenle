length = int(input("Length?:"))

width = int(input("Width?:"))

guess = int(input("Guess the are of recangle?:"))

area = length * width

if guess != area:
  print ("wrong")

if guess == area: 
  print ("correct")