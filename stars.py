from turtle import * 
p=Pen()
def angle(n):
    A=(n-2)*180/n
    B=180-A
    angle=3*B
    return angle
def star(n,l):
    for x in range(n):
        p.fd(l)
        p.lt(angle(n))
        
star(5,100)
