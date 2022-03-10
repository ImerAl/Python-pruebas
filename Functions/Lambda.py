#Funcion anonima con solo 1 expresion dentro

suma = lambda x , y : x + y
print(suma(1,2))

wea = lambda s : print(s)
wea("Pupusas de FQ")

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))