from tkinter import *

import random

class SnakeGUI:
    def __init__(self):
        self.food_points = 0
        
        self.coord_lst = []

        self.gameover = False
        
        self.bool = False
        
        self.top = Tk()
        self.top.geometry("1500x600")
        self.top.configure(background = "blue")
        self.top.title("Snake Game")
        self.win = Canvas(self.top, bg = "white", width=600, height=600)
        self.win.pack()
        
        self.top.bind("<d>", self.move_right)
        self.top.bind("<a>", self.move_left)
        self.top.bind("<w>", self.move_up)
        self.top.bind("<s>", self.move_down)

        self.top.bind("<Right>", self.move_right)
        self.top.bind("<Left>", self.move_left)
        self.top.bind("<Up>", self.move_up)
        self.top.bind("<Down>", self.move_down)

        self.top.bind("<space>", self.space_pause)
        
        self.testButton = Button(self.top, text="START", command = self.pause)
        self.testButton.place(x = 895, y = 300)
        
        self.X = 300
        self.Y = 300
        self.X2 = 280
        self.Y2 = 280
        self.lst = [self.win.create_rectangle(self.X, self.Y, self.X2, self.Y2, \
                                              fill = "green")]

        self.pause()
        
        self.food_make()
        
        self.direction = [20,0]

        self.time = 500
                    
        self.top.mainloop()
        
    def restart_game(self):
        self.top.destroy()
        SnakeGUI()                    
    def food_make(self):        
        self.xOne = random.randrange(40, 560, 20)
        self.yOne = random.randrange(40, 560, 20)
        self.xTwo = self.xOne - 20
        self.yTwo = self.yOne - 20

        while self.xOne == 300 and self.yOne == 300 and self.xTwo == 280 and self.yTwo\
              == 280:
            self.xOne = random.randrange(40, 560, 20)
            self.yOne = random.randrange(40, 560, 20)
            self.xTwo = self.xOne - 20
            self.yTwo = self.yOne - 20
           
        itr = 0
        while itr < (len(self.coord_lst) - 1):
            while self.coord_lst[itr][0] == self.xOne and self.coord_lst[itr][1] == \
                  self.yOne:
                self.xOne = random.randrange(40,560,20)
                self.yOne = random.randrange(40,560,20)
                self.xTwo = self.xOne - 20
                self.yTwo = self.yOne - 20
            itr += 1
            
        self.food = self.win.create_oval(self.xOne, self.yOne,\
                                              self.xTwo, self.yTwo, fill = "yellow")
        
    def space_pause(self,event):
        if self.bool == True:
            self.bool = False
            self.testButton["text"] = "PAUSE"
            self.move()
        else:
            if self.bool == False:
                self.bool = True

    def pause(self):
        if self.bool == True:
            self.bool = False
            self.testButton["text"] = "PAUSE"
            self.move()
        else:
            if self.bool == False:
                self.bool = True
                self.testButton["text"] = "START"
                
    def comb_func(self):
        self.text.place_forget()
        self.text["text"] = ""
        self.restart_game()
                
    def move_right(self, event):
        self.direction = [20,0]

    def move_left(self, event):
        self.direction = [-20,0]

    def move_up(self, event):
        self.direction = [0, -20]

    def move_down(self, event):
        self.direction = [0,20]
            
    def move(self):
        self.win.delete(self.lst[-1])
        self.lst = self.lst[:-1]
        
        self.X += self.direction[0]
        self.X2 += self.direction[0]
        self.Y += self.direction[1]
        self.Y2 += self.direction[1]
        
        self.coord_lst.append([self.X,self.Y])
        
        self.lst.insert(0, self.win.create_rectangle(self.X, self.Y, \
                                                     self.X2, self.Y2, \
                                                     fill = "green"))

        if (self.X == self.xOne and self.Y == self.yOne) or (self.X2 == \
           self.xTwo  and self.Y2  == self.yTwo):
            self.food_points += 1
            self.time -= 10
            self.win.delete(self.food)
            self.lst.insert(0, self.win.create_rectangle(self.X, self.Y, self.X2, \
                                                         self.Y2, fill = "green"))
            self.food_make()
        else:
            self.coord_lst=self.coord_lst[1:]
            

        if self.X == 600 or self.Y == 600 or self.X2 == 600 or self.Y2 == 600 or \
           self.X == 0 or self.Y == 0 or self.X2 == 0 or self.Y2 == 0:
            self.text = Label(self.win, text = ("GAME OVER! SCORE: ") + \
                              str(self.food_points), font = ("Helvetica", 15))
            self.text.place(x = 250, y = 200)
            self.bool = True
            self.testButton.place_forget()
            self.button = Button(self.win, text="RESTART", command = self.comb_func)
            self.button.place(x = 300, y = 280)
            self.gameover = True

        itr = 0
        while itr < (len(self.coord_lst) - 1):
            if self.coord_lst[itr][0] == self.X and self.coord_lst[itr][1] == self.Y:
                self.text = Label(self.win, text = ("GAME OVER! SCORE: ") + \
                                  str(self.food_points), font = ("Helvetica", 15))
                self.text.place(x = 250, y = 200)
                self.bool = True
                self.testButton.place_forget()
                self.button = Button(self.win, text="RESTART", command = self.comb_func)
                self.button.place(x = 300, y = 280)
                self.gameover = True
            itr += 1
                
        if self.bool == False and self.gameover == False: 
            self.win.after(self.time, self.move)
