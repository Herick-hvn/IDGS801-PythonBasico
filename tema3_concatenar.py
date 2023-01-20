#Generando cadenas
texto1= "Hola" 
texto2= "Mundo¡¡" 

#concatenando las cadenas e imprimiendo
textoFinal= texto1+" "+texto2
print(textoFinal)

#Otra manera de imprimir
print ("El saludo es: %s %s" %(texto1,texto2))

#Otra manera de imprimir pero por posicion
candena = "Saludar dos: {1} {0}".format(texto1, texto2) 
print(candena)

candena = "Saludar dos: {x} {y}".format(x = texto1, y = texto2) 
print(candena)