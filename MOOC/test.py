#DayDayUp01.py
dayup =pow(1.001,365)
daydown =pow(0.999,365)
print(dayup,daydown)

dayfactor=eval(input())
DU=pow(1+dayfactor,365)
DD=pow(1-dayfactor,365)
print("{:.3f},{:.3f}".format(DU,DD))
