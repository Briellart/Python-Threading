# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:20:15 2024

@author: Usuario
"""

from threading import Thread, Semaphore, Lock
import time
from queue import Queue
from TrabajoImpresion import TrabajoImpresion
from Fecha import FechaHora
import random
from GenerarHilos import GenerarHilos
from random import randint

class Escribe(Thread):
    def __init__(self,cola,semaforo,bloqueo,fichero):
        Thread.__init__(self)
        self.cola=cola
        self.semaforo=semaforo
        self.bloqueo=bloqueo
        self.fichero=fichero
        
    def run(self):
        n=0
        with self.semaforo:
            while n<50: #tiene que hacer 50 impresiones en total
                linea =self.cola.get()
                fecha=FechaHora()
                n+=1
                
                with self.bloqueo:
                    print(f"{fecha} Imprimiendo: {linea}")
                    print(f"{fecha} Trabajos impresos: {n} - Numero de trabajos en cola: {self.cola.qsize()}")
                    
                self.fichero.write(f"{fecha} Imprimiendo: {linea}\n")    
                self.fichero.flush()
                self.cola.task_done()
                time.sleep(linea.get_tiempo_impresion())
                
                
if __name__=="__main__":
    cola = Queue(3)
    semaforo = Semaphore(5)
    bloqueo=Lock()
    fichero=open("pruebaEscritor.txt","w")
    
    hilo_escritor=Escribe(cola, semaforo, bloqueo, fichero)
    hilo_escritor.start()
    
    hilos_generadores=[]
    for i in range(10):
        hilo_generador = GenerarHilos(i, cola, semaforo)
        hilos_generadores.append(hilo_generador)

    for hilo in hilos_generadores:
        hilo.start()

    for hilo in hilos_generadores:
        hilo.join()
    
    hilo_escritor.join()
    fichero.close()
            