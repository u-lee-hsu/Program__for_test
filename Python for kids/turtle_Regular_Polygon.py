import turtle
import sys
pen=turtle.Pen()
def Regular_Polygon():
	print('请输入多边形的边数:')
	n=int(sys.stdin.readline())
	print('请输入多边形的边长：')
	l=int(sys.stdin.readline())
	for x in range(n):
	  pen.fd(l)
	  pen.rt(180-((n-2)*180/n))
'''Regular_Polygon()
pen.reset()
def Regular_Polygon_Fill():
        pen.reset()
        print('请输入多边形的边数:')
        n=int(sys.stdin.readline())
        print('请输入多边形的边长：')
        l=int(sys.stdin.readline())
        pen.color(1,1,0)
        pen.begin_fill()
        for x in range(n):
                pen.fd(l)
                pen.lt(180-((n-2)*180/n))
        pen.end_fill()'''

def R_P_F():
        pen.color(1,1,0)
        pen.begin_fill()
        Regular_Polygon()
        pen.end_fill()
        
R_P_F()

