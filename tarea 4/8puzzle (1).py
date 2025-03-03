from collections import deque

# Definir el objetivo del puzzle
ESTADO_OBJETIVO = (1, 2, 3,
                   4, 5, 6,
                   7, 8, 0)

# Función para imprimir el estado del puzzle
def imprimir_puzzle(estado):
    for i in range(0, 9, 3):
        fila = estado[i:i+3]
        print(" ".join(str(num) if num != 0 else ' ' for num in fila))
    print()

# Función para encontrar los vecinos (movimientos posibles)
def obtener_vecinos(estado):
    vecinos = []
    indice = estado.index(0)
    fila, columna = divmod(indice, 3)
    movimientos = []
    if fila > 0:
        movimientos.append((-1, 0))  # Arriba
    if fila < 2:
        movimientos.append((1, 0))   # Abajo
    if columna > 0:
        movimientos.append((0, -1))  # Izquierda
    if columna < 2:
        movimientos.append((0, 1))   # Derecha

    for movimiento in movimientos:
        nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
        nuevo_indice = nueva_fila * 3 + nueva_columna
        nuevo_estado = list(estado)
        nuevo_estado[indice], nuevo_estado[nuevo_indice] = nuevo_estado[nuevo_indice], nuevo_estado[indice]
        vecinos.append(tuple(nuevo_estado))
    return vecinos

# Función para reconstruir el camino desde el estado inicial hasta el objetivo
def reconstruir_camino(viene_de, actual):
    camino = [actual]
    mientras_actual = actual
    while mientras_actual in viene_de:
        mientras_actual = viene_de[mientras_actual]
        camino.append(mientras_actual)
    camino.reverse()
    return camino

# BFS (Búsqueda en Anchura)
def bfs(estado_inicial):
    print("=== BFS (Búsqueda en Anchura) ===")
    frontera = deque([estado_inicial])
    viene_de = {}
    explorados = set()

    while frontera:
        actual = frontera.popleft()
        if actual == ESTADO_OBJETIVO:
            camino = reconstruir_camino(viene_de, actual)
            return camino
        explorados.add(actual)
        for vecino in obtener_vecinos(actual):
            if vecino not in explorados and vecino not in frontera:
                frontera.append(vecino)
                viene_de[vecino] = actual
    return None

# Función para mostrar el camino paso a paso
def mostrar_solucion(camino):
    if not camino:
        print("No se encontró solución.")
        return
    print(f"Se encontraron {len(camino)-1} movimientos.\n")
    for i, estado in enumerate(camino):
        print(f"Paso {i}:")
        imprimir_puzzle(estado)

# Función principal
def main():
    print("Juego del 8-Puzzle")
    print("Ingresa el estado inicial del puzzle (usa 0 para el espacio vacío):")
    estado_inicial = []
    while True:
        entrada = input("Ingresa los 9 números separados por espacios (ejemplo: 1 2 3 4 5 6 7 8 0): ")
        partes = entrada.strip().split()
        if len(partes) != 9:
            print("Por favor, ingresa exactamente 9 números.")
            continue
        try:
            estado_inicial = tuple(int(num) for num in partes)
            if set(estado_inicial) != set(range(9)):
                print("Los números deben ser del 0 al 8 sin repetirse.")
                continue
            break
        except ValueError:
            print("Por favor, asegúrate de ingresar números válidos.")

    print("\nEstado Inicial:")
    imprimir_puzzle(estado_inicial)
    camino = bfs(estado_inicial)
    mostrar_solucion(camino)

if __name__ == "__main__":
    main()