from datetime import datetime
import time

class FechaHora:
    def __init__(self):
        pass
    
    def __str__(self):
        return datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")

if __name__ == "__main__":
    hora = FechaHora()
    print(hora)
    time.sleep(1)
    print(hora)