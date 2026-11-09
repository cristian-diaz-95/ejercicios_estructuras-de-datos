def solucion(a):
    peso_equipo1 = 0
    peso_equipo2 = 0
    
    for i in range(len(a)):
        if i % 2 == 0:
            peso_equipo1 += a[i]
        else:
            peso_equipo2 += a[i]
            
    return [peso_equipo1, peso_equipo2]