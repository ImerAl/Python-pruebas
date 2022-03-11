#abs para el valor absoluto
x= -15
print(abs(x))

k = (5 - 6j) #Numero complejo
print(abs(k))

#round redondea un decima
print(round(7.93231,2))

#Range --- range(start, stop, step)

for i in range(1,20,2):
    print(i,end=" ")

a_list = ['Weon', 'Qliao','Wea','Fome']
for i in range(len(a_list)):
    print(a_list[i], end =" ")

#Timeit() measure time of execution
#type() te devuelve el tipo de un objeto
#Enumerable devuelve una coleccion de tuplas


x = ["W","A","C","H","O"]
e = enumerate(x)
print(list(e))

#Imprimir en la misma linea
print("Viva er", end=" ")
print("Betih")