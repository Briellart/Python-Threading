# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:41:51 2024

@author: Usuario
"""
import random
from random import randint

class TrabajoImpresion:
    def __init__(self):
        self.aplicacion = self.aplicacion_aleatorio()
        self.usuario = self.nombre_aleatorio()
        self.archivo = self.generar_nombre_archivo()
        self.tiempo_impresion = self.generarTiempo()

    def generar_nombre_archivo(self):
        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        n=""
        for i in range(8):
            nombre_archivo = "".join(random.choice(caracteres)) 
            n+=nombre_archivo
        extension = random.choice(["txt", "docx","exe","py"])
        return f"{n}.{extension}"
    
    def nombre_aleatorio(self):
        nombre=random.choice(["Javier","Diego","Oscar","Bogdan","Asier","Unax","Ema","Susana","Gabriel"])
        return nombre
    
    def aplicacion_aleatorio(self):
        aplicacion=random.choice(["WORD","Spotify","Steam","Archivo","PowerPoint"])
        return aplicacion
    
    def generarTiempo(self):
        tiempo=random.randint(1,10)
        return tiempo
        
    
    def get_aplicacion(self):
        return self.aplicacion

    def get_usuario(self):
        return self.usuario

    def get_archivo(self):
        return self.archivo

    def get_tiempo_impresion(self):
        return self.tiempo_impresion
    
    def __str__(self):
        return f"{self.get_archivo()} - {self.get_aplicacion()} - {self.get_usuario()} - {self.get_tiempo_impresion()} seg."
    
if __name__ == "__main__":
    trabajo = TrabajoImpresion()
    print(trabajo)


