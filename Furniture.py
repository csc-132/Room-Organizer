class Furniture(object):

    def __init__(self,name,length,width):
        self.length = length
        self.width = width
        self.name = name
        self.x = 0
        self.y = 0

    #Accessors and Mutators
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
        
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
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        if(value > 0):
            self._x = value
        else:
            self._x = 0

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        if(value > 0):
            self._y = value
        else:
            self._y = 0

    def __str__(self):
        return self.name
##########################################################################
