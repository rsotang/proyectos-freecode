class Rectangle:
    width=0
    height=0

    def __init__(self,width,height):
        self.width = width
        self.height=height
        print('construido')


    def set_width(self,width):
        self.width = width
        
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width **2 + self.height ** 2)** .5

    def get_picture(self):    
        picture=''
        if self.width > 50 or self.height>50:
            return 'Too big for picture.'
        else:  

            for i in range(self.height):
                line=''
                while len(line) < self.width:

                    line += '*'
                line += '\n'
                picture += line 
            
            return picture

    def get_amount_inside(self,shape):
        fitting_times = self.get_area() // shape.get_area()
        return fitting_times

    def __str__(self):
        str_out = 'Rectangle(width='+str(self.width)+', height=' + str(self.height)+')'
        return str_out

####################################################################

class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side
        
    
    def set_side(self,side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self,width):
        self.width = width
        self.height = width
        
    def set_height(self,height):
        self.height = height
        self.width = height

    def __str__(self):
        str_out = 'Square(side='+str(self.width)+')'
        return str_out

        

###################################################

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))