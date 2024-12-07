"""Escribir un programa que pregunte al usuario una cantidad a 
invertir, el interés anual y el número de años, y muestre por 
pantalla el capital obtenido en la inversión."""

cantidad_a_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual: "))
numero_de_anos = float(input("Ingrese el numero de años: "))
total_obtenido = round(cantidad_a_invertir*(interes_anual/100+1)**numero_de_anos),2

print(f"Usted Invirtió {int(cantidad_a_invertir)} con un interés de {interes_anual} durante {int(numero_de_anos)} años, por tanto obtuvo un total de {total_obtenido}")