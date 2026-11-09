
filas=int(input("ingrese cantidad de dias: "))
columnas=int(input("ingrese la cantidad de productos: "))
matVentas=[]
def crear_matrix():
    matrix=[]
    for f in range(1,filas+1):
        p=input(f"cantidad de ventas dia {f}: ")
        matrix.append(p)
        
        
    return matrix
for c in range (1,columnas+1):
    print(f"ventas del producto {c}: ")
    matrix=crear_matrix()
    matVentas.append(matrix)  
print(matVentas)   

lstPrecios = []
for i in range(1,columnas+1):
    a=int(input(f"ingrese precio del producto {i}"))
    lstPrecios.append(a)

def lstTotalesProdxSem(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for f in range(fils):
        suma = 0
        for c in range(cols):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)

def lstdiaventas(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    lstTotalesdias = []
    for c in range(cols):
        suma = 0
        for f in range(fils):
            suma += ventas[f][c] * precios[f]
        lstTotalesdias.append(suma)

    return lstTotalesdias

lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)
listTotalesdias=lstdiaventas(matVentas,lstPrecios)
maxtotaldias=max(listTotalesdias)
maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal) + 1
ventamaxdia=listTotalesdias.index(maxtotaldias)+1

print(f"El producto {prodVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")
print(f"El dia de la semana con mas ventas es el dia numero {ventamaxdia}")