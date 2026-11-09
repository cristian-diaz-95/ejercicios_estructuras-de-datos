def imprimir(Matriz):
    fils = len(Matriz)
    cols = len(Matriz[0])
    for f in range(fils): # Aqui recorro todas las filas 
        for c in range(cols):  # Aqui recorro las columnas de dicha fila
            print(Matriz[f][c], end="\t\t") # Imprimo cada elemento de la matriz
        print("") # Cambia de linea
def crear_matriz_vacia(n, valor_inicial=0):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            fila.append(valor_inicial)
        matriz.append(fila)
    return matriz
n=6
print("MATRIZ 1: ")
matriz_1 = crear_matriz_vacia(n)
contador = 1
for f in range(n):
    for c in range(n):
        matriz_1[f][c] = contador
        contador += 1
imprimir(matriz_1)
print("\n")

print("MATRIZ 2: ")
matriz_2 = crear_matriz_vacia(n)
for f in range(n):
    for c in range(n):
        if f % 2 == 0:
            matriz_2[f][c] = c + 1
        else:
            matriz_2[f][c] = n - c
imprimir(matriz_2)
print("\n")

print("MATRIZ 3: ")
matriz_3 = crear_matriz_vacia(n)
for f in range(n):
    for c in range(n):
        if f == c:
            matriz_3[f][c] = 1
imprimir(matriz_3)
print("\n")

print("MATRIZ 4: ")
matriz_4 = crear_matriz_vacia(n)
for f in range(n):
    for c in range(n):
        if f + c == n - 1:
            matriz_4[f][c] = 1
imprimir(matriz_4)
print("\n")

print("MATRIZ 5: ")
matriz_5 = crear_matriz_vacia(n)
for f in range(n):
    for c in range(n):
        if f >= c:
            matriz_5[f][c] = 1
imprimir(matriz_5)
print("\n")


print("MATRIZ 6: ")
matriz_6 = crear_matriz_vacia(n)
for f in range(n):
    for c in range(n):
        if f <= c:
            matriz_6[f][c] = 1
imprimir(matriz_6)
print("\n")


print("MATRIZ 7: ")
matriz_7 = crear_matriz_vacia(n)
contador_col = 1
for c in range(n): 
    for f in range(n): 
        matriz_7[f][c] = contador_col
        contador_col += 1
imprimir(matriz_7)
print("\n")


print("MATRIZ 8: ")
matriz_8 = crear_matriz_vacia(n, " ")
for f in range(n):
    for c in range(n):
        if f >= c: 
            if c % 2 == 0:
                matriz_8[f][c] = "A"
            else:
                matriz_8[f][c] = "B"
imprimir(matriz_8)