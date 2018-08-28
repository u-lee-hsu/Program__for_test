#DayDayUp01.py
dayup =pow(1.001,365)
daydown =pow(0.999,365)
print(dayup,daydown)

dayfactor=eval(input("你每天准备多努力多少呢？（请输入0～100的值）"))
day=eval(input("你一年努力多少天？"))
DU=pow(1+dayfactor/100,day)
DD=pow(1-dayfactor/100,day)
percent=1
for i in range(365):
    if i%7 in [0,6]:
        percent=percent*(1-dayfactor/100)
    else:
        percent=percent*(1+dayfactor/100)
print("每天努力一点点，你就会进步：{:.3f},每天偷懒一点点，你就会退步到：{:.3f},365天内如果工作时间每天努力一点点，放假期间每天偷懒一点点，你会做到{:.3f}".format(DU,DD,percent))


