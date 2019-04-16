from Tkinter import *

class DragManager():
    def add_dragable(self,widget):
        widget.bind("<ButtonPress-1>",self.on_start)
        widget.bind("<B1-Motion>",self.on_drag)
        widget.bind("<ButtonRelease-1>",self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self,event):
        pass

    def on_drag(self,event):
        pass

    def on_drop(self, event):
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        print x
        print y
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            print "no"

root = Tk()
root.geometry("800x800")

canvas = Canvas(root, height=480, width=640, bg="white")

frame = Frame(root, height=480, width=640, bg="white")
frame.propagate(0)

image = PhotoImage(file="HelpSmile.gif")

label = Label(canvas, image=image)
label.pack()

label_2 = Label(frame, text="Drop Here !")
label_2.pack()
label_2.place(x=200, y=225, anchor=CENTER)

dnd = DragManager()
dnd.add_dragable(label)

canvas.pack(side=LEFT)
frame.pack()



root.mainloop()
