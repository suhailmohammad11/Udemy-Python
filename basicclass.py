class circle():
    pi=3.14
    def __init__(self,radius) :
        self.radius=radius
        self.area=self.pi * (radius**2)
        
    def circumference(self):
        return 2*self.pi*self.radius

result=circle(10)
print(result.area)
print(result.circumference())