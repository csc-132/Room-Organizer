class Furniture(object):

    def __init__(self,shape,roomside,roomheight,length,width,x,y):
        self.roomside = roomside
        self.roomheight = roomheight
        self.length = length
        self.width = width
        self.shape = shape
        self.x = x
        self.y = y

    #Accessors and Mutators
    @property
    def roomside(self):
        return self._roomside

    @roomside.setter
    def roomside(self,value):
        if(value > 0):
            self._roomside = value
        else:
            self._roomside = .1

    @property
    def roomheight(self):
        return self._roomheight

    @roomheight.setter
    def roomheight(self,value):
        if(value > 0):
            self._roomheight = value
        else:
            self._roomheight = .1
    
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self,value):
        if(value > 0):
            self._length = value
        else:
            self._length = .1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if(value > 0):
            self._width = value
        else:
            self._width = .1

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self,value):
        if(value == "oval"):
            self._shape = value
        else:
            self._shape = "rectangle"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        if(value > 0):
            if(value < self.roomside-self.width):
                self._x = value
            else:
                self._x = self.roomside - self.width
        else:
            self._x = 0

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        if(value > 0):
            if(value < self.roomheight-self.length):
                self._y = value
            else:
                self._y = self.roomheight - self.length
        else:
            self._y = 0

    def __str__(self):
        return self.shape
##########################################################################
