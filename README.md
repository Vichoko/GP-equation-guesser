# Genetic-Programming
Implementaci�n de algoritmo de Programaci�n Gen�tica sobre el lenguaje definido por las funciones ```+, -, *, /``` y los terminales ```n�meros y variable x```, en el problema de b�squeda de un polinomio en base a sus valores de entrada (x) y salida (y).
## Problema

Dado un **polinomio de una variable** (Ej. ```3x^2 + 2x + 3 + x^3```), encontrar la expresi�n del polinomio (AST) mediante **programaci�n gen�tica,** minimizando los errores cuadr�ticos medios, resultantes de la evaluaci�n comparada.
## Restricciones

Para el polinomio, se admiten valores de coeficientes entre -5 y 5.

El c�lculo de errores cuadr�ticos medios resulta de evaluar el polinomio esperado y cada individuo con valores de **x** entre -5 y 5.

El error cuadr�tico m�nimo aceptable para un individuo perfecto es de 0.1.

### Dependencias

* Numpy
## Fitness

Se utiliza la suma de errores cuadrados entre el valor esperado y el valor actual obtenido mediante cada polinomio, para cada x entre -5 y 5.

Por lo que a menor fitness, mejor individuo.
## Selecci�n

Por Tournament Selection con k= 2 (modificable)
## Ejecuci�n
Luego de configurar (� por defecto), ejecutar script ```./Evolution.py```

## Configuraci�n

Se pueden modificar par�metros y el polinomio objetivo dentro del archivo 
```./Global.py```

### Constantes num�ricas

```
MAX_NUMBER = 5.0  # valor m�ximo de coeficiente & x
MIN_NUMBER = -5.0 # valor m�nimo de coeficiente & x
MAX_DEPTH = 5 # profundidad m�xima de AST generado aleatoriamente
MIN_ACCEPTABLE_ERROR = 0.1 # error m�nimo aceptable para ser individuo perfecto
DELTA = 0.1 # Paso de discretizaci�n de x entre MAX_NUMBER y MIN_NUMBER
```

### Par�metros de evoluci�n

```
POPULATION_SIZE = 1000  # Tama�o de poblaci�n
CROSSOVER_CHANCE = 0.5  # Probabilidad de hacer crossover, si no heredan genes directos
SEX_CHANCE = 0.8  # Probabilidad de engendrar un hijo
MUTATION_CHANCE = 0.1  # Probabilidad de que ocurra una mutaci�n en un AST
TOURNAMENT_K = 2  # Elecciones en selecci�n por torneo
```

### Expresi�n objetivo
Aparte de poder configurar el polinomio a gusto, se debe variar la constante ```NUMBER_OF_OPERATIONS``` , para prevenir que se generes AST excesivamente grandes que obstruyan la ejecuci�n.

```
NUMBER_OF_OPERATIONS = 8  # Numero de operaciones m�nimas en el polinomio

def polynomial(x):
    return 3*x**2 + 2*x + 3 + x**3

```
