from Tkinter import *
import tkMessageBox

DEBUG=False

class Room(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        
    
class Menu(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master

    def createRoom(self):
        SCREEN_X=int(window.winfo_screenwidth())
        SCREEN_Y=int(window.winfo_screenheight())
        
        if ((str.isdigit(Menu.e1.get())) and (str.isdigit(Menu.e2.get()))):
            if (int(Menu.e1.get())>int(Menu.e2.get())):
                x=int(Menu.e1.get())
                y=int(Menu.e2.get())
            else:
                x=int(Menu.e2.get())
                y=int(Menu.e1.get())

            xs,ys=SCREEN_X/x,SCREEN_Y/y
            if (xs < ys):
                s=xs
            else:
                s=ys
                
            Menu.b1=Button(self.master,text='Create Furniture')
            Menu.b1.grid(row=3,column=1)

            c1=Checkbutton(self.master,text='Circular')
            c1.grid(row=4,column=1,sticky=E+W)
            
            room_window=Tk()
            room_window.geometry('{}x{}'.format(x*s-70,y*s-70))
            room_window.title("Room")
            room=Room(room_window)
            room_window.mainloop()
        else:
            tkMessageBox.showinfo('Error','Must enter an integer in inches')
    
    def convert(self):
        try:
            Menu.l3=Label(self.master,text=str(int(float(Menu.e3.get())*12)))
            Menu.l3.grid(row=5,column=1,sticky=E+W)
        except ValueError:
            tkMessageBox.showinfo('Error','Must enter a number')
    
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
Menu=Menu(window)
Menu.setUpMenu()
window.mainloop()
