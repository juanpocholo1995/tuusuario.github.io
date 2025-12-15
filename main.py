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
