# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11eoGMQ8dTeVUGs_pXrGi0rpkUzG7EvNA
"""

# pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Membaca citra
image = img.imread("D:/source.jpg")

# Mengambil setiap channel
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

# Membuat citra untuk channel Red, Green, dan Blue
imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

# Mengisi channel Red
imgRed[:,:,0] = red

# Mengisi channel Green
imgGreen[:,:,1] = green

# Mengisi channel Blue
imgBlue[:,:,2] = blue

# Menampilkan citra
plt.figure(figsize=(10,10))
plt.subplot(4,1,1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(4,1,2)
plt.imshow(imgRed)
plt.title('Red Channel')

plt.subplot(4,1,3)
plt.imshow(imgGreen)
plt.title('Green Channel')

plt.subplot(4,1,4)
plt.imshow(imgBlue)
plt.title('Blue Channel')

plt.show()