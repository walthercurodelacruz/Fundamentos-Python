
#creando una lista (se pueden modificar)
lista = ["Walther De la Cruz",True, 1.85, "De La Cruz"] 

#creando una tupla (no pueden modificar)
tupla = ("Walther Curo",True, 1.85, "De La Cruz")

#esto es vàlido
#lista[3] = "Instructor"

#esto no
#tupla[3] = "Instructor"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Walther Curo",True, 1.85, "De La Cruz"}


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Walther Curo De La Cruz",
    'Entidad' : "SENATI",
    'Estado' : True,
    'altura' : 1.72,
    'dato_duplicado' : "Walther Curo De La Cruz"
}

print(diccionario['Entidad'])



