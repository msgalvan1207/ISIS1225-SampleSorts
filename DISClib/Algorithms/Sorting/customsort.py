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

    El pseudocódigo para Bucket Sort es:
        # TODO completar documentación

    Para mayor información sobre Bucket Sort, ver:
        - https://en.wikipedia.org/wiki/Bucket_sort
        - https://www.geeksforgeeks.org/bucket-sort-2/
        # TODO completar con más referencias
"""


def sort(lst, sort_crit):
    """sort ordena una lista de elementos utilizando el algoritmo
    implementado por el usuario. puede ser Tim Sort o Bucket Sort.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.

    Returns:
        list: La lista ordenada.
    """
    # TODO implementar el algoritmo de ordenamiento seleccionado lab 5
    # TODO cree todas las funciones y variables auxiliares que necesite
    # decide el tamaño de la corrida
    n = lt.size(lst)
    minRun = setMinRun(n)

    # parte del insertion sort
    for start in range(1, n, minRun):
        end = min(start + minRun, n)
        insertion(lst, sort_crit, start, end)

    # parte del merge sort
    size = minRun
    while size < n:
        for left in range(1, n, 2 * size):
            mid = min(n, left + size)
            right = min((left + 1 * size), (n))
            if mid < right:
                merge(lst, sort_crit, left, mid, right)
        size = 2 * size
    return lst


# para Tim Sort
MIN_MERGE = 32


def setMinRun(n):
    """setMinRun calcula el tamaño mínimo de la corrida
    para el algoritmo Tim Sort.

    Args:
        n (int): El tamaño de la lista a ordenar.

    Returns:
        int: El tamaño mínimo de la corrida.
    """
    # TODO implementar el cálculo del tamaño mínimo de la corrida
    R = 0
    # toca explicar esto mejor
    while n >= MIN_MERGE:
        R |= n & 1
        n >>= 1
    return n + R


def insertion(lst, sort_crit, left_idx, right_idx):
    """insertion ordena una lista de elementos utilizando con una variante
    del algoritmo de inserción.

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario para
        comparar los elementos de la lista.
        left_idx (int): El índice izquierdo de la lista.
        right_idx (int): El índice derecho de la lista.

    Returns:
        list: La lista ordenada.
    """
    # esto es insertionsort casi que puro
    for i in range(left_idx + 1, right_idx + 1):
        j = i
        while j > left_idx and sort_crit(lt.getElement(lst, j),
                                         lt.getElement(lst, j - 1)):
            lt.exchange(lst, j, j - 1)
            j -= 1
            # lt[j], lt[j - 1] = lt[j - 1], lt[j]
            # j -= 1


def merge(lst, sort_crit, left_idx, mid_idx, right_idx):
    """merge fusiona las corridas ordenadas en una lista.

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
    # esto es del timsort
    size1, size2 = mid_idx - left_idx + 1, right_idx - mid_idx
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

    i, j, k = 1, 1, left_idx

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

    while i < size1:
        temp1 = lt.getElement(left_lt, i)
        lt.changeInfo(lst, k, temp1)
        k += 1
        i += 1

    while j < size2:
        temp2 = lt.getElement(right_lt, j)
        lt.changeInfo(lst, k, temp2)
        k += 1
        j += 1
