from Tkinter import *
from Furniture import *

DEBUG = False
menuless = False

class Room(Canvas):

    def __init__(self,master):
        Canvas.__init__(self,master, bg = "white")
        self.pack(fill = BOTH, expand =1)
        self.furniture = []
        self.bind("<ButtonPress-1>",self.grab)
        self.bind("<B1-Motion>",self.drag)
        self.bind("<ButtonRelease-1>",self.drop)
        self.moving = Furniture("square",750,750,.1,.1,0,0)
        self.movable = 1

    #Creates a new peice of furniture in the room
    def createFurniture(self,shape,roomlength,roomwidth,length,width,x,y):
        F = Furniture(shape,roomlength,roomwidth,length,width,x,y)
        self.furniture.append(F)

    #Function that keeps the canvas updated with where all the furniture should be.
    #Runs automatically whenever furniture is moved or created
    def update(self):
        self.delete("all")
        for i in range(len(self.furniture)):
            #self.create_polygon(self.furniture[i].x,self.furniture[i].y,self.furniture[i].x+self.furniture[i].width,self.furniture[i].y,self.furniture[i].x+self.furniture[i].width,self.furniture[i].y+self.furniture[i].length,self.furniture[i].x,self.furniture[i].y+self.furniture[i].length,self.furniture[i].x,self.furniture[i].y,fill="brown")
            if(self.furniture[i].shape == "rectangle"):
                self.create_polygon(self.furniture[i].x,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y+self.furniture[i].width,self.furniture[i].x,self.furniture[i].y+self.furniture[i].width,self.furniture[i].x,self.furniture[i].y,fill="brown")
            if(self.furniture[i].shape == "oval"):
                self.create_oval(self.furniture[i].x,self.furniture[i].y,self.furniture[i].x+self.furniture[i].width,self.furniture[i].y+self.furniture[i].length,fill = "black")

    #Function that ends the drag feature when the mouse button is released
    def drop(self,event):
        self.moving.x,self.moving.y = event.widget.winfo_pointerxy()
        if(DEBUG):
            print "{} {}".format(self.moving.x,self.moving.y)
        self.update()
        self.moving = Furniture("square",750,750,.1,.1,0,0)

    #Function that continually updates the canvas so the furniture moves smoothly
    def drag(self,event):
        self.moving.x,self.moving.y = event.widget.winfo_pointerxy()
        if(DEBUG):
            print event.widget.winfo_pointerxy()
        self.update()

    #Function that determines which peice of furniture is being grabbed and initiates the drag feature
    def grab(self,event):
        xlocation,ylocation = event.widget.winfo_pointerxy()
        if(DEBUG):
            print xlocation,ylocation
        for i in range(len(self.furniture)):
            if(self.furniture[i].x<xlocation<self.furniture[i].x+self.furniture[i].width):
                if(self.furniture[i].y <ylocation<self.furniture[i].y+self.furniture[i].length):
                    self.moving = self.furniture[i]
                    self.movable = i
                    if(DEBUG):
                        print "Grabbed"
                    
        
######################################################################
if(menuless):
    Length=10
    Width=10
    window = Tk()
    window.geometry("{}x{}".format(Length*75,Width*75))
    room = Room(window)
    room.createFurniture("rectangle",750,600,200,200,100,100)

    room.createFurniture("oval", 750,600,100,100,400,500)
    if(DEBUG):
        print room.furniture[0].roomside
        print room.furniture[0].roomheight
        print room.furniture[0].x
        print room.furniture[0].y
        print room.furniture[0].length
        print room.furniture[0].width
    room.update()
    window.mainloop()

