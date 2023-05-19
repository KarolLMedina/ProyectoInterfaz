import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk, Label, Button, ttk
from scipy import signal
import scipy.fftpack as fp
from skimage.draw import disk
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
            imagen = tk.PhotoImage(file= Archivo)
            etiqueta_imagen = tk.Label (root, rayosX = imagen)
            etiqueta_imagen.pack()

root = Tk()
miVentana= VentanaInicio(root)
rayosX = Archivo

shape = rayosX.shape
center_X, center_Y = shape[0]//2, shape[1]//2
rr, cc = disk((center_X, center_Y), 10)
kernel = np.zeros(shape, dtype=np.uint8)
kernel[rr, cc] = 1

freq = fp.fft2(rayosX)

freq_kernel = fp.fft2(fp.ifftshift(kernel))
convolved = freq*freq_kernel
imageOut = fp.ifft2(convolved).real

#plot_images([moire, 255*kernel, imageOut], ["Original", "Filtro pasabajas", "Resultado"])

def dilation(rayosX, rect, padding_func):
  
    pad_size = (rect.shape[0]-1)//2
    padded_rayosX = padding_func(rayosX, pad_size)
    height, width = rayosX.shape
    new_rayosX = np.zeros((height, width), dtype=np.uint8)
    for i in range(height): 
        for j in range(width): 
            current_i = pad_size + i
            current_j = pad_size + j
            rayosX_region = padded_rayosX[current_i-pad_size:current_i+pad_size+1,
                                    current_j-pad_size:current_j+pad_size+1]

            new_rayosX[i,j] = np.max(rayosX_region*rect)
    return new_rayosX

imageOut = dilation(rayosX, rect, zero_padding)

shape = rayosX.shape
center_X, center_Y = shape[0]//2, shape[1]//2

rr, cc = disk((center_X, center_Y), 60)
kernel = np.zeros(shape, dtype=np.uint8)
kernel[rr, cc] = 1

rr, cc = disk((center_X, center_Y), 30)
kernel2 = np.zeros(shape, dtype=np.uint8)
kernel2[rr, cc] = 1

kernel3 = 1-(kernel-kernel2)

freq = fp.fftshift(fp.fft2(rayosX))

freq_kernel = fp.fft2(fp.ifftshift(kernel3))
convolved = freq*kernel3
imageOut = np.clip(fp.ifft2(fp.ifftshift(convolved)).real,0,255)

#plot_images([rayosX, 255*kernel3, imageOut], ["Original", "Filtro rechazabanda", "Resultado"])

root.mainloop()