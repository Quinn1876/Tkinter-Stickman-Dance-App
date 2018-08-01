from tkinter import *
import time
class Window(Frame):
    """
    Widgets:
    Animation
    Start Button
    """
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.animation = BestMates(self.master)
        self.start_button = Button(self.master, text="Start", command=self.animation.dance)
        self.kill_button = Button(self.master, text="END", command=self.destroy).pack()
        
        self.start_button.pack(side=BOTTOM)
        

class Shape():
    
    
    def __init__(self, canvas, shape, x1, y1, dx, dy):
        self.x1 = x1
        self.x2 = x1 + dx
        self.y1 = y1
        self.y2 = y1 + dy
        self.shape = shape
        self.shapes = {'arc' : canvas.create_arc,
                       'line' : canvas.create_line,
                       'oval' : canvas.create_oval,
                       'rectangle' : canvas.create_rectangle}

    # returns starting coords
    def start(self): return [self.x1, self.y1]

    # returns end cords
    def end(self): return [self.x2, self.y2]

    def draw(self):
        try:
            self.shapes[self.shape](self.x1, self.y1, self.x2, self.y2)
        except KeyError:
            print("%s not found in shapes" % (self.shape))
            
        
class Animation(Canvas):
    """
    This is the basic animation class. It has a single costume that is a stickman just standing still
    All animations are children of this class. 
    """
    _WIDTH = 300
    _HEIGHT = 300
    
    def __init__(self, master=None):
        Canvas.__init__(self, master=None, width=self._WIDTH, height=self._HEIGHT, background="white")
        # self.bind("<Button-1>", self.callback)
        self.costume1()
        self.pack()

    
    def print_costume(self, costume):
        if type(costume) is not list:
            print('The costume needs to be a list')
            return 0
         # Deletes all the other stuff currently drawn
        self.delete("all")
        # Draws the costume
        for c in costume:
            if type(c) is Shape:
                c.draw()
            else:
                for k in c.keys():
                    c[k].draw()

    def dance(self):
        pass

    def costume1(self):
        """
        The stick man is standing still
            0
       left/|\right
            |
           / \
        """        

        # defines then draws all the shapes
        _head = Shape(self, 'oval', 130, 50, 30, 30)

        _upperBody = Shape(self, 'line', 145, 80, 0, 60)

        _leftArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [-10, 20]))}
        _leftArm['lower'] =  Shape(self, 'line', *(_leftArm['upper'].end()+ [-10, 20]))
               
        _rightArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [10, 20]))}
        _rightArm['lower'] =  Shape(self, 'line', *(_rightArm['upper'].end()+ [10, 20]))

        _leftLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [-10, 20]))}
        _leftLeg['lower'] =  Shape(self, 'line', *(_leftLeg['upper'].end()+ [-10, 20]))
               
        _rightLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [10, 20]))}
        _rightLeg['lower'] =  Shape(self, 'line', *(_rightLeg['upper'].end()+ [10, 20]))

        costume = [_head,
                   _upperBody,
                   _leftArm,
                   _rightArm,
                   _leftLeg,
                   _rightLeg]
        
        self.print_costume(costume)
       
     
class BestMates(Animation):
    """
    Best mates dance from fortnight
    """

    def move1(self):
        """
            0
          --|----
          | |
           / \
        """
        _head = Shape(self, 'oval', 130, 50, 30, 30)

        _upperBody = Shape(self, 'line', 145, 80, 0, 60)

        _leftArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [-22.36, 0]))}
        _leftArm['lower'] =  Shape(self, 'line', *(_leftArm['upper'].end()+ [0, 22.36]))
               
        _rightArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [22.36, 0]))}
        _rightArm['lower'] =  Shape(self, 'line', *(_rightArm['upper'].end()+ [22.36, 0]))

        _leftLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [-10, 20]))}
        _leftLeg['lower'] =  Shape(self, 'line', *(_leftLeg['upper'].end()+ [-10, 20]))
               
        _rightLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [10, 20]))}
        _rightLeg['lower'] =  Shape(self, 'line', *(_rightLeg['upper'].end()+ [10, 20]))

        costume = [_head,
                   _upperBody,
                   _leftArm,
                   _rightArm,
                   _leftLeg,
                   _rightLeg]
        
        self.print_costume(costume)

    def move2(self):
        """
            0
        ----|--
            | |
           / \
        """
        _head = Shape(self, 'oval', 130, 50, 30, 30)

        _upperBody = Shape(self, 'line', 145, 80, 0, 60)

        _leftArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [-22.36, 0]))}
        _leftArm['lower'] =  Shape(self, 'line', *(_leftArm['upper'].end()+ [-22.36, 0]))
               
        _rightArm = {"upper" : Shape(self, 'line', *(_upperBody.start() + [22.36, 0]))}
        _rightArm['lower'] =  Shape(self, 'line', *(_rightArm['upper'].end()+ [0, 22.36]))

        _leftLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [-10, 20]))}
        _leftLeg['lower'] =  Shape(self, 'line', *(_leftLeg['upper'].end()+ [-10, 20]))
               
        _rightLeg = {"upper" : Shape(self, 'line', *(_upperBody.end() + [10, 20]))}
        _rightLeg['lower'] =  Shape(self, 'line', *(_rightLeg['upper'].end()+ [10, 20]))

        costume = [_head,
                   _upperBody,
                   _leftArm,
                   _rightArm,
                   _leftLeg,
                   _rightLeg]
        
        self.print_costume(costume)

    def dance(self):
        count = 0
        while True:
            if count == 0:
                self.move1()
                count = 1
            else:
                self.move2()
                count = 0
            tk.update_idletasks()
            tk.update()
            time.sleep(0.5)
    
    
if __name__ == '__main__':
    tk = Tk()

    window1 = Window(tk)

    tk.mainloop()
