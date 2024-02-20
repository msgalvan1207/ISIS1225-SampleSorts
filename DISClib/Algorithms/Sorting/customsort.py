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
El algoritmo de ordenamiento que se implementa en este módulo puede ser:
    1) Tim Sort 
    ó
    2) Bucket Sort

    El pseudocódigo para Tim Sort es:
        Function timSort(arr, n)
            min_run = 32
            For i = 0 to n step min_run
                insertionSort(arr, i, min(i+min_run-1, n-1))
            End For
            current_size = min_run
            While current_size < n
                For left = 0 to n step 2*current_size
                    mid = min(left + current_size - 1, n-1)
                    right = min(left + 2*current_size - 1, n-1)
                    merge(arr, left, mid, right)
                End For
                current_size = current_size * 2
            End While
        End Function

    El pseucodógido para el algoritmo de ordenamiento por inserción es:
        Function insertionSort(arr, left, right)
            For i = left+1 to right
                j = i
                While j > left and arr[j] < arr[j-1]
                    swap(arr[j], arr[j-1])
                    j = j-1
                End While
            End For
        End Function

    El pseudocódigo para el algoritmo de ordenamiento por merge es:
        Function merge(arr, left, mid, right)
            len1 = m - l + 1
            len2 = r - m
            l = new Array(len1)
            r = new Array(len2)
            For i = 0 to len1
                l[i] = arr[l + i]
            End For
            For i = 0 to len2
                r[i] = arr[m + 1 + i]
            End For
            i = 0
            j = 0
            k = l
            While i < len1 and j < len2
                If l[i] <= r[j]
                    arr[k] = l[i]
                    i = i + 1
                Else
                    arr[k] = r[j]
                    j = j + 1
                End If
                k = k + 1
            End While
            While i < len1
                arr[k] = l[i]
                i = i + 1
                k = k + 1
            End While
            While j < len2
                arr[k] = r[j]
                j = j + 1
                k = k + 1
            End While
        End Function

    Para mayor información sobre Tim Sort, ver:
        - https://en.wikipedia.org/wiki/Timsort
        - https://www.geeksforgeeks.org/timsort/
        - https://www.youtube.com/watch?v=_dlzWEJoU7I

        
    El pseuocodigo para patience sort es:
        Function patienceSort(arr, n)
            piles = 0
            top = new Array(n)
            for i = 0 to n
                left = 0
                right = piles
                while left < right
                    mid = (left + right)/2
                    if arr[i] > top[mid]
                        left = mid + 1
                    else
                        right = mid
                    end if
                end while
                if left == piles
                    piles = piles + 1
                end if
                top[left] = arr[i]
            end for
            return piles
        End Function

        
    Para mayor información sobre Patience Sort, ver:
        - https://en.wikipedia.org/wiki/Patience_sort
        - https://www.geeksforgeeks.org/patience-sort/
        - https://www.youtube.com/watch?v=K9M6g7BiBX4

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
    return lst