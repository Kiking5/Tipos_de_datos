"""Escribir un programa que pida al usuario su peso (en kg) y estatura 
(en metros), calcule el índice de masa corporal y lo almacene en 
una variable, y muestre por pantalla la frase Tu índice de masa 
corporal es <imc> donde <imc> es el índice de masa corporal calculado 
redondeado con dos decimales."""

print("El Indice de masa corporal es ((Peso(kg))/((altura(cm))^2))*10000")
peso = float(input("¿Cual es tu peso en Kg? "))
altura = float(input("¿Cual es tu altura en cm? "))
imc = (((peso)/(altura**2))*10000)
imc_redondeado = round(imc,2)
print(f"Su peso es {peso}kg, su altura es {altura}cm, por lo tanto \n su indice de masa corporal es {imc_redondeado}")
