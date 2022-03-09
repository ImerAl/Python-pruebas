#Cuenta los elementos de un string
#string.count(char/substring, start index, end index)

var = "Bicho"
c = var.count("i",0,7)
print(c)

#format
print("Madre mia el {}".format(var))

#len() retorna la logintud
print(len(var))

#find() busca el substring, find(substring,start(optional),end(optional))
print(var.find("c"))

#split() separa el string dependiendo del separador
s = "Even if you win, you're still a rat"
f = s.split(",")
print(f)
