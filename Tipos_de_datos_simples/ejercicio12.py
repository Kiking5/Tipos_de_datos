"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no
es el día tiene un descuento del 60%. Escribir un programa que comience
leyendo el número de barras vendidas que no son del día. Después el
programa debe mostrar el precio habitual de una barra de pan, el 
descuento que se le hace por no ser fresca y el coste final total."""

valor_barra_de_pan = 3.49

descuento = 0.60
precio_con_descuento = valor_barra_de_pan * (1 - descuento)
cantidad_vendida = int(input("Ingrese la cantidad de barras que no son del día vendidas: "))

# Mostrar los cálculos
print(f"El precio habitual de la barra de pan es, {round(valor_barra_de_pan, 2)}, €")
print(f"El precio con el '60%' de descuento es, {round(precio_con_descuento, 2)}, €")
print(f"El total sin descuento sería, {round(valor_barra_de_pan * cantidad_vendida, 2)}, €")
print(f"El total con descuento es, {round(precio_con_descuento * cantidad_vendida, 2)}, €")
