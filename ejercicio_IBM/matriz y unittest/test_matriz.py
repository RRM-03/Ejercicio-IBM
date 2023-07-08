# Importamos el modulo de unittest y la matriz del archivo a comprobar con sus funciones
import unittest
from random import randint
from matriz import n_matriz
from matriz import sumar_filas
from matriz import sumar_columnas
from matriz import excepcion
  # Creamos una clase para guardar los resultados de los test
class Testmatriz(unittest.TestCase):
  # Prueba para verificar si la matriz se crea correctamente
 def test_n_matriz(self):
        n = 3
        matriz = n_matriz(n)
        self.assertEqual(len(matriz), n)
        for fila in matriz:
            self.assertEqual(len(fila), n)

 # Prueba para verificar si la función suma correctamente las filas
 def test_sumar_filas(self):
       
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        filas = sumar_filas(matriz)
        self.assertEqual(filas, [6, 15, 24])
 # Prueba para verificar si la función suma correctamente las columnas
 def test_sumar_columnas(self):
       
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        columnas = sumar_columnas(matriz)
        self.assertEqual(columnas, [12, 15, 18])
 
 # Prueba para verificar las excepciones
 def excepcion(self):
       
        with self.assertRaises(IndexError):
            excepcion(0, -int)
        with self.assertRaises(ValueError):
            excepcion('')

        




if __name__ == '__main__':
    unittest.main()

