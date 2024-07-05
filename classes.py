import debug_mode
import better_math as math
from functools import lru_cache
class point(debug_mode.Base):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.color=(int(x/100*255),int(y/100*255),int(z/100*255))
    @lru_cache(maxsize=1024)
    def prj(self,screen):
        b=math.matrix_multiply(screen.a,((self.x-screen.xpos,),(self.y-screen.ypos,),(self.z-screen.zpos,)))
        return [math.round(b[0][0]+screen.width/2),math.round(b[1][0]+screen.height/2)]
    def run(self,func):
        func(self)
class screen():
    def __init__(self, width, height,xangle,yangle,zangle, xpos,ypos,zpos):
        self.width = width
        self.height = height
        self.xangle = xangle
        self.yangle = yangle
        self.zangle = zangle
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
    def __setattr__(self, obj, value):
        if obj=="xangle":
            self.xangle=value
        elif obj=="yangle":
            self.yangle=value
        elif obj=="zangle":
            self.zangle=value
        else:
            super().__setattr__(obj, value)
        try:
            self.a=math.matrix_multiply(math.matrix_multiply(((1,0,0),
                                                         (0,math.cos(self.xangle),-math.sin(self.xangle)),
                                                         (0,math.sin(self.xangle),math.cos(self.xangle))),
                                                        ((math.cos(self.yangle),0,math.sin(self.yangle)),
                                                         (0,1,0),
                                                         (-math.sin(self.yangle),0,math.cos(self.yangle)))),
                                    ((math.cos(self.zangle),-math.sin(self.zangle),0),
                                    (math.sin(self.zangle),math.cos(self.zangle),0),
                                    (0,0,1)))
        except:
            pass
class face():
    def __init__(self,points):
        self.data=points
    def run(self,func):
        for i in self.data:
            func(i)
class polyhedron():
    def __init__(self,faces):
        self.data=faces
    def run(self,func):
        for i in self.data:
            i.run(func)
class cube(polyhedron):
    def __init__(self, x, y, z, size):
        super().__init__([])
        x-=size/2
        y-=size/2
        z-=size/2
        self.data=[face([point(x+i,y+j,z+size) for i in range(size) for j in range(size)]),
                   face([point(x+i,y+size,z+j) for i in range(size) for j in range(size)]),
                   face([point(x+size,y+i,z+j) for i in range(size) for j in range(size)]),
                   face([point(x+i,y+j,z) for i in range(size) for j in range(size)]),
                   face([point(x+i,y,z+j) for i in range(size) for j in range(size)]),
                   face([point(x,y+i,z+j) for i in range(size) for j in range(size)]),]
class scene():
    def __init__(self,polyhedrons):
        self.data=polyhedrons
    def run(self,func):
        for i in self.data:
            i.run(func)