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
    mensaje = file.read() <

for numero in numeros:
    pywhatkit.sendwhats_image(
        f"{numero}", "imagenes/imagen1.jpeg", f"{mensaje}", wait_time=45)
    for imagen in glob.glob('imagenes/*.jpeg'):
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
