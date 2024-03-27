# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:55:06 2024

@author: Usuario
"""


from threading import Thread, Semaphore, Lock
import time
from queue import Queue
from TrabajoImpresion import TrabajoImpresion
from Fecha import FechaHora
import random
from random import randint

class GenerarHilos(Thread):
    def __init__(self, hilo_id,cola,semaforo,bloqueo):
        Thread.__init__(self)
        self.hilo_id = hilo_id
        self.cola=cola
        self.semaforo=semaforo
        self.bloqueo=bloqueo
        
    def run(self):
        
        for i in range(5):
            trabajo = TrabajoImpresion()
            fecha=FechaHora()
            trabajoo="Imprimiendo: "+str(trabajo)
            linea = str(fecha)+ trabajoo
            
            with self.semaforo:
                self.cola.put(trabajo)
            with self.bloqueo:
                print(f"{fecha} - Enviado trabajo nº {i}: {trabajoo}")
                print(f"{fecha} - Numero de trabajos en cola: {self.cola.qsize()}")
            time.sleep(randint(5,20))

if __name__=="__main__":
    cola = Queue(3)
    semaforo = Semaphore(5)
    bloqueo=Lock()
    
    hilos_generadores=[]
    for i in range(10):
        hilo_generador = GenerarHilos(i, cola, semaforo,bloqueo)
        hilos_generadores.append(hilo_generador)

    for hilo in hilos_generadores:
        hilo.start()
        print(hilo)

    for hilo in hilos_generadores:
        hilo.join()
    
    