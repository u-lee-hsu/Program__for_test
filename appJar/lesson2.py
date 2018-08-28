from appJar import gui
import random
win=gui('windows','50x60')
win.addLabel('lb1','按了多少次')
count=0
n=random.randint(0,5)
def CountDown():
    global count
    count-=1
    win.setLabel('lb1','按了'+str(count)+'次')
    color()
    if count==0:
        win.stop()
def CountUp():
    global count
    count+=1
    win.setLabel('lb1','按了'+str(count)+'次')
    color()
    if count==0:
        win.stop()
win.addButton('加',CountUp)
win.addButton('减',CountDown)
def color():
    color=['blue','pink','red','orange','black','green','gold','pink','yellow']
    
    win.setFg(color[random.randint(0,8)])
    win.setBg(color[random.randint(0,8)])
win.go()
