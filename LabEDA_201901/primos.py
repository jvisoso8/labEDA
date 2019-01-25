#
#   serie de programas de ejemplo
#
# ------------------------------------------------------------------------
# Por RGGH
# Enero de 2019
# para EDA
# ------------------------------------------------------------------------
# Se implementan como funciones para un número n dado (no verifica si n es entero positivo)
#
import sys
import time
#
# Ejemplo 1.- Determinar si un número es primo a partir de la definición directa
#
def primo_00( n ):
#
# intentamos dividir el número entre los números inferiores a él partiendo del 2
# si algún número d menor que n lo divide entonces no es primo
#
  d = 2
  while n % d != 0:
      if d == 2:
          d = 3
      else: d+= 2
  #
  # Se revisa el d que dividió a n
  #
  if d == n:
      print(str(n) + " es primo")
      es_primo = True
  else:
      print(str(n) + " no es primo, lo divide " + str(d))
      es_primo = False
  return es_primo    
      
#
# -------------------------------------------------------------------------------------------------------
#
# Ejemplo 2.- Aplicamos el principio de Eratóstenes: Un número entero positivo es primo si no es divisible
# entre los primos inferiores a él cuyo cuadrado no lo sobrepasen.
#
def primo_01(n):
    d = 2
    ban = True
    while ban:
        ban = n % d != 0 and d * d < n
        if ban:
            if d == 2:
                d = 3
            else:
                d += 2
    if n % d != 0:
        print(str(n) + " es primo")
        es_primo = True
    else:
        print(str(n) + " no es primo, pues divisible entre " + str(d))
        es_primo = False
    return es_primo    
#
# Ejercicio 3.- Encontrar los K primos menores o iguales a sys.maxsize
#
def primosGrandes(K):
  w = sys.maxsize #1234567423
  #w = 2**31 - 1  
#
# sys.maxsize debe ser impar, pero por si las moscas...
#
  if w % 2 == 0:
    w -= 1
  v = 0
  
  while v <= K:
     if primo_01(w):
         v += 1
     w -= 2
#
# Ejercicio 4.- Encontrar los K primos menores o iguales a sys.maxsize
#
def descompon(n):
  d = 2
  factores = {}
  while n > 1:
    pot = 0
    while n % d == 0:
      pot += 1
      n = n // d
    if pot > 0:
      factores.update({d:pot})
    if d == 2:
      d = 3
    else:
      d += 2
  return factores
#
# ============================ Programa Principal ====================
#

print(descompon(125))
     
##t0 = time.time()
##primosGrandes(10)
##t1 = time.time()
##print(t1-t0)



#
# ===================== Fin del programa Principal ====================
#

