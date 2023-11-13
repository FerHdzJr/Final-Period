"""https://replit.com/join/pqsflmyzky-a00573910"""
grif=0
sly=0
n=int(input("Number of events in the match:\n"))
for i in range(0, n):
  s=input("Enter the event (goal/foul/snitch):")
  x=input("By which team? (Gryffindor or Slytherin)\n")
  x=x.lower()
  if x=="gryffindor":
    if s=="goal":
      grif+=10
    elif s=="foul":
      grif-=30
    else:
      grif+=150
  else:
    if s=="goal":
      sly+=10
    elif s=="foul":
      sly-=30
    else:
      sly+=150

print("Gryffindor:", grif)
print("Slytherin:", sly)
if grif>sly:
  print("Gryffindor wins!!!")
elif sly>grif:
  print("Slytherin wins!!!")
else:
  print("It is a draw")
