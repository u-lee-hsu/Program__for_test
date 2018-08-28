from tkinter import *
import random
import time
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=(canvas.create_rectangle(0,0,100,10,fill=color))
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
    
        
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        #创建椭圆，create_oval(x1,y1,x2,y2,fill=颜色）
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        #将椭圆self.id移动到245x100
        self.canvas.move(self.id,245,100)
        #设置list作为移动变量初始值取值范围
        starts=[-1,-2,-1,1,2,3]
        #随机
        random.shuffle(starts)
        #设置移动变量初始值
        self.x=starts[0]
        self.y=starts[1]

        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        #设定撞底边初始False
        self.hit_bottom=False
        
    def draw(self):
        #canvas.move移动对象，self.x self.y为移动变量
        self.canvas.move(self.id,self.x,self.y)
        #小球坐标左上X：pos[0] 左上Y：pos[2] 右下X：pos[1] 右下Y：pos[3]
        pos=self.canvas.coords(self.id)
        #上边界
        if pos[1]<=0:
            self.y=3
        #下边界
        if pos[3]>=self.canvas_height:
            self.y=-3
        #左边界
        if pos[0]<=0:
            self.x=3
        #右边界
        if pos[2]>=self.canvas_width:
            self.x=-3
        #撞平板
        if self.hit_paddle(pos)==True:
            self.y=-3
        #撞地面，小球底部Y坐标pos[3]大于画布高canvas.height，小球撞底边为真
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
        #打印坐标：调试用    
        #print(self.canvas.coords(self.id))
    '''撞平板检测，如果X方向小球在平板区域内（小球右下X2>=平板左侧坐标 并且 小球左上X1<=平板右侧坐标）
    再判断Y方向小球下底边在平板区域内（如果小球右下Y2>=平板左上Y1 并且 小球右下Y2<=平板右下Y2）
    那么，撞击有效'''        
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1]and pos[3]<=paddle_pos[3]:
                return True
            return False
        
#建立画布       
tk=Tk()
#标题是GAME
tk.title('Game')
#画布不可调节,1可调,0不可调
tk.resizable(0,0)
#窗口状态，-disabled(窗口点击无效） -toolwindow（工具菜单） -topmost（窗口置顶） 
tk.wm_attributes('-topmost',1)
#画布定义 
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
canvas.update()
paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red')
time.sleep(5)
while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
