from .arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]

        # Extraer nodo
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, []):
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None


def obtener_camino(nodo_solucion, estado_inicial):
    if nodo_solucion is None:
        return []

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    return resultado