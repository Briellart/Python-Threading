# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:09:50 2024

@author: Usuario
"""

from threading import  Lock, Semaphore
from queue import Queue
from Escritor import Escribe
from GenerarHilos import GenerarHilos
from Fecha import FechaHora

if __name__=="__main__":
    hora = FechaHora()
    print(f"{hora} - Abierta la cola de impresión")
    cola = Queue(3)
    semaforo = Semaphore(5)
    bloqueo=Lock()
    fichero=open("log.txt","w")
    
    hilo_escritor=Escribe(cola, semaforo, bloqueo, fichero)
    hilo_escritor.start()
    
    hilos_generadores=[]
    for i in range(10):
        hilo_generador = GenerarHilos(i, cola, semaforo,bloqueo)
        hilos_generadores.append(hilo_generador)
    
    for hilo in hilos_generadores:
        hilo.start()
    
    for hilo in hilos_generadores:
        hilo.join()
    
    hilo_escritor.join()
    fichero.close()