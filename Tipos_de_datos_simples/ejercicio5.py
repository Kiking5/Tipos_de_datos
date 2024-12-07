"""Escribir un programa que pregunte al usuario por el número de 
horas trabajadas y el coste por hora. Después debe mostrar por 
pantalla la paga que le corresponde."""

print("Ingrese horas trabajadas: ")
horas = float(input()) #sin (float) el programa convierte el input en un string.
print(("Ingrese el valor de una hora: "))
valor_hora = float(input())
valor_a_pagar = (horas * valor_hora)
print(f"El valor a pagar es: {valor_a_pagar}")