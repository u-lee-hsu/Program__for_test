Money=input("请输入金额（美元以USD开头，人民币以RMB开头）：")

number=eval(Money[3:])
type=Money[0:3]
if type in ['USD','usd']:
  number=number*6.78
  print("RMB{:.2f}number".format(number))
elif type in ['RMB','rmb']:
  number=number/6.78
  print("USD{:.2f}".format(number))
else:
  print("输入有误")
