# Función para ordenar un vector de forma ascendente
def orden_ascendente(vector):
    return sorted(vector)

# Función para ordenar un vector de forma descendente
def orden_descendente(vector):
    return sorted(vector, reverse=True)

# Ejemplo de uso
vector = [5, 2, 9, 1, 7]

# Ordenar el vector de forma ascendente
vector_ascendente = orden_ascendente(vector)
print("Vector ordenado de forma ascendente:", vector_ascendente)

# Ordenar el vector de forma descendente
vector_descendente = orden_descendente(vector)
print("Vector ordenado de forma descendente:", vector_descendente)
