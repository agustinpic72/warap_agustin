import pywhatkit
import glob
from pywhatkit.core.core import copy_image
from pyautogui import hotkey, press, keyDown, keyUp
from time import sleep

numeros = []
with open('numeros.txt', 'r') as file:
    numeros = file.readlines()
    numeros = [n[:-1] for n in numeros]
with open('mensaje.txt', 'r') as file:
    mensaje = file.read()

imagenes = glob.glob('imagenes/*.jpeg')
for numero in numeros:
    pywhatkit.sendwhats_image(
        f"{numero}", imagenes.pop(0), f"{mensaje}", wait_time=45)
    for imagen in imagenes:
        copy_image(imagen)
        keyDown('ctrl')
        press('v')
        keyUp('ctrl')
        sleep(3)
    press('enter')
    print('closing tab...')
    sleep(10)
    keyDown('ctrl')
    press('w')
    keyUp('ctrl')
    sleep(2)
    press('enter')
    sleep(2)
    print('releasing keys...')
