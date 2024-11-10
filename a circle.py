class circle():
    def __init__(self, radius):
        self.radius = int(radius)
    
    def calc_area(self):
        return 3.14*self.radius*self.radius
    
    def calc_perimeter(self):
        return 2*3.14*self.radius
# C1 = circle(3)
cir2 = circle(2)
area = cir2.calc_area()
print(area)
# perimeter = C1.calc_perimeter()
# print(perimeter)

