"""https://replit.com/join/pdubisgpnn-a00573910"""
cad=input()
cad=cad.split()
cnt=0
pal=""
for s in cad:
  s=s.lower()
  for i in s:
    if i.isalpha()==False:
      continue
    pal+=i
  pal+=" "
pal=pal.split()
for s in pal:
  if s=="Alexa" or s=="alexa":
    cnt+=1
if cnt==1:
  print("Tell me, how can i help you?")
elif cnt>1:
  print("Hey, just say my name once")
