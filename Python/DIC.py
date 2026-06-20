print("Estructuras de datos en Python")
print("-----------------------------\n")



#Listas acepta cambios !!!
print("Listas (list)")
print("-------------")
#              0      1     2    3
fullstack = ["HTML","CSS","JS","PY"]
print(fullstack)

print(f"El tipo de dato es:{type(fullstack)}")#clase lista

#Acceder a elemento
print(fullstack [3]) 
print(fullstack [0])
print(fullstack [-1])
#Agregar elemento a lista
print("-------------")
fullstack.append("base de datos")
print(fullstack)
#Cambiar valor
print("-------------")
fullstack[0] = "HTML cambio valor"
print(fullstack)
#Lista de lisats
print("-------------")

simulnado_matiz = [
[1,2,3],
[4,5,6]

]
print(simulnado_matiz)

print("-------------")
print("Cadena de texto alvaro")
# una cadena de texto se comporta como una lista 
cadenadenatexto = "alvaro"
print(type(cadenadenatexto),cadenadenatexto[3])
print("-------------")

#----------------------------------------------------------------------

print("Tuplas")
#Tuplas no acepta cambios !!! 
titulo = "Tuplas (tuplas)"
print(titulo)
print(len(titulo) * "-")# len ecuenta elementos por ejemplo titulo tiene 15 si le quetamos el * "-"


curso = ("Bootscamp", "Fullstack","Python","2026")

print(curso)

print(f"El tipo de dato es: {type(curso)}") # type es la clase y esta es tuple 





print("-------------")
print("Set")

#Set no permite valores repetidos !!!
titulo = "Set (set)" 
print(titulo)
print("-" * len(titulo))

lenguajes = {"Python","JavaScript","PHP","Elixir","Java"}#si ponemos otrp java solo imprime 1 aun que tenga 2 o más

print(lenguajes)

print(f"El tipo de dato es: {type(lenguajes)}")

lista_duplicada = [1,2,3,4,1,6,1]
print("sin set")
print(lista_duplicada)
print("con set")
print(set(lista_duplicada))#aqui se hace eso que se menciona arriba 


lista_unicos = set(lista_duplicada)

print(lista_unicos)

lista_unicos.add(5)
print("agregamos con add un 5")
print(lista_unicos)








#Diccionarios

estudiante = {
    #clave       valor
    "nombre" : "Álvaro",
    "edad" : 28, 
    "curos" : "Python"
}

print(estudiante)
print( f"El tipo de dato es :{type(estudiante)}")


#Lista de diccionariso 
dict1 = {
    #clave       valor
    "nombre" : "Álvaro",
    "edad" : 28, 
    "curos" : "Python"
}
dict2 = {
    #clave       valor
    "nombre" : "Juan",
    "edad" : 30, 
    "curos" : "Python"
}
data = [dict1, dict2]

data_json = {
    "status" : "ok",
    "mesnaje" : "lista de estudaintes",
    "data" : [data]
 }

print(data_json)

#Forma 1 : Llamado directamente la clave
print("llamando la clave")
#      doble                             simple simple     doble
print(f"El nombre del estudiante es:{estudiante['nombre']}")


#Esto es para que si no hay uno sale el segundo con get
#                                                     1              2                 si no esta el primero pasa al segundo 
print(f"El nombre del estudiante es:{estudiante.get('apellido','No registrado')}")