import threading
import time
import random

semaforo = threading.Semaphore(3) # Inicia el samaforo contdo en 3.
# Crear un lock para proteger el acceso al contador de hilos activos
lock = threading.Lock()
# Contador de hilos activos
hilos_activos = 0
# Simulación de logueo de jugadores
def loguear_jugador(id_jugador):
    global hilos_activos
    print(f"Jugador {id_jugador} intentando loguearse...\n")

    time.sleep(random.uniform(0.1, 0.5))
    
    # Simular una pequeña espera aleatoria antes de acceder a la sección crítica
    # Adquirir el semáforo antes de acceder a la sección crítica
    semaforo.acquire()
    try:
        # Incrementar el contador de hilos activos
        with lock:
            hilos_activos += 1
            print(f"Jugador {id_jugador} logueado en el servidor. Hilos activos: {hilos_activos}\n")
        
        # Simular el tiempo de permanencia en el servidor
        time.sleep(2)
        
        print(f"Jugador {id_jugador} desconectado del servidor.\n")
    finally:
        # Decrementar el contador de hilos activos y liberar el semáforo
        with lock:
            hilos_activos -= 1
            print(f"Hilos activos: {hilos_activos}\n")
        semaforo.release()

# Crear y arrancar varios jugadores simulando el acceso al servidor
jugadores = []

for i in range(10):
    jugador = threading.Thread(target=loguear_jugador, args=(i,))
    jugadores.append(jugador)
    jugador.start()
# Esperar a que todos los jugadores terminen
for jugador in jugadores:
    jugador.join()

print("Todos los jugadores han terminado de jugar.\n")