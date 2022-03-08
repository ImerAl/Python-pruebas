from OOP import MyClass

class DerivedClass(MyClass): #Herencia
    def method3(self):
        print("Mamahuevazo")

def main():
    d = DerivedClass()
    d.method3()
    d.method2("xD")

if __name__ == "__main__":
    main()
