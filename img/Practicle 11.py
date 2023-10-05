class sphere:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def diameter(self):
        d=self.r*2
        print("Daimeter of a sphere is : ",d)
    def circumference(self):
        c=2*self.pi*self.r
        print("circumference of a sphere is : ",c)
    def volume(self):
        v=4/3*self.pi*self.r*self.r*self.r
        print("Volume of a sphere is : ",v)
s=sphere(3.14,6)
s.diameter()
s.circumference()
s.volume()
