
#Creando la tupla
tupla=(1,2,3,2,2)

#Imprimiendo
print(tupla)

#Imprimiendo el tipo
print(type(tupla))

#Asignado valores a una nueva tupla
tupla2=(7, "Roberto", True, 23.8, 16 + 17j)

#Imprimiendo la nueva tupla
print(tupla2)

#Imprimiendo tupla en la posicion 1
print(tupla2[1])

#Imprimiendo tupla en la posicion 4
print(tupla2[4])

#Imprimiendo tupla en la posicion -1
print(tupla2[-1])

#Imprimiendo tupla de la posicion 0 a la 3
print(tupla2[0:3])

#Asigna el primer elemento de la tupla a "a" el segundo a "b" y el tercero a "c"
a, b, c = tupla

print(a)
print(c)
tuplaN = tupla + tupla2
print(tuplaN)
print(tupla.count(2))

tupla[2]=23