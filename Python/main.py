#COMENTARIO LINEA   
print("Hola mundo")

"""
ESTO ES UN COMENTARIO 
DE VARIAS 
LIENAS Y SE HACE CON 3 COMILLAS en ralidad es texto sin print ni variable....lo correcto es gato
"""
"""
TRABAJANDO CON VARIABLES 
    -NOMBRE (INIICIAR CON LETRA O GION BAJO_)
    -VALOR
    -TIPO DE DATO
"""
# ASIGNAR TIPO DE DATO

nombre = "Álvaro"
print(nombre)

# PARA PY TODO ES UN OBJETO 
print("Tipo de dato de la variable nombre:", type(nombre) )

print("alvaro" "catalan") 
#esto es igual a poner un + porque concatena queda alvarocatalan
#la coma , va si y solo si quiero dar dos argumentos(asi no hace salto de carro) 

# Metodos de variables 
print(nombre.upper())

apellido: str = "Catalán"

print(apellido, type(apellido))

#cambiar valor(otro tipo de dato) a una variable
apellido = 10
print(apellido, type(apellido))

#posicion de memoria de una variable 
#id es fuincion que permite conocer la posicion de memoria, donde esta almacenada la variable 
print(id(apellido))


#datos numericos 
edad = 25
print("Edad:", edad, type(edad), id(edad))

#numeros enteros 
numero_entero_1 = 10
numero_entero_2 = 20
print("Sumando numeros enteros:", numero_entero_1 + numero_entero_2)
print("Restando numeros enteros:", numero_entero_1 - numero_entero_2 , type(numero_entero_1 - numero_entero_2))
print("Multiplicacion numeros enteros:", numero_entero_1 * numero_entero_2 , type(numero_entero_1 * numero_entero_2,))
print("Division numeros enteros:", numero_entero_1 / numero_entero_2 , type(numero_entero_1 / numero_entero_2))
print("Division numeros enteros (int):", numero_entero_1 // numero_entero_2 , type(numero_entero_1 // numero_entero_2))
#siempre redonde apa abajo cuando forzamos el entero con //
#modulo o resto de la division lo que sobra el 2 entra 3 veces en el 7 y sobra 1 
print("Division (Modulo)", 7 % 2 , type(7 % 2 ))


#comprtamiento de cadena de texto
ciudad = "La Serena"
av = 10  #no podemos concatenar + un str con un int
print(ciudad + str(av)) #esto es conversion explicita 


#trabajando con input

print()
print("--------------------------")
print("Suma dos Numeros!")
print("--------------------------")
primer_numero = input("Ingreesa el primer numero:")
segundo_numero = input("Ingresa el segundo numero:")
#aqui concetamos los input
print("La suma de los dos numeros es:", primer_numero + segundo_numero)
print("La suma de los dos numeros es:", int(primer_numero) + int(segundo_numero))

#usando f string

suma_str = f"La suma de {primer_numero} con {segundo_numero} es: {int(primer_numero)+int(segundo_numero)}"

print(suma_str)