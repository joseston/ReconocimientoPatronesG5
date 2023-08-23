import numpy as np
import pandas as pd

# 1. Crea una lista de 10 números e imprime los valores negativos en otra lista.
lista_numeros = [10, -2, 3, -5, 6, -1, 7, 9, -3, 4]
valores_negativos = [n for n in lista_numeros if n < 0]
print("Valores negativos:", valores_negativos)

# 2. Escribe una matriz de 3x3 con números float distintos.
matriz_float = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
print("Matriz de float:", matriz_float)

# 3. Crea una matriz A de 3x3 y 2 matrices (B y C) de 3x1 con números enteros distintos y calcula AxB+C.
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[1], [2], [3]])
C = np.array([[3], [2], [1]])
resultado = A.dot(B) + C
print("Resultado de AxB+C:", resultado)

# 4. Disponer de números enteros desde el 1 hasta el 100 y cambiar los múltiplos de 3 por el string “m3”.
multiplos_de_tres = ['m3' if x % 3 == 0 else x for x in range(1, 101)]
print("Múltiplos de 3 cambiados:", multiplos_de_tres)

# 5. Recorriendo la matriz A del ejercicio 3, calcular la traza de la matriz transpuesta.
traza = np.trace(A.T)
print("Traza de la matriz transpuesta:", traza)

# 6. Si eliminamos la letra “a” de la pregunta anterior cuántas letras se obtienen.
texto_pregunta = "Si eliminamos la letra “a” de la pregunta anterior cuántas letras se obtienen."
letras_sin_a = texto_pregunta.replace("a", "")
print("Cantidad de letras sin 'a':", len(letras_sin_a))

# 7. ¿Cuál es la palabra más frecuente en toda la prueba?
palabras = texto_pregunta.split()
palabra_frecuente = pd.Series(palabras).value_counts().idxmax()
print("Palabra más frecuente:", palabra_frecuente)

