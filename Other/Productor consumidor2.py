# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:27:43 2024

@author: Mamaguebo
"""
"""
Ahora imagina que estás en un centro de llamadas con varios operadores (hilos productores) y varios especialistas (hilos consumidores).
 Los operadores reciben llamadas y las ponen en una cola. Los especialistas toman las llamadas de la cola y las resuelven. 
 Asegúrate de manejar correctamente la sincronización y las condiciones de carrera.
 """

import threading
import queue
import random
import math

class Productor(threading.Thread):
    def __init__(self, cola, id):
        threading.Thread.__init__(self)
        self.cola = cola
        self.id = id

    def run(self):
        for _ in range(10):
            num = random.randint(1, 100)
            self.cola.put(num)
            print(f"Productor {self.id} produjo: {num}")

class Consumidor(threading.Thread):
    def __init__(self, cola, id):
        threading.Thread.__init__(self)
        self.cola = cola
        self.id = id

    def run(self):
        while not self.cola.empty():
            num = self.cola.get()
            print(f"Consumidor {self.id} calculó el factorial de {num}: {math.factorial(num)}")

cola = queue.Queue()

productores = [Productor(cola, i) for i in range(1, 4)]
consumidores = [Consumidor(cola, i) for i in range(1, 4)]

for productor in productores:
    productor.start()

for productor in productores:
    productor.join()

for consumidor in consumidores:
    consumidor.start()

for consumidor in consumidores:
    consumidor.join()