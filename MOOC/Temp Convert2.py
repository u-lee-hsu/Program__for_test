temp=input()
type=temp[0]
Temp=eval(temp[1:])
if type in ['C','c']:
  Temp=Temp* 1.8 + 32
  print("F{:.2f}".format(Temp))
elif type in ['F','f']:
  Temp=(Temp- 32 ) / 1.8
  print("C{:.2f}".format(Temp))
else:
  print("Something Wrong!")
