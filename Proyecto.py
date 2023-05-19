import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk, Label, Button, ttk
class VentanaInicio:
    def __init__(self, master):
        self.master = master
        master.title("Procesador de Imágenes Rayos X")
        self.etiqueta = Label(master, text="Inserte la imagen a filtrar")
        self.etiqueta.pack()
        self.botonInicio = Button(master, text="Insertar", command=self.insert)
        self.botonInicio.pack()
        self.botonCancelar = Button(master, text="Cancelar", command=master.quit)
        self.botonCancelar.pack()
    def insert(self):
            print ("Inserta el nombre del archivo: ")
            root = tk.Tk ()
            root.config (width=200, height=200)
            Archivoent = tk.StringVar()
            Archivo = ttk.Entry (textvariable=Archivoent)
            # Archivo = ttk.Entry()
            Archivo.place (x=0, y=20)
           # root.mainloop()
            print(Archivo.get())
            imagen = tkinter.PhotoImage(file= Archivo)
            etiqueta_imagen = tkinter.Label (root, rayosX = imagen)
            etiqueta_imagen.pack()

root = Tk()
miVentana= VentanaInicio(root)



root.mainloop()