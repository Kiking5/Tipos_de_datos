"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece 
el 4% de interés al año. Estos ahorros debido a intereses, que no se 
cobran hasta finales de año, se te añaden al balance final de tu cuenta 
de ahorros. Escribir un programa que comience leyendo la cantidad de 
dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad 
a dos decimales."""

deposito = float(input("¡Ingrese su dinero!"))
print(f"usted ingreso {deposito} pesos. \n el interes anual es de 4%")
interes = (4/100)+1
primer_ano = interes*deposito
print(f"Al finalizar el primer año usted tendra: {interes*deposito}")
segundo_ano = interes*primer_ano
print(f"Al finalizar el segundo año usted tendra: {interes*primer_ano}")
tercer_ano = interes*segundo_ano
print(f"Al finalizar el tercer año usted tendra: {interes*segundo_ano}")