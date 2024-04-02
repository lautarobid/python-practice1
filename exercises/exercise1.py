"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5
area= lado_cuadrado*lado_cuadrado
print("El area del cuadrado es: ", area)

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado=lado_cuadrado**2
# COMPLETAR - FIN

assert area_cuadrado == 25

"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5
area_cuadrado=pow(lado_cuadrado, 2)
# COMPLETAR - INICIO
print("El area del cuadrado es:", area_cuadrado)
# COMPLETAR - FIN
assert area_cuadrado == 25

"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
cantidad_a_comprar=presupuesto_disponible//precio
cantidad_a_comprar=int(cantidad_a_comprar)
print("La cantidad maxima de unidades que se pueden comprar son: ", cantidad_a_comprar)

# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""
numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO

resultado_numero = numero_incalculable % 7

es_divisible_por_siete = (resultado_numero == 0)

assert es_divisible_por_siete
print("El número es divisible por 7")
# COMPLETAR - FIN

