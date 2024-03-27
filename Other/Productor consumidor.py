# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:26:11 2024

@author: Mamaguebo
"""
"""
Imagina que estás en una fábrica con una máquina que produce piezas (hilo productor) 
y un trabajador que verifica la calidad de las piezas (hilo consumidor). 
La máquina produce piezas y las pone en una cinta transportadora (cola). 
El trabajador toma las piezas de la cinta transportadora y verifica su calidad.
"""

import threading
import queue
import random

class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for _ in range(10):
            num = random.randint(1, 100)
            self.cola.put(num)
            print(f"Productor produjo: {num}")

class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        while not self.cola.empty():
            num = self.cola.get()
            print(f"Consumidor calculó el cuadrado de {num}: {num**2}")

cola = queue.Queue()

productor = Productor(cola)
consumidor = Consumidor(cola)

productor.start()
productor.join()

consumidor.start()
consumidor.join()
