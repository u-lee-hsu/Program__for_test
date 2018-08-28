reliang=input()
if reliang[-1] in ['J']:
  Cal=(eval(reliang[:-1])/4.186)
  print(Cal)
  print("{:.3f}cal".format(Cal))
elif reliang[-3:] in ['cal']:
  J=eval(reliang[:-3])*4.186
  print("{:.3f}J".format(J))
else:
  print("sth wrong")
