"""Una juguetería tiene mucho éxito en dos de sus productos: payasos 
y muñecas. Suele hacer venta por correo y la empresa de logística les 
cobra por peso de cada paquete así que deben calcular el peso de los 
payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso 
pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número 
de payasos y muñecas vendidos en el último pedido y calcule el peso 
total del paquete que será enviado."""

peso_payaso = 112
peso_muneca = 75
cantidad_payasos = float(input("Ingrese la cantidad de payasos a enviar: "))
cantidad_munecas = float(input("Ingrese la cantidad de muñecas a enviar: "))

peso_payasos_total = peso_payaso*cantidad_payasos
peso_munecas_total = peso_muneca*cantidad_munecas

peso_total = peso_payasos_total+peso_munecas_total
print(f"El peso tota a enviar es de {(peso_total/1000)} kg para enviar.")