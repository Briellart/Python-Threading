import threading
import datetime
import random
from random import randint
import time
import queue


"""
Imagina que estás en una tienda con dos cajas registradoras. 
Cada caja registradora puede atender a varios clientes a la vez, 
por lo que cada una tiene varios hilos (por ejemplo, uno para cobrar, otro para empaquetar los productos, etc.). 
Todos estos hilos comparten un recurso común: la impresora de recibos. 
Usa un bloqueo para asegurarte de que solo un hilo imprima un recibo a la vez.
"""


class Recibo:
    def __init__(self, id, quien_te_atiende, ubicacion, precio):
        self.id = id
        self.fecha = datetime.datetime.now()
        self.quien_te_atiende = self.get_quien_te_atiende()
        self.ubicacion = self.get_ubicacion()
        self.precio = self.get_precio()
        self.precio_con_iva = self.get_precio_con_iva()
        
    
    def get_ubicacion(self):
        return random.choice(["Calle 1", "Calle 2", "Calle 3", "Calle 4", "Otro"])
    
    def get_quien_te_atiende(self):
        return random.choice(["ALEX", "SOFIA", "JAVI", "INES", "ANDREA"])
    
    def get_precio(self):
        return random.randint(1, 100)
        
    def get_precio_con_iva(self):
        return self.precio * 1.21
    
    def get_quien_te_atiende(self):
        return random.choice(["ALEX", "SOFIA", "JAVI", "INES", "ANDREA"])

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Fecha: {self.fecha}\n"
                f"Atendido por: {self.get_quien_te_atiende()}\n"
                f"Ubicación: {self.get_ubicacion()}\n"
                f"Precio: {self.precio}\n"
                f"Precio con IVA: {self.precio_con_iva}\n")

class CajaRegistradora:
    def __init__(self, id, max_hilos):
        self.id = id
        self.lock = threading.Lock()
        self.bloqueo = threading.Lock()
        self.cola = queue.Queue(maxsize=max_hilos)

    def sacar_recibo(self, num_recibo):
        with self.lock:
            print(f"Hilo {num_recibo} saliendo de la cola de la Caja {self.id}")
            recibo = Recibo(num_recibo,"", "", "")
            with self.bloqueo:
                 print(recibo)
            print(f"Caja registradora {self.id} ha sacado el recibo {num_recibo}")
            print(f"Caja registradora {self.id} tiene {self.cola.qsize()} hilos en la cola")
            time.sleep(random.randint(1, 5))

class GenerarHilos(threading.Thread):
    def __init__(self, caja_registradora, num_hilo):
        threading.Thread.__init__(self)
        self.caja_registradora = caja_registradora
        self.num_hilo = num_hilo

    def run(self):
        for i in range(1, 6):
            self.caja_registradora.sacar_recibo(i)
            time.sleep(random.randint(1, 5))  # Add random sleep between 1 and 5 seconds

"""
caja1 = CajaRegistradora(1)
caja2 = CajaRegistradora(2)

hilos_caja1 = [GenerarHilos(caja1,i) for i in range(5)]
hilos_caja2 = [GenerarHilos(caja2,i) for i in range(5)]


for hilo in hilos_caja1:
    hilo.start()
for hilo in hilos_caja2:
    hilo.start()

for hilo in hilos_caja1:
    hilo.join()
for hilo in hilos_caja2:
    hilo.join()
    """

caja1 = CajaRegistradora(1, 3)
caja2 = CajaRegistradora(2, 3)

hilos_caja1 = []
hilos_caja2 = []

for i in range(5):
    if not caja1.cola.full():
        hilo = GenerarHilos(caja1, i)
        caja1.cola.put(hilo)
        hilos_caja1.append(hilo)
        print(f"Hilo {i} añadido a la cola de la Caja {caja1.id}")
        hilo.start()
        time.sleep(random.randint(1, 5))
    if not caja2.cola.full():
        hilo = GenerarHilos(caja2, i)
        caja2.cola.put(hilo)
        hilos_caja2.append(hilo)
        print(f"Hilo {i} añadido a la cola de la Caja {caja2.id}")
        hilo.start()
        time.sleep(random.randint(1, 5))

for hilo in hilos_caja1:
    hilo.join()

for hilo in hilos_caja2:
    hilo.join()

