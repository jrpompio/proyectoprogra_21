#!/usr/bin/python3
# El siguiente programa adivina el numero seleccionado
# después de introducir 4 veces el valor de la columna en la que
# el numero seleccionado se encuentra
#### a rocha le pica el culo

#### afsldñkfjalñjsdfalj justin solo piensa en A
##Import librerias y Funciones propias
import numpy as np





####Función para menú:
def selecionar(Mensaje):
    "Valicacion de los numeros 1, 2 y 3"
    Cantidad_de_valores = 3
    cond = True
    while cond:

        valor = input(Mensaje)
        try:
            valor = int(valor)
            if valor > 0 and valor <= Cantidad_de_valores:
                cond = False
            else:
                cantidad = np.arange(1, Cantidad_de_valores + 1)

                print(f"\nError:\n Usted seleccionó el valor: -> {valor} <-\ny los valores posibles son:")
                for i in cantidad:
                    print(f" ->   {i}", end=" ")
                print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
                print("▒▒-Intente usando uno de estos valores-▒▒")
                print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        except ValueError:

            print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print("▒▒   Error: Debe indicar el numero -   ▒▒")
            print("▒▒  correspondiente a su selección.    ▒▒")
            print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    return valor


## Funcion para repetir o salir de while:
def Psalir(Mensaje):
    # Ciclo de Validación.
    while True:
        # Mostrar mensaje en pantalla.
        Letra = input(Mensaje)
        # Validar Letra.
        if Letra == "S" or Letra == "s":
            return True
        elif Letra == "N" or Letra == "n":
            return False
        else:
            # Mensaje de error.
            print("ERROR: Letra insertada es inválida\nDigite S para si, o N para no")


re = True
## Ciclo while para repetir
while re:
    ##Cuerpo del codigo
    m = np.arange(1, 22).reshape(7, -1)

    print()
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒-------------------------------------------------▒▒")
    print("▒▒ Escoge un numero, dime solo en que columna esta ▒▒")
    print("▒▒       en 4 turnos te diré cual escogiste        ▒▒")
    print("▒▒-------------------------------------------------▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")
    seleccion = int(selecionar(f"\n{m}\n\nEmpecemos ¿En que columna se encuentra?\n------>"))
    seleccion = int(seleccion) - int(1)
    if seleccion == 0:
        m = m[:, [1, 0, 2]]
        m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                      [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                      [m[2][0], m[1][0], m[0][0]]])

        ##pegar 1

        seleccion = int(selecionar(f"\n{m}\n\nSigamos ¿En que columna se encuentra?\n------>"))
        seleccion = int(seleccion) - int(1)

        if seleccion == 0:
            m = m[:, [1, 0, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2


            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 1:
            m = m[:, [0, 1, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 2:
            m = m[:, [0, 2, 1]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])


    elif seleccion == 1:
        m = m[:, [0, 1, 2]]
        m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                      [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                      [m[2][0], m[1][0], m[0][0]]])

        ##pegar 1

        seleccion = int(selecionar(f"\n{m}\n\n Sigamos ¿En que columna se encuentra?\n------>"))
        seleccion = int(seleccion) - int(1)
        if seleccion == 0:
            m = m[:, [1, 0, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 1:
            m = m[:, [0, 1, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 2:
            m = m[:, [0, 2, 1]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

    elif seleccion == 2:
        m = m[:, [0, 2, 1]]
        m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                      [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                      [m[2][0], m[1][0], m[0][0]]])

        ##pegar 1

        seleccion = int(selecionar(f"\n{m}\n\n Sigamos ¿En que columna se encuentra?\n------>"))
        seleccion = int(seleccion) - int(1)

        if seleccion == 0:
            m = m[:, [1, 0, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 1:
            m = m[:, [0, 1, 2]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

        elif seleccion == 2:
            m = m[:, [0, 2, 1]]
            m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                          [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                          [m[2][0], m[1][0], m[0][0]]])

            ##pegar 2

            seleccion = int(selecionar(f"\n{m}\n\nVamos de nuevo ¿En que columna se encuentra?\n------>"))
            seleccion = int(seleccion) - int(1)

            if seleccion == 0:
                m = m[:, [1, 0, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 1:
                m = m[:, [0, 1, 2]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])

            elif seleccion == 2:
                m = m[:, [0, 2, 1]]
                m = np.array([[m[6][2], m[5][2], m[4][2]], [m[3][2], m[2][2], m[1][2]], [m[0][2], m[6][1], m[5][1]],
                              [m[4][1], m[3][1], m[2][1]], [m[1][1], m[0][1], m[6][0]], [m[5][0], m[4][0], m[3][0]],
                              [m[2][0], m[1][0], m[0][0]]])


    seleccion = int(selecionar(f"\n{m}\n\nUna vez más ¿En que columna se encuentra?\n------>"))
    seleccion = int(seleccion) - int(1)

    print()
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒-------------------------------------------------▒▒")
    print("                  TU NUMERO ES EL:                   ")
    print(f"                       {m[3][seleccion]}            ")
    print("▒▒-------------------------------------------------▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒-----------------------------------------------------------------------------▒▒")
    print("▒▒  ¿Desea volver a jugar?(S/N) [S: para responder Si  ; N: para responder No] ▒▒")
    print("▒▒-----------------------------------------------------------------------------▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    ## Uso de función para cerrar o repetir el ciclo while
    re = Psalir("\n------------------------►  ")
    ##Mensaje de despedida
    if re == False:

        print()
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒-----------------------------------------------------------------------------▒▒")
        print("▒▒  Ha sido un placer entretenerle, Gracias por usar nuestros servicios.       ▒▒")
        print("▒▒-----------------------------------------------------------------------------▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        input("Presione ENTER para terminar.... ")
