import threading
import time
import random

# Simulación de logueo de jugadores
def loguear_jugador(id_jugador):
    print(f"Jugador {id_jugador} intentando loguearse...\n")
    
    # Simular una pequeña espera aleatoria antes de acceder a la sección crítica
    time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Jugador {id_jugador} logueado en el servidor.\n")
    time.sleep(2)  # Simular el tiempo de permanencia en el servidor
    print(f"Jugador {id_jugador} desconectado del servidor.\n")

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

