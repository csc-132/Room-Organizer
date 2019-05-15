from Tkinter import *
import tkMessageBox
from Room import *

DEBUG = False

##########################################################
##########################################################
class Room(Canvas):

    def __init__(self,master):
        Canvas.__init__(self,master, bg = "white")
        self.pack(fill = BOTH, expand =1)
        self.furniture = []
        self.bind("<ButtonPress-1>",self.grab)
        self.bind("<B1-Motion>",self.drag)
        self.bind("<ButtonRelease-1>",self.drop)
        self.moving = Furniture("square",750,750,.1,.1)
        self.movable = 1

    #Creates a new peice of furniture in the room
    def createFurniture(self,shape,roomlength,roomwidth,length,width):
        F = Furniture(shape,roomlength,roomwidth,length,width)
        self.furniture.append(F)
        self.update()

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
        for x in range(int(self.moving.width)+1):
            for y in range(int(self.moving.length)+1):
                for f in self.furniture:
                    if ((f.x<=self.moving.x+x<=f.x+f.width) and (f.y<=self.moving.y+y<=f.y+f.length)):
                        tkMessageBox.showinfo("Collisions","Can not place objects over each other")
                        break
                    else:
                        self.moving.x,self.moving.y = event.widget.winfo_pointerxy()
                        if(DEBUG):
                            print "{} {}".format(self.moving.x,self.moving.y)
                        self.update()
                        self.moving = Furniture("square",750,750,.1,.1)

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

    def motion(self,event):
        x,y = event.x,event.y
        for i in range(len(self.furniture)):
            if(self.furniture[i].x<x<self.furniture[i].x+self.furniture[i].width):
                if(self.furniture[i].y <y<self.furniture[i].y+self.furniture[i].length):

                    Menu.X=Label(Menu.master,text='x: {}'.format(self.furniture[i].width*(1/Menu.s)))
                    Menu.X.grid(row=7,column=0,sticky=W)
                    Menu.Y=Label(Menu.master,text='y: {}'.format(self.furniture[i].length*(1/Menu.s)))
                    Menu.Y.grid(row=7,column=1,sticky=W)
                    print self.furniture[i].width,self.furniture[i].length
            else:
                Menu.X=Label(Menu.master,text='x:')
                Menu.X.grid(row=7,column=0,sticky=W)
                Menu.Y=Label(Menu.master,text='y:')
                Menu.Y.grid(row=7,column=1,sticky=W)
                print ''
##                    measurement=Tk()
##                    measurement.geometry('+{}+{}'.format(x,y))
                    
        
########################################################################
##Length=10
##Width=10
##window = Tk()
##window.geometry("{}x{}".format(Length*75,Width*75))
##room = Room(window)
##room.createFurniture("rectangle",750,600,10,20)
##room.furniture[0].x=100
##room.furniture[0].length=200
##room.furniture[0].width=200
##room.furniture[0].y=100
##room.createFurniture("oval", 750,600,100,100)
##room.furniture[1].x=400
##room.furniture[1].y=500
##if(DEBUG):
##    print room.furniture[0].roomside
##    print room.furniture[0].roomheight
##    print room.furniture[0].x
##    print room.furniture[0].y
##    print room.furniture[0].length
##    print room.furniture[0].width
##room.update()
##window.mainloop()
################################################################################
################################################################################

class Menu(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master

    def createRoom(self):
        Menu.SCREEN_X=int(window.winfo_screenwidth())
        Menu.SCREEN_Y=int(window.winfo_screenheight())
        
        if ((str.isdigit(Menu.e1.get())) and (str.isdigit(Menu.e2.get()))):
            if (int(Menu.e1.get())>int(Menu.e2.get())):
                x=int(Menu.e1.get())
                y=int(Menu.e2.get())
            else:
                x=int(Menu.e2.get())
                y=int(Menu.e1.get())
            
            xs,ys=Menu.SCREEN_X/float(x),Menu.SCREEN_Y/float(y)
                
            if (xs < ys):
                Menu.s=xs
            else:
                Menu.s=ys
                
            Menu.b1=Button(self.master,text='Create Furniture',command=self.furnish)
            Menu.b1.grid(row=3,column=1)

            Menu.C=IntVar()
            Menu.c1=Checkbutton(self.master,text='Circular',variable=Menu.C)
            Menu.c1.grid(row=4,column=1,sticky=E+W)

            room_window=Tk()
            room_window.geometry('{}x{}'.format(int(x*Menu.s-70),int(y*Menu.s-70)))
            room_window.title("Room")
            room_window.resizable(width='False',height='False')
            Menu.room=Room(room_window)
            room_window.bind('<Motion>',Menu.room.motion)
            room_window.mainloop()
            
        else:
            tkMessageBox.showinfo('Error','Must enter an integer in inches')
        
    def convert(self):
        try:
            Menu.l3=Label(self.master,text=str(int(float(Menu.e3.get())*12)))
            Menu.l3.grid(row=5,column=1,sticky=E+W)
        except ValueError:
            tkMessageBox.showinfo('Error','Must enter a number')

    def furnish(self):
        if (((str.isdigit(Menu.e1.get()))) and (str.isdigit(Menu.e2.get())) and (Menu.SCREEN_Y>=int(Menu.e1.get())) and (Menu.SCREEN_Y>=int(Menu.e2.get()))):
            if (int(Menu.e1.get())>int(Menu.e2.get())):
                x=int(Menu.e1.get())
                y=int(Menu.e2.get())
            else:
                x=int(Menu.e2.get())
                y=int(Menu.e1.get())
                
            if (Menu.C.get()):
                Menu.room.createFurniture("oval",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
            else:
                Menu.room.createFurniture("rectangle",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
        else:
            tkMessageBox.showinfo('Error','Must enter an integer in inches and must not be bigger than the room')
        
    def setUpMenu(self):
        l1=Label(self.master,text='Enter room dimensions in inches\nand as an integer')
        l1.grid(row=0,column=0,columnspan=2,sticky=E+W)
        
        Menu.e1=Entry(self.master)
        Menu.e1.grid(row=1,column=0)
        Menu.e1.focus()
        s1=Button(self.master,text='       Scan       ')
        s1.grid(row=1,column=1,sticky=E+W)
        
        
        Menu.e2=Entry(self.master)
        Menu.e2.grid(row=2,column=0)
        s2=Button(self.master,text='       Scan     ')
        s2.grid(row=2,column=1,sticky=E+W)
        
        Menu.b1=Button(self.master,text='Create Room',command=self.createRoom)
        Menu.b1.grid(row=3,column=0,sticky=E+W)

        l2=Label(self.master,text='\nFeet>Inch Converter')
        l2.grid(row=4,column=0,sticky=E+W)

        Menu.e3=Entry(self.master)
        Menu.e3.grid(row=5,column=0)
        Menu.l3=Label(self.master,text='')
        Menu.l3.grid(row=5,column=1,stick=E+W)

        Menu.b2=Button(self.master,text='    Convert   ',command=self.convert)
        Menu.b2.grid(row=6,column=0,columnspan=2,sticky=E+W)
################################################################################
window=Tk()
##window.geometry('250x200')
window.title("Menu")
window.resizable(width='False',height='False')
Menu=Menu(window)
Menu.setUpMenu()
window.mainloop()
