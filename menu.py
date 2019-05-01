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

        if (DEBUG):
            print SCREEN_X,SCREEN_Y
        
        if ((str.isdigit(Menu.e1.get())) and (str.isdigit(Menu.e2.get()))):
            if (int(Menu.e1.get())>int(Menu.e2.get())):
                x=int(Menu.e1.get())
                y=int(Menu.e2.get())
            else:
                x=int(Menu.e2.get())
                y=int(Menu.e1.get())
                
            if (DEBUG):
                print x,y,4/2,x/y,SCREEN_X/x

            xs,ys=SCREEN_X/x,SCREEN_Y/y
            if (xs < ys):
                s=xs
            else:
                s=ys
            room_window=Tk()
            room_window.geometry('{}x{}'.format(x*s-70,y*s-70))
            room_window.title("Room")
            room=Room(room_window)
            room_window.mainloop()
        else:
            tkMessageBox.showinfo('Error','Must enter an integer in inches')

    def convert(self):
        try:
            Menu.l3.forget()
            Menu.l3=Label(self.master,text=str(int(float(Menu.e3.get())*12)))
            Menu.l3.pack()
        except ValueError:
            tkMessageBox.showinfo('Error','Must enter a number')
    
    def setUpMenu(self):
        l1=Label(self.master,text='Enter room dimensions in\ninches and as an integer')
        l1.pack()
        
        Menu.e1=Entry(self.master)
        Menu.e1.pack()
        Menu.e1.focus()
        
        Menu.e2=Entry(self.master)
        Menu.e2.pack()
        
        Menu.b1=Button(self.master,text='Create Room',command=self.createRoom)
        Menu.b1.pack()

        l2=Label(self.master,text='\nFeet>Inch Converter')
        l2.pack()

        Menu.e3=Entry(self.master)
        Menu.e3.pack()

        Menu.b2=Button(self.master,text='Convert',command=self.convert)
        Menu.b2.pack()

        Menu.l3=Label(self.master,text='')
        Menu.l3.pack()
################################################################################
window=Tk()
window.geometry('250x200')
window.title("Menu")
Menu=Menu(window)
Menu.setUpMenu()
window.mainloop()
