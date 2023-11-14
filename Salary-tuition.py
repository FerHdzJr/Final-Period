while True:
  s=input("Is there a seller?\n")
  s=s.lower()
  if s=="no":
    break
  name=input("What is your name?\n")
  x=int(input("Which is your base salary?\n"))
  y=int(input("How much you have sold?\n"))
  if y<3500:
    x=x+x*0.07
  elif y<=7000:
    x=x+x*0.1
  else:
    x=x+x*0.15
  print("The salary of", name, "is: $"+str(x))
