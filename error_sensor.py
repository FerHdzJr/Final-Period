"""https://replit.com/join/dxlfhpttvy-a00573910"""
n=int(input("How many temperatures readings do you have?\n"))
cnt=0
for i in range(0, n):
  x=int(input("Insert temperature: "))
  if x<10 or x>40:
    cnt+=1

print("The sensor went wrong:", cnt, "times")
print("The sensor error rate is: "+str(cnt/n*100)+"%")
