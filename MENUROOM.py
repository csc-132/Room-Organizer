from Tkinter import *
import tkMessageBox
from Furniture import *
import RPi.GPIO as GPIO
from time import sleep,time

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
                        break

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
                Menu.X.grid(row=7,column=0,sticky=W+E)
                Menu.Y=Label(Menu.master,text='y:')
                Menu.Y.grid(row=7,column=1,sticky=W+E)
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
        self.correction_factor=0
        self.x=None
        self.y=None

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
                
            b1=Button(self.master,text='Create Furniture',command=self.furnish)
            b1.grid(row=3,column=1)

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

    def calibrate(self):
        print "Calibrating..."
        # prompt the user for an object's known distance
        print "-Place the sensor a measured distance away from an \
         object."
        known_distance = input("-What is the measured distance \
         (cm)? ")
        # measure the distance to the object with the sensor
        # do this several times and get an average
        print "-Getting calibration measurements..."
        distance_avg = 0
        for i in range(CALIBRATIONS):
            distance = getDistance()
            if (DEBUG):
                print "--Got {}cm".format(distance)
            # keep a running sum
            distance_avg += distance
            # delay a short time before using the sensor again
            sleep(CALIBRATION_DELAY)
        # calculate the average of the distances
        distance_avg /= CALIBRATIONS
        if (DEBUG):
            print "--Average is {}cm".format(distance_avg)
        # calculate the correction factor
        correction_factor = known_distance / distance_avg
        if (DEBUG):
            print "--Correction factor is \ {}".format(correction_factor)
        print "Done.\n"
        
        print correction_factor+"\n"
        
        self.correction_factor = correction_factor

    def getDistance():
        # trigger the sensor by setting it high for a short time and
        # then setting it low
        GPIO.output(TRIG, GPIO.HIGH)
        sleep(TRIGGER_TIME)
        GPIO.output(TRIG, GPIO.LOW)
        # wait for the ECHO pin to read high
        # once the ECHO pin is high, the start time is set
        # once the ECHO pin is low again, the end time is set
        while (GPIO.input(ECHO) == GPIO.LOW):
            start = time()
        while (GPIO.input(ECHO) == GPIO.HIGH):
            end = time()
        # calculate the duration that the ECHO pin was high
        # this is how long the pulse took to get from the sensor to
        # the object -- and back again
        duration = end - start
        # calculate the total distance that the pulse traveled by
        # factoring in the speed of sound (m/s)
        distance = duration * SPEED_OF_SOUND
        # the distance from the sensor to the object is half of the
        # total distance traveled
        distance /= 2
        # convert from meters to centimeters
        distance *= 100
        return distance*self.correction_factor

    def scan_x(self):
        self.x=getDistance()

    def scan_y(self):
        self.y=getDistance()
    
    def convert(self):
        try:
            Menu.l3=Label(self.master,text=str(int(float(Menu.e3.get())*12)))
            Menu.l3.grid(row=5,column=1,sticky=E+W)
        except ValueError:
            tkMessageBox.showinfo('Error','Must enter a number')

    def furnish(self):
        if  ((self.x!=None) and (self.x!=None) and (Menu.SCREEN_Y>=self.x) and (Menu.SCREEN_Y>=self.y)):
            x=self.x
            y=self.y

            if (Menu.C.get()):
                Menu.room.createFurniture("oval",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
            else:
                Menu.room.createFurniture("rectangle",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
                
        elif (((str.isdigit(Menu.e1.get()))) and (str.isdigit(Menu.e2.get())) and (Menu.SCREEN_Y>=int(Menu.e1.get())) and (Menu.SCREEN_Y>=int(Menu.e2.get()))):
            x=int(Menu.e1.get())
            y=int(Menu.e2.get())
                
            if (Menu.C.get()):
                Menu.room.createFurniture("oval",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
            else:
                Menu.room.createFurniture("rectangle",Menu.SCREEN_X,Menu.SCREEN_Y,int(Menu.s*y),int(Menu.s*x))
        else:
            tkMessageBox.showinfo('Error','Must enter an integer in inches and must not be bigger than the room')
        
    def setUpMenu(self):
        l1=Label(self.master,text='Enter room dimensions in\ninches and as an integer. Make sure\nto make only one room at a time.')
        l1.grid(row=0,column=0,columnspan=2,sticky=E+W)
        
        Menu.e1=Entry(self.master)
        Menu.e1.grid(row=1,column=0)
        Menu.e1.focus()
        s1=Button(self.master,text='   Scan Width   ',command=self.scan_x)
        s1.grid(row=1,column=1,sticky=E+W)
        
        
        Menu.e2=Entry(self.master)
        Menu.e2.grid(row=2,column=0)
        s2=Button(self.master,text='   Scan Width   ',command=self.scan_y)
        s2.grid(row=2,column=1,sticky=E+W)
        
        b=Button(self.master,text='Create Room',command=self.createRoom)
        b.grid(row=3,column=0,sticky=E+W)

        l2=Label(self.master,text='\nFeet>Inch Converter')
        l2.grid(row=4,column=0,sticky=E+W)

        Menu.e3=Entry(self.master)
        Menu.e3.grid(row=5,column=0)
        Menu.l3=Label(self.master,text='')
        Menu.l3.grid(row=5,column=1,stick=E+W)

        b2=Button(self.master,text='    Convert   ',command=self.convert)
        b2.grid(row=6,column=0,columnspan=2,sticky=E+W)

        b3=Button(self.master,text='Calibrate Sensor',command=self.calibrate)
        b3.grid(row=7,column=0,columnspan=2,stick=E+W)    
################################################################################
# constants
DEBUG = True # debug mode?

SETTLE_TIME = 2 # seconds to let the sensor settle

CALIBRATIONS = 5 # number of calibration measurements to

# take
CALIBRATION_DELAY = 1 # seconds to delay in between

# calibration measurements
TRIGGER_TIME = 0.00001 # seconds needed to trigger the sensor

# (to get a measurement)
SPEED_OF_SOUND = 343 # speed of sound in m/s


# set the RPi to the Broadcom pin layout
GPIO.setmode(GPIO.BCM)


# GPIO pins
TRIG = 18 # the sensor's TRIG pin

ECHO = 27 # the sensor's ECHO pin

GPIO.setup(TRIG, GPIO.OUT) # TRIG is an output
GPIO.setup(ECHO, GPIO.IN) # ECHO is an input

# first, allow the sensor to settle for a bit
print "Waiting for sensor to settle ({}s)...".format(SETTLE_TIME)
GPIO.output(TRIG, GPIO.LOW)
sleep(SETTLE_TIME)

window=Tk()
##window.geometry('250x200')
window.title("Menu")
window.resizable(width='False',height='False')
Menu=Menu(window)
Menu.setUpMenu()
window.mainloop()
