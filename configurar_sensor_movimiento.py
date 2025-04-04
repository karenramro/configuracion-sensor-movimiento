import RPi.GPIO as GPIO
import time

# Configurar la numeración de pines de la Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # Usa el pin GPIO 17 (ajústalo según tu conexión)

try:
    while True:
        if GPIO.input(17):
            print("¡Movimiento detectado!")
        else:
            print("No hay movimiento.")
        time.sleep(1)  # Espera 1 segundo

except KeyboardInterrupt:
    print("Programa terminado.")
    GPIO.cleanup()
