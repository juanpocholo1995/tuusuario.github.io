Tarea Mini-Turtle

Este proyecto corresponde a la Tarea Mini-Turtle, cuyo objetivo es aplicar modularidad y programación orientada a objetos (POO) en Python mediante la creación de dos paquetes independientes.

📌 Ejercicio 1: Versión Funcional (Modularidad)
🎯 Objetivo

Transformar las funciones sueltas adelante() y abajo() en un paquete Python distribuible llamado mini_turtle, demostrando la separación entre:

Lógica interna

Interfaz pública

⚙️ Requerimientos cumplidos

Interfaz limpia:

from mini_turtle import adelante, abajo, reiniciar

Nueva función reiniciar() que restablece posicion_x a 0

Uso de variable global solo en la versión funcional

📦 Estructura del proyecto
mini_turtle/
│
├── mini_turtle/
│   ├── __init__.py
│   └── drawer_logic.py
│
└── main.py
🧠 Lógica (drawer_logic.py)
posicion_x = 0


def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Avanza {pasos} pasos → x = {posicion_x}")


def abajo():
    print("Lápiz abajo")


def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
🧪 Prueba (main.py)
from mini_turtle import adelante, abajo, reiniciar


print("Dibujando escalera")
abajo()
adelante(2)
adelante(2)
adelante(2)


reiniciar()


print("\nDibujando algo nuevo")
adelante(5)
adelante(3)

🔗 Repositorio Ejercicio 1: 👉 https://github.com/juanpocholo1995/mini_turtle/tree/e24edf142a962ef83b651b888e6fecf34b34dce0/mini_turtle

📌 Ejercicio 2: Versión Orientada a Objetos (POO)
🎯 Objetivo

Refactorizar el paquete anterior utilizando Clases y Objetos, eliminando variables globales y aplicando encapsulamiento.

⚙️ Requerimientos cumplidos

Clase Tortuga

Estado encapsulado en self.posicion_x

Prohibido usar global

Posibilidad de crear múltiples objetos independientes

Interfaz limpia:

from mini_turtle_oo import Tortuga
📦 Estructura del proyecto
mini_turtle_oo/
│
├── mini_turtle_oo/
│   ├── __init__.py
│   └── turtle_class.py
│
└── main.py
🧠 Clase Tortuga (turtle_class.py)
class Tortuga:
    def __init__(self):
        self.posicion_x = 0


    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Avanza {pasos} pasos → x = {self.posicion_x}")


    def abajo(self):
        print("Lápiz abajo")


    def reiniciar(self):
        self.posicion_x = 0
        print("Posición reiniciada a 0")
🧪 Prueba con múltiples objetos (main.py)
from mini_turtle_oo import Tortuga


t1 = Tortuga()
t2 = Tortuga()


print("Movimientos de t1")
t1.adelante(5)
t1.adelante(3)


print("\nMovimientos de t2")
t2.adelante(10)


print("\nReiniciando t1")
t1.reiniciar()


print("\nMovimientos finales")
t1.adelante(2)
t2.adelante(1)

🔗 Repositorio Ejercicio 2: 👉 https://github.com/TU_USUARIO/mini_turtle_oo

