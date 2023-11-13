"""https://replit.com/join/vxfjmnnicn-a00573910"""
cnt1=cnt2=cnt3=cnt4=0
n=0
buy=0
while True:
  s=input("Does a client come in?\n")
  s=s.lower()
  if s=="no":
    break
  n+=1
  s=input("Buy something?\n")
  s=s.lower()
  if s=="no":
    continue
  buy+=1
  print("Wands:")
  print("(1)Elder Wand   (2)Hawthorn Wand")
  print("(3)Willow Wand  (4)Holly Wand")
  x=int(input("Which wands he bought? [1, 2, 3, 4]\n"))
  if x==1:
    cnt1+=1
  elif x==2:
    cnt2+=1
  elif x==3:
    cnt3+=1
  else:
    cnt4+=1

print("Total clients:", n)
print("Customers who bought:", buy)
print("Customers who not bought:", n-buy,"\n")

print("Units sold:")
print("Elder Wand", cnt1)
print("Hawthorn Wand", cnt2)
print("Willow Wand", cnt3)
print("Holly Wand", cnt4)
