import Punto
class Punto3D(Punto.Punto):
    def __init__(self,x,y,z):
        super(Punto3D, self).__init__(x,y)
        self.z = z

    def __str__(self):
        return "%d , %d, %d"  % (self.x, self.y, self.z)

h = Punto3D(1,2,3)
print(h)



