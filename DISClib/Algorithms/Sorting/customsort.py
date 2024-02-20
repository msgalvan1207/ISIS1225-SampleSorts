"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
from DISClib.ADT import list as lt
assert cf

"""
El algoritmo de ordenamiento que se implementa en este módulo pueden ser:
    1) Tim Sort
    2) Bucket Sort

    El pseudocódigo para Tim Sort es:
        # TODO completar documentación

    Para mayor información sobre Tim Sort, ver:
        - https://en.wikipedia.org/wiki/Timsort
        - https://www.geeksforgeeks.org/timsort/
        # TODO completar con más referencias

    El pseudocódigo para Patience Sort es:
        # TODO completar documentación

    Para mayor información sobre Patient Sort, ver:
        - https://en.wikipedia.org/wiki/Patience_sorting
        - https://www.geeksforgeeks.org/patience-sorting/
        # TODO completar con más referencias
"""


def sort2(lst, sort_crit):
    """sort ordena una lista de elementos utilizando el algoritmo
    implementado por el usuario. puede ser Tim Sort o Patient Sort.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.

    Returns:
        list: La lista ordenada.
    """
    # TODO implementar el algoritmo de ordenamiento seleccionado lab 5
    # TODO cree todas las funciones y variables auxiliares que necesite
    # decide el tamaño de la corrida según el tamaño de la lista
    lt_size = lt.size(lst)
    min_run = setMinRun(lt_size)

    # ordena las corridas individuales de tamaño min_run
    for start in range(1, lt_size, min_run):
        end = min(start + min_run, lt_size)
        insertion(lst, sort_crit, start, end)

    # empieza a fusionar desde el tamaño min_run (o 32)
    size = min_run
    while size < lt_size:
        # selecciona el punto de inicio de la sublista izquierda
        # despues de cada merge, se aumenta el punto de inicio por 2*size
        for left in range(1, lt_size, 2 * size):
            # encontrar el punto final de la sublista izquierda
            # mid+1 es el punto de inicio de la sublista derecha
            mid = min(lt_size, left + size)
            right = min((left + 1 * size), (lt_size))
            # merge de las sublistas lst[left...mid] y lst[mid+1..right]
            if mid < right:
                merge(lst, sort_crit, left, mid, right)
        size = 2 * size
    return lst


# ===========================================
# Funciones auxiliares para Tim Sort
# ===========================================

# Rango mínimo del recorrido para el algoritmo Tim Sort
MIN_MERGE = 32


def setMinRun(n):
    """setMinRun calcula el recorrido minimo entre 23 y 64 para que la
    relación len(lst)/min_run sea igual o menor a una potencia de 2.

    Args:
        n (int): El tamaño de la lista a ordenar.

    Returns:
        int: El tamaño mínimo de la corrida.
    """
    R = 0
    while n >= MIN_MERGE:
        R |= n & 1
        n >>= 1
    min_run = n + R
    return min_run


def insertion(lst, sort_crit, left_idx, right_idx):
    """insertion ordena una lista de elementos utilizando con una variante
    del algoritmo de inserción entre los indices izquierdo (left_idx) y
    derecho (right_idx) con un recorrido de a lo sumo min_run.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario para
        comparar los elementos de la lista.
        left_idx (int): El índice izquierdo de la lista.
        right_idx (int): El índice derecho de la lista.

    Returns:
        list: La lista ordenada.
    """
    # TODO implementar la parte del insertion para el timsort en el lab 5
    for i in range(left_idx + 1, right_idx + 1):
        j = i
        while j > left_idx and sort_crit(lt.getElement(lst, j),
                                         lt.getElement(lst, j - 1)):
            lt.exchange(lst, j, j - 1)
            j -= 1


