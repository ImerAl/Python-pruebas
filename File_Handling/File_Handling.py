#Crear y abrir un file
file = open("example.txt","w+")

#Escribir
for i in range(10):
    file.write("Viv er Betih %d\r\n" % (i+1))

#Cerrar
file.close()

#Agregar mas
file = open("example.txt","a+")

for i in range(2):
    file.write("Vamoh mi Betih %d\r\n" % (i+1))

file.close

#Leer
file = open("example.txt", "r")

if file.mode == "r":
    content = file.read()
    print(content)

