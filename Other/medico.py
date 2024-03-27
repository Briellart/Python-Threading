# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:26:53 2024

@author: Mamaguebo
"""
"""
Ahora imagina que estás en un hospital con varios médicos (hilos).
 Cada médico puede atender a un paciente a la vez.
 Sin embargo, solo hay una sala de rayos X (recurso compartido). 
 Usa un semáforo para asegurarte de que solo un médico use la sala de rayos X a la vez.
 """

import threading
import time

class Medico(threading.Thread):
    def __init__(self, id, semaforo):
        threading.Thread.__init__(self)
        self.id = id
        self.semaforo = semaforo

    def run(self):
        print(f"Médico {self.id} esperando para usar la sala de rayos X")
        self.semaforo.acquire()
        print(f"Médico {self.id} está usando la sala de rayos X")
        time.sleep(1)  # Simula el tiempo que tarda en usar la sala de rayos X
        print(f"Médico {self.id} ha terminado de usar la sala de rayos X")
        self.semaforo.release()

semaforo = threading.Semaphore(1)

medicos = [Medico(i, semaforo) for i in range(1, 4)]

for medico in medicos:
    medico.start()

for medico in medicos:
    medico.join()