def merge(lst, sort_crit, left_idx, mid_idx, right_idx):
    """merge fusiona los recorridos previamente ordenados con el insertion.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario para
        comparar los elementos de la lista.
        left_idx (int): El índice izquierdo de la lista.
        mid_idx (int): El índice medio de la lista.
        right_idx (int): El índice derecho de la lista.

    Returns:
        list: La lista ordenada.
    """
    # el arreglo original se divide en dos partes, izquierda y derecha
    size1 = mid_idx - left_idx + 1
    size2 = right_idx - mid_idx
    # listas temporales con la misma configuración que la lista a ordenar
    struct_config = lst["type"]
    struct_cmp = lst["cmpfunction"]
    left_lt = lt.newList(struct_config,
                         cmpfunction=struct_cmp)
    right_lt = lt.newList(struct_config,
                          cmpfunction=struct_cmp)
    # esto es del mergesort
    for i in range(1, size1):
        lt.addLast(left_lt, lt.getElement(lst, left_idx + i))
    for i in range(1, size2):
        lt.addLast(right_lt, lt.getElement(lst, mid_idx + i + 1))

    # inicialización de los índices de trabajo
    i, j, k = 1, 1, left_idx

    # después de comparar, fusionamos esos dos arreglos
    while i < size1 and j < size2:
        temp1 = lt.getElement(left_lt, i)
        temp2 = lt.getElement(right_lt, j)
        if sort_crit(temp1, temp2):
            lt.changeInfo(lst, k, temp1)
            i += 1
        else:
            lt.changeInfo(lst, k, temp2)
            j += 1
        k += 1

    # copia cualquier elemento que quede en la izquierda
    while i < size1:
        temp1 = lt.getElement(left_lt, i)
        lt.changeInfo(lst, k, temp1)
        k += 1
        i += 1

    # copia cualquier elemento que quede en la derecha
    while j < size2:
        temp2 = lt.getElement(right_lt, j)
        lt.changeInfo(lst, k, temp2)
        k += 1
        j += 1


# ===========================================
# Funciones auxiliares para Patience Sort
# ===========================================

def sort(lst, sort_crit):

    # configura la estructura de datos para el algoritmo
    struct_config = lst["type"]
    struct_cmp = lst["cmpfunction"]
    # lista de pilas
    pile_lt = lt.newList(struct_config,
                         cmpfunction=struct_cmp)
    # recorre la lista de elementos
    for i in range(1, lt.size(lst)):
        # si la pila esta vacia
        if lt.isEmpty(pile_lt):
            # crea una nueva pila
            temp = lt.newList(struct_config)
            # agrega un nuevo elemento en la pila
            lt.addLast(temp, lt.getElement(lst, i))
            # agrega la nueva pila en el listado de pilas
            lt.addLast(pile_lt, temp)
        # de lo contrario
        else:
            # revisa si el elemento del tope de cada pila cumple con el orde
            flag = True
            size = lt.size(pile_lt)
            j = 1
            # recorre las pilas mientras el flag lo permita
            while j <= size and flag:
                # elemento por revisar
                cur = lt.getElement(lst, j)
                # elemento del tope de la pila
                top_pile = lt.lastElement(lt.getElement(pile_lt, j))
                # compara el elemento actual con el tope de la pila
                if sort_crit(cur, top_pile):
                    # agregael nuevo elemento en la pila
                    cur_pile = lt.getElement(pile_lt, j)
                    lt.addLast(cur_pile, lt.getElement(lst, i))
                    # actualiza el flag
                    flag = False
                j += 1
            # si el flag no se actualizó
            if flag is True:
                # crea una nueva pila
                temp = lt.newList(struct_config)
                # actualiza el nuevo elemento en la pila
                lt.addLast(temp, lt.getElement(lst, i))
                # agrega la nueva pila en el listado de pilas
                lt.addLast(pile_lt, temp)
    # fusiona las pilas en una sola lista ordenada
    ans = merge_pile(pile_lt, sort_crit)
    # retorna la lista ordenada
    lst = ans
    return lst


def merge_pile(pile_lt, sort_crit):
    # crea lista resultante con la misma configuración de la lista a ordenar
    struct_config = pile_lt["type"]
    struct_cmp = pile_lt["cmpfunction"]
    ans = lt.newList(struct_config,
                     cmpfunction=struct_cmp)

    # mientras haya pilas que revisar
    while not lt.isEmpty(pile_lt):
        # tome la primera pila asumiendo que es la más pequeña
        idx = 1
        cur_pile = lt.getElement(pile_lt, idx)
        minimum = lt.lastElement(cur_pile)
        # variable temporal para el ciclo
        i = 1
        # recorrer la lista de pilas
        while i <= lt.size(pile_lt):
            # toma el elemento del tope de la pila asumiendo que es mayor
            cur = lt.lastElement(lt.getElement(pile_lt, i))
            # si el minimo es mayor que el elemento de la pila actual
            if not sort_crit(minimum, cur):
                # se actualiza el minimo y el indice de la pila
                minimum = cur
                idx = i
            i += 1
        # agregar el minimo en la lista de resultado
        lt.addLast(ans, minimum)
        # si la pila actual no está vacía
        if not lt.isEmpty(cur_pile):
            # remueva el elemento de la pila
            lt.deleteElement(pile_lt, idx)
    # retorne la lista resultante
    return ans
