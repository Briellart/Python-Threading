import threading
import time
import random

# El dato al que los hilos intentarán llegar
dato = 10

# Semáforo para controlar el acceso al dato
sem = threading.Semaphore()

# Variable para rastrear el primer hilo que llega al dato
primer_hilo = None

class MiHilo(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        global dato
        global primer_hilo
        while True:
            sem.acquire()
            if dato == 0:
                # Si ningún hilo ha llegado al dato aún, este hilo es el primero
                if primer_hilo is None:
                    primer_hilo = self.nombre
                    print(f"{self.nombre} ha llegado primero al dato!")
                sem.release()
                break
            else:
                print(f"{self.nombre} está disminuyendo el dato, valor actual: {dato}")
                dato -= 1
                time.sleep(random.uniform(0.1, 1.0))
                sem.release()

# Crear y empezar los hilos
hilo1 = MiHilo("Hilo 1")
hilo2 = MiHilo("Hilo 2")

time.sleep(0.1)  # Introduce un pequeño retraso
hilo1.start()

time.sleep(0.1)  # Introduce un pequeño retraso
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambos hilos han terminado.")