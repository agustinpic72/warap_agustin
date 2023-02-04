import pywhatkit
from keyboard import press, release
from time import sleep

numeros = []
with open('numeros.txt','r') as file:
    numeros = file.readlines()
    numeros = [n[:-1] for n in numeros]
with open('mensaje.txt','r') as file:
    mensaje = file.read()


for numero in numeros:
    pywhatkit.sendwhats_image(f"{numero}", "imagen.jpg", f"{mensaje}", wait_time=45)
    print('closing tab...')
    sleep(10)
    press('ctrl+w')
    release('ctrl+w')
    sleep(2)
    press('enter')
    release('enter')
    sleep(2)
    print('releasing keys...')


    
