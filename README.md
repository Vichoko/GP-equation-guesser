# Genetic-Programming
Implementación de algoritmo de Programación Genética sobre el lenguaje definido por las funciones ```+, -, *, /``` y los terminales ```números y variable x```, en el problema de búsqueda de un polinomio en base a sus valores de entrada (x) y salida (y).
## Problema

Dado un **polinomio de una variable** (Ej. ```3x^2 + 2x + 3 + x^3```), encontrar la expresión del polinomio (AST) mediante **programación genética,** minimizando los errores cuadráticos medios, resultantes de la evaluación comparada.
## Restricciones

Para el polinomio, se admiten valores de coeficientes entre -5 y 5.

El cálculo de errores cuadráticos medios resulta de evaluar el polinomio esperado y cada individuo con valores de **x** entre -5 y 5.

El error cuadrático mínimo aceptable para un individuo perfecto es de 0.1.

### Dependencias

* Numpy
## Fitness

Se utiliza la suma de errores cuadrados entre el valor esperado y el valor actual obtenido mediante cada polinomio, para cada x entre -5 y 5.

Por lo que a menor fitness, mejor individuo.
## Selección

Por Tournament Selection con k= 2 (modificable)
## Ejecución
Luego de configurar (ó por defecto), ejecutar script ```./Evolution.py```

## Configuración

Se pueden modificar parámetros y el polinomio objetivo dentro del archivo 
```./Global.py```

### Constantes numéricas

```
MAX_NUMBER = 5.0  # valor máximo de coeficiente & x
MIN_NUMBER = -5.0 # valor mínimo de coeficiente & x
MAX_DEPTH = 5 # profundidad máxima de AST generado aleatoriamente
MIN_ACCEPTABLE_ERROR = 0.1 # error mínimo aceptable para ser individuo perfecto
DELTA = 0.1 # Paso de discretización de x entre MAX_NUMBER y MIN_NUMBER
```

### Parámetros de evolución

```
POPULATION_SIZE = 1000  # Tamaño de población
CROSSOVER_CHANCE = 0.5  # Probabilidad de hacer crossover, si no heredan genes directos
SEX_CHANCE = 0.8  # Probabilidad de engendrar un hijo
MUTATION_CHANCE = 0.1  # Probabilidad de que ocurra una mutación en un AST
TOURNAMENT_K = 2  # Elecciones en selección por torneo
```

### Expresión objetivo
Aparte de poder configurar el polinomio a gusto, se debe variar la constante ```NUMBER_OF_OPERATIONS``` , para prevenir que se generes AST excesivamente grandes que obstruyan la ejecución.

```
NUMBER_OF_OPERATIONS = 8  # Numero de operaciones mínimas en el polinomio

def polynomial(x):
    return 3*x**2 + 2*x + 3 + x**3

```
