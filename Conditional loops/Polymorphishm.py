
from cmath import pi

class Figures():
    def area():
        pass
    def perimetro():
        pass

class Cuadrado(Figures):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        area = self.lado ** 2
        print(area)
    
    def perimetro(self):
        p = self.lado * 4
        print(p)

class Circulo(Figures):
    def __init__(self,radio):
        self.radio = radio
    
    def area(self):
        area = (pi)*(self.radio**2)
        print(area)
    
    def perimetro(self):
        p = 2*pi*self.radio
        print(p)

def main():
    c = Cuadrado(5)
    cir = Circulo(10)
    c.area()
    c.perimetro()
    cir.area()
    cir.perimetro()

if __name__ == "__main__":
    main()
        