N=input()
n=eval(N)/1000
if 0<=n<=100:
  Up=1
  Down=1
  for i in range(365):
    Up=Up*(1+n)
    Down=Down*(1-n)
  print("{:.2},{:.2},{:d}".format(Up,Down,Up/Down))
