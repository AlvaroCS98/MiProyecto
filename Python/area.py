base = input("Ingresar la base del rectangulo : ")
altura = input("Ingrese la altura del rectangulo :")

#        enetros
if base.isdigit() and altura.isdigit() :
    area = int(base) * int(altura) 
    print(f"El area del rectangulo es: {area}")
else:
    print("ERROR")
    print("Los valores ingresados deben ser numeros enteros") 
    print(f"valores ingresados base : {base}, altura : {altura}")


    