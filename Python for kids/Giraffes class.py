class Things():
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Animals(Animate):
    def eat(self):
        print('eating')
class Mammals(Animals):
    def feed_young(self):
        print('feeding young with milk')
    def move(self):
        print('moving')
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("I've found food!")
    def dance(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def __init__(self,spots):
        self.giraffe_spots=spots
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_back(self):
        print('right foot back')
    def dan(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
        
Lucy=Giraffes(100)
        


        
