print()
print(" calcular el area de un rectángulo")
print(" ---------------------------------\n")# el \n es un salto de liena


print()
base = input("Ingresar la base del rectángulo : ")
altura = input("Ingrese la altura del rectángulo :")

#        enetros
if base.isdigit() and altura.isdigit() :
    area = int(base) * int(altura) 
    print(f"El area del rectángulo es: {area}")
else:
    print("ERROR")
    print("Los valores ingresados deben ser numeros enteros") 
    print(f"valores ingresados base : {base}, altura : {altura}")


    