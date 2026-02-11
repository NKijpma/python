
class persoon:
    def __init__(self,naam,leeftijd):
        self.naam =naam
        self.leeftijd= leeftijd
        
    def perkoon(self):
        print(f"hoi mij naam is {self.naam} en ik ben {self.leeftijd} oud ")
p1 =persoon ("jeroen",63)
p2 =persoon("jasmijn",31)

p1.perkoon()
p2.perkoon()

class hond:
    def __init__(self,naam,ras):
        self.naam = naam
        self.ras = ras
    def daggoe(self):
        print(f"mijn hond heet {self.naam}en zijn ras is {self.ras}")
d1= hond ("spike","kooiker")
d2= hond ("amu","corgi")

d1.daggoe()
d2.daggoe()

class calc:
    def __init__(self,a,b):
     self.a=(int)(input("Enter a"))
     self.b=(int)(input("Enter b"))
