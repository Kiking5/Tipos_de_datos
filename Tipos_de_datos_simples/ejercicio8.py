"""Escribir un programa que pida al usuario dos números enteros 
y muestre por pantalla la <n> entre <m> da un cociente <c> y un 
resto <r> donde <n> y <m> son los números introducidos por el 
usuario, y <c> y <r> son el cociente y el resto de la división 
entera respectivamente."""

n = int(input("Ingrese un numero 'Dividendo' : "))
m  = int(input("Ingrese un nunmero divisor: "))
r = n % m
c = n / m

print(f"{n} dividido entre {m} de un cociente de {int(c)} y un resto de {int(r)}")

# Graficar en una hoja ayuda mucho a la facil comprension