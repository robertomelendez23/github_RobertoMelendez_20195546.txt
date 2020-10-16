import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma():
    sumDosNum = 4 + 2
    return sumDosNum


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    sumPares = 0
    inicio = 1
    final = 1000
    while inicio <= final:
        if inicio % 2 == 0:
            sumPares = sumPares + inicio
        inicio = inicio + 1
    return sumPares


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro():
    areaTotalCilindro = round((areaCirculo() + areaLateral()), 2)
    return areaTotalCilindro


import math


def areaLateral():
    altura = 7.0
    radio = 5.0
    areaLat = 2.0 * math.pi * radio * altura
    return areaLat


import math


def areaCirculo():
    radio = 5.0
    areaCirc = 2.0 * math.pi * radio ** 2
    return areaCirc


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
import math


class Cilindro:
    def areaTotalCilindro(self):
        alturaCilindro = 7.0
        radioCirculo = 5.0
        claseAreaCilindro = round(
            (
                2.0 * math.pi * radioCirculo ** 2
                + 2 * math.pi * radioCirculo * alturaCilindro
            ),
            2,
        )
        return claseAreaCilindro


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def ordenar(self):
        pass

    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return (
        "https://github.com/robertomelendez23/github_RobertoMelendez_20195546.txt.git"
    )
