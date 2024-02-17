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
    return lst