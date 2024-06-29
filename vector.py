from premium_math import *
from fractions import *
class point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def prj(self,screen):
        x=self.x-screen.A*Fraction((screen.A*self.x+screen.B*self.y+screen.C*self.z+screen.D),(screen.A**2+screen.B**2+screen.C**2))
        y=self.y-screen.B*Fraction((screen.A*self.x+screen.B*self.y+screen.C*self.z+screen.D),(screen.A**2+screen.B**2+screen.C**2))
        z=self.z-screen.C*Fraction((screen.A*self.x+screen.B*self.y+screen.C*self.z+screen.D),(screen.A**2+screen.B**2+screen.C**2))
        return point(x,y,z)
    def run(self,func,screen):
        
        func(point(self.x, self.y, self.z).prj(screen)[1], point(self.x, self.y, self.z).prj(screen)[2])
    def __getitem__(self, item):
        if item==0:
            return self.x
        elif item==1:
            return self.y
        elif item==2:
            return self.z
        else:
            return None
    def __str__(self):
        return "point("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
class line():
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

class face():
    def __init__(self,points):
        self.data=points
    def run(self,func,screen):
        for i in self.data:
            i.run(func,screen)
class screen():
    def __init__(self,A,B,C,D):
        self.A=A
        self.B=B
        self.C=C
        self.D=D
    def __contains__(self,dot):
        if self.A*dot.x+self.B*dot.y+self.C*dot.z+self.D==0:
            return True
        else:
            return False