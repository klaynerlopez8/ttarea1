num1=int(input("ingrese un numero entero:"));
nun2=int(input("ingrese otro numero entero:"));
num3=int(input("ingrese otro numero entero:"))
suma=num1+nun2+num3
promedio=suma//3;
if promedio%2==0:
    mensaje = promedio,"el promedio es un numero par"
else:
    mensaje = promedio, "el promedio es un numero impar"
print(mensaje);