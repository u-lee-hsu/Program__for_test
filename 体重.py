import sys
def moon_weight():
    print("你的体重是?")
    weight=int(sys.stdin.readline())
    print('你每年增重多少公斤?')
    add=int(sys.stdin.readline())
    print('你连续去了月球几年?')
    years=int(sys.stdin.readline())
    for year in range(years):
        weight_on_moon=weight*0.165
        weight=weight+add
        print('你第%s年在月球上的重量是：%skg'%(year,weight_on_moon))


