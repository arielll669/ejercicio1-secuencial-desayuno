"""
Ejercicio 1: Ejecución SECUENCIAL
Ejemplo de la vida real: preparar el desayuno.

En una ejecución secuencial cada tarea empieza solo cuando la anterior
terminó por completo. El tiempo total es la SUMA de los tiempos de cada paso.
"""

import time

INICIO = time.perf_counter()


def log(mensaje: str) -> None:
    """Imprime un mensaje con el segundo exacto en que ocurrió."""
    transcurrido = time.perf_counter() - INICIO
    print(f"[{transcurrido:5.1f}s] {mensaje}")


def hervir_agua() -> None:
    log("Paso 1: Poniendo a hervir el agua...")
    time.sleep(3)
    log("Paso 1: Agua hervida.")


def tostar_pan() -> None:
    log("Paso 2: Tostando el pan...")
    time.sleep(2)
    log("Paso 2: Pan tostado.")


def freir_huevos() -> None:
    log("Paso 3: Friendo los huevos...")
    time.sleep(3)
    log("Paso 3: Huevos fritos.")


def preparar_cafe() -> None:
    log("Paso 4: Preparando el cafe con el agua caliente...")
    time.sleep(2)
    log("Paso 4: Cafe listo.")


def servir_desayuno() -> None:
    log("Paso 5: Sirviendo el desayuno en la mesa...")
    time.sleep(1)
    log("Paso 5: Desayuno servido.")


def main() -> None:
    print("=" * 60)
    print("EJECUCION SECUENCIAL: Preparando el desayuno")
    print("Cada paso espera a que el anterior termine.")
    print("=" * 60)

    hervir_agua()
    tostar_pan()
    freir_huevos()
    preparar_cafe()
    servir_desayuno()

    total = time.perf_counter() - INICIO
    print("=" * 60)
    print(f"Tiempo total: {total:.1f} segundos")
    print("(3 + 2 + 3 + 2 + 1 = 11 s: la suma de todos los pasos)")
    print("=" * 60)


if __name__ == "__main__":
    main()
