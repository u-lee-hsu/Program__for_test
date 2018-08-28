from tkinter import *

#创建根窗口 root名字随便取
root = Tk()
#title里面设置窗口标题 
root.title("Hello")
#设置窗口大小 geometry（几何结构）
root.geometry("300x200")
#在窗体中创建一个frame(框架、结构)，用它来承载其他小部件
app = Frame(root)
#设置布局管理器 grid 格子
app.grid()
#label(标签)
label = Label(app,text="hello word!")
#生成标签
label.grid()

btn = Button(app)
#生成按钮
btn.grid()

#小部件的任何选项都可以通过configure()方法操作
btn.configure(text = "click")

root.mainloop();
