#Importamos el modulo randint para generar los numeros aleatorios 
from random import randint

    
#Creamos una funcion para definir la matriz
def n_matriz(n):
    matriz= []
    
#Usamos el bucle for para ir rellenando cada fila  
    for i in range(n):
        matriz.append([])
# Con el for anidado rellenamos las columnas
        for j in range(n):
            matriz[i].append(randint(0, 9)) 
            
  #Con el return mandamos a la matriz los numneros
    return matriz

# Creamos la funcion para sumar las filas de la matriz
def sumar_filas(rellenar):
    filas = []
    for i in rellenar:
        filas.append(sum(i))
    return filas
# Creamos la funcion para sumar las columnas de la matriz
def sumar_columnas(rellenar):
    columnas = []
    for j in range(len(rellenar[0])):
        suma_columna = 0
        for i in range(len(rellenar)):
          suma_columna += rellenar[i][j]
        columnas.append(suma_columna)
    return columnas

# Creamos una excepcion para los errores de los valores 0, numero negativo y un caracter string
# Metemos dentro de la excepcion todo el codigo de ejecucion del programa
try:
   # Pedimos al usuario que introduzca un numero 

   num = int(input("Introduce  un  numero : \n"))
   # Creamos la varibale rellenar para mostrar la matriz
   
   rellenar = n_matriz(num)
  # Mostramos por pantalla la matriz generada
   
   print('la matriz genenerada es :', rellenar)

# Mostramos por pantalla la suma de filas y columnas
   print('la suma de las filas es :', sumar_filas(rellenar))
   print('la suma de las columnas es :', sumar_columnas(rellenar))
   
except IndexError : 
    print('El numero introducido es erroneo')

except ValueError :
    print('El numero introducido es erroneo')
