"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribuciones
 *
 * Dario Correal
 """

import config as cf
import sys
import controller
import itertools
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x libros por promedio")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Selecccionar algoritmo de ordenamiento")
    print("6- Seleccionar muestra de libros")
    print("7- Ordenar los libros por rating")
    print("0- Salir")


def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags = controller.loadData(control)
    return books, authors, tags, book_tags


def printAuthorData(author):
    if author:
        print("Autor encontrado: " + author["name"])
        print("Promedio: " + str(author["average_rating"]))
        print("Total de libros: " + str(lt.size(author["books"])))
        for book in lt.iterator(author["books"]):
            print("Titulo: " + book["title"] + "  ISBN: " + book["isbn"])
    else:
        print("No se encontro el autor")


def printBestBooks(books):
    size = lt.size(books)
    if size:
        print(" Estos son los mejores libros: ")
        for book in lt.iterator(books):
            print("Titulo: " + book["title"] + "  ISBN: " +
                  book["isbn"] + " Rating: " + book["average_rating"])
    else:
        print("No se encontraron libros")


def printSortResults(sort_books, sample=3):
    iter = itertools.count()
    num = next(iter)
    # TODO completar funcion para imprimir resultados sort lab 5
    size = lt.size(sort_books)
    if size <= sample*2:
        print("Los {} libros ordenados son: ".format(size))
        for book in lt.iterator(sort_books):
            num = next(iter)
            print("Numero {} Titulo {} ISBN {} Rating {}".format(num,book["title"], book["isbn"], book["average_rating"]))
    else:
        print("Los {} primeros libros ordenados son: ".format(sample))
        i = 1
        while i <= sample:
            book = lt.getElement(sort_books, i)
            print("Numero {} Titulo {} ISBN {} Rating {}".format(i, book["title"], book["isbn"], book["average_rating"]))
            i += 1
        
        print("Los {} últimos libros ordenados son: ".format(sample))
        i = size - sample + 1
        while i <= size:
            book = lt.getElement(sort_books, i)
            print("Numero {} Titulo {} ISBN {} Rating {}".format(i, book["title"], book["isbn"], book["average_rating"]))
            i += 1
    pass


def inputTry():
    while True:
        try:
            inputs = input("Seleccione una opción para continuar\n")
            return int(inputs)
        except ValueError:
            print("Por favor ingrese un número entero")
            continue

# Variable asociada al controlador de la vista, por defecto None
control = None


# variables utiles para el programa
algo_str = """Seleccione el algoritmo de ordenamiento:
                1. Selection Sort ||
                 2. Insertion Sort ||
                 3. Shell Sort ||
                 4. Merge Sort ||
                 5. Quick Sort ||
                 6. Heap Sort ||
                 7. Bogo Sort ||
                 8. Custom Sort (Tim Sort o Patience Sort)):"""
exit_opt_lt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

# main del ejercicio
if __name__ == "__main__":

    """
    Menu principal
    """
    # bandera para controlar el ciclo del menu
    working = True
    # tamaño de la muestra para pruebas
    size = 0.0

    # ciclo del menu
    while working:
        printMenu()
        inputs = input("Seleccione una opción para continuar\n")#inputTry()
        
        if int(inputs[0]) == 1:
            # se inicia un controlador nuevo y se cargan los datos
            control = newController()
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = loadData()
            print("Libros cargado1s: " + str(bk))
            print("Autores cargados: " + str(at))
            print("Géneros cargados: " + str(tg))
            print("Asociación de Géneros a Libros cargados: " + str(bktg))

        elif int(inputs[0]) == 2:
            number = input("Buscando los TOP ?: ")
            books = controller.getBestBooks(control, int(number))
            printBestBooks(books)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = controller.getBooksByAuthor(control, authorname)
            printAuthorData(author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = controller.countBooksByTag(control, label)
            print("Se encontraron: ", book_count, " Libros")

        elif int(inputs[0]) == 5:
            algo_opt = input(algo_str)
            algo_opt = int(algo_opt)
            algo_msg = controller.setSortAlgorithm(algo_opt)
            print(algo_msg)

        elif int(inputs[0]) == 6:
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            control = controller.setBookSublist(control, size)

        elif int(inputs[0]) == 7:
            # TODO completar modificaciones para el lab 5
            sample = int(input("Indique el tamaño de la muestra: "))
            print("Ordenando los libros por rating ...")
            result = controller.sortBooks(control)
            sortedBooks = result[0]
            deltaTime = f"{result[1]:.3f}"
            print("Tiempo de ejecución: ", deltaTime, " segundos")
            printSortResults(sortedBooks, sample)

        elif int(inputs[0]) == 0:
            # confirmar salida del programa
            end_str = "¿desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in exit_opt_lt:
                working = False
                print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)
