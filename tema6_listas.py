#Generando la lista
nombres=["Juan","Mario","Lara"]
numeros=[1, 2, 3, 4, 5]
datos=[1, 2.5, "Mario",True]

#Cambiando el valor de la lista nombres en la posicion 0
nombres[0]="Roberto"

#Imprimiendo en distintas poiciones
print(nombres[:])
print(nombres[:2])
print(nombres[:3])
print(nombres[1:])

#Agregando a la lista nombres el valor Dario
nombres.append("Dario")
print(nombres)

nombres.insert(2,"Maria")
print(nombres)

nombres.extend(["chencha",2 , 23, 5])
print(nombres)

#Quitando un valor de la lista
nombres.remove("chencha")
print(nombres)

#Elimina el ultimo elemento
nombres.pop()
print(nombres)


#Multiplica elementos de la lista
n = "Juan"
n2 = n*5
print(n2)
print(nombres)


#Elimina una posicion
del nombres[2]
print (nombres)