#DayDayupVSHaveARest.py
A=1
B=1
dayfactor=0.01
A=pow(A+dayfactor,365)
print("A="+"{:.2f}".format(A))
df=dayfactor
def dayf(df):
    B=1

    for i in range(365):
        if i%7 in [0,6]:
            B=B*(1-0.01)
        else:
            B=B*(1+df)
    return B
while dayf(df) < A :
    print("B="+"{:.3f}".format(dayf(df)))
    df+=0.001
    print("df="+"{:.4f}".format(df))
print(df)
print(dayfactor)
df=(df-dayfactor)*100
print("A每天多完成"+"{:.2f}".format(dayfactor*100)+
      "%那么,一年后比不努力要多完成{:.2f}".format(A)
      +"，B如果做五休二，则在工作日要比A更努力{:.3f}%才能超过A".format(df))
