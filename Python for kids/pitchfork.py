import turtle
sonic1=turtle.Pen()
sonic2=turtle.Pen()
sonic3=turtle.Pen()
sonic4=turtle.Pen()
def fork1():
    sonic1.fd(100)
    sonic1.left(90)
    sonic1.fd(100)
    sonic1.right(90)
    sonic1.fd(50)
def fork2():
    sonic2.fd(100)
    sonic2.fd(10)
    sonic2.left(90)
    sonic2.fd(30)
    sonic2.right(90)
    sonic2.fd(45)
def fork3():
    sonic3.fd(100)
    sonic3.right(90)
    sonic3.fd(100)
    sonic3.left(90)
    sonic3.fd(50)
def fork4():
    sonic4.fd(100)
    sonic4.fd(10)
    sonic4.right(90)
    sonic4.fd(30)
    sonic4.left(90)
    sonic4.fd(45)

    
def pitchfork():
    fork1()
    fork2()
    fork3()
    fork4()
