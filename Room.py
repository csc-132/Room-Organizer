from Tkinter import *
from Furniture import *

class Room(Canvas):

    def __init__(self,master):
        Canvas.__init__(self,master, bg = "white")
        self.pack(fill = BOTH, expand =1)
        self.furniture = []

    #Creates a new peice of furniture in the room
    def createFurniture(self,name,length,width):
        F = Furniture(name,length,width)
        self.furniture.append(F)

    #Function that keeps the canvas updated with where all the furniture should be.
    #Runs automatically whenever furniture is moved or created
    def update(self):
        for i in range(len(self.furniture)):
            self.create_polygon(self.furniture[i].x,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y+self.furniture[i].width,self.furniture[i].x,self.furniture[i].y+self.furniture[i].width,self.furniture[i].x,self.furniture[i].y,fill="brown")
        #self.furniture[i].x,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y,self.furniture[i].x+self.furniture[i].length,self.furniture[i].y+self.furniture[i].width,self.furniture[i].x,self.furniture[i].y+self.furniture[i].width,fill="red")

    def drag(self):
        pass
######################################################################
#window = Tk()
#window.geometry("{}x{}".format(Length*75,Width*75))
#room = Room(window)
#room.createFurniture("chair",2*75,4*75)
#room.furniture[0].x=50
#room.furniture[0].y=70
#room.update()
#window.mainloop()

