num1=int(input("ingrese un numero entero:"));
nun2=int(input("ingrese otro numero entero:"));
num3=int(input("ingrese otro numero entero:"));
if num1 > nun2 and num1>num3:
    mensaje="el numero mayor es:",num1,
elif nun2>num1 and nun2>num3:
    mensaje = "el numero mayor es:", nun2
else:
    mensaje = "el numero mayor es:",num3
print(mensaje);