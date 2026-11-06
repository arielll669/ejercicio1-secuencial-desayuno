# Ejercicio 1: Ejecución secuencial - Preparar el desayuno

Script en Python que muestra una **ejecución secuencial** con un ejemplo de la vida diaria: preparar el desayuno.

## ¿Qué es la ejecución secuencial?

Las tareas se ejecutan **una después de otra**. Una tarea no empieza hasta que la anterior termina por completo. El tiempo total es la **suma** de los tiempos de cada tarea.

## El ejemplo

Una persona prepara el desayuno siguiendo estos pasos en orden:

| Paso | Tarea | Duración |
|------|-------|----------|
| 1 | Hervir el agua | 3 s |
| 2 | Tostar el pan | 2 s |
| 3 | Freír los huevos | 3 s |
| 4 | Preparar el café | 2 s |
| 5 | Servir el desayuno | 1 s |
| | **Total** | **11 s** |

Aunque mientras el agua hierve se podría tostar el pan, en este ejercicio la persona espera a que cada paso termine antes de pasar al siguiente. Así se ve claramente qué es una ejecución secuencial.

## Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución (incluye Docker Compose).

## Cómo ejecutarlo con Docker Compose

1. Clonar el repositorio y entrar a la carpeta:

   ```bash
   git clone https://github.com/arielll669/ejercicio1-secuencial-desayuno.git
   cd ejercicio1-secuencial-desayuno
   ```

2. Construir la imagen y ejecutar el script:

   ```bash
   docker compose up --build
   ```

3. Al terminar, limpiar el contenedor:

   ```bash
   docker compose down
   ```

## Salida esperada

```
============================================================
EJECUCION SECUENCIAL: Preparando el desayuno
Cada paso espera a que el anterior termine.
============================================================
[  0.0s] Paso 1: Poniendo a hervir el agua...
[  3.0s] Paso 1: Agua hervida.
[  3.0s] Paso 2: Tostando el pan...
[  5.0s] Paso 2: Pan tostado.
[  5.0s] Paso 3: Friendo los huevos...
[  8.0s] Paso 3: Huevos fritos.
[  8.0s] Paso 4: Preparando el cafe con el agua caliente...
[ 10.0s] Paso 4: Cafe listo.
[ 10.0s] Paso 5: Sirviendo el desayuno en la mesa...
[ 11.0s] Paso 5: Desayuno servido.
============================================================
Tiempo total: 11.0 segundos
(3 + 2 + 3 + 2 + 1 = 11 s: la suma de todos los pasos)
============================================================
```

Observa que cada paso empieza exactamente en el segundo en que termina el anterior.

## Estructura del proyecto

```
.
├── main.py              # Script con la ejecución secuencial
├── Dockerfile           # Imagen de Python 3.12
├── docker-compose.yml   # Definición del servicio
└── README.md
```

## Ejecución sin Docker (opcional)

```bash
python main.py
```
