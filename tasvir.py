import time
import sys
import os

print("Iniciando extracción de datos...\n")

for i in range(1, 101):
    # Simular tiempo de extracción
    time.sleep(0.05)
    
    # Mostrar progreso
    sys.stdout.write(f"\rExtrayendo datos... {i}%")
    sys.stdout.flush()

print("\n\n¡Extracción completada con éxito!")
time.sleep(1)

# Mensaje sorpresa
print("Gracias por tus datos... te lo agradece JOEYTAS 🤖")
time.sleep(2)

# Mensaje adicional para la broma
print("\nDetectando archivos importantes...")
time.sleep(2)
print("JOEYTAS lo está cifrando 😱...")


# Abrir la primera ventana del CMD
os.system("start cmd /k echo Gracias por tus datos")

# Esperar un momento para que sea visible
time.sleep(2)

# Abrir la segunda ventana del CMD
os.system("start cmd /k echo Estaran seguros...")

# Esperar unos segundos para simular que están activas
time.sleep(5)

# Cerrar ambas ventanas CMD automáticamente
# Esto cierra todas las ventanas CMD que se abrieron
os.system("taskkill /F /IM cmd.exe")