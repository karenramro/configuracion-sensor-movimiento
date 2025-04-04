import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  

try:
    while True:
        if GPIO.input(17):
            print("¡Movimiento detectado!")
        else:
            print("No hay movimiento.")
        time.sleep(1)  

except KeyboardInterrupt:
    print("Programa terminado.")
    GPIO.cleanup()
