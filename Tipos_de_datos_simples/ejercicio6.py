"""Escribir un programa que lea un entero positivo, (n)
, introducido por el usuario y después muestre en pantalla la suma 
de todos los enteros desde 1 hasta(n). La suma de los (n) primeros enteros 
positivos puede ser calculada de la siguiente forma:
(https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/)"""

n = int(input("Ingresa un numero para iniciar el programa: "))
suma = ((n)*(n+1))/2
print(f"La suma de todos los numeros hata {n} es: {suma}")