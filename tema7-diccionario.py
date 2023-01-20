#Generando el diccionario
miDiccionario = {"Matricula":12344, "Nombre":"Dario", "edad":23,}

print(type(miDiccionario))
print(miDiccionario)

#Cambiamos el nombre del diccionario
miDiccionario["Nombre"]="Panfilo"
print(miDiccionario["edad"])

#Imprime valores
print(miDiccionario.values())
#Imprime indices
print(miDiccionario.keys())