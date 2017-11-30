# Genetic-Programming
Implementación de algoritmo de Programación Genetica sobre el lenguaje definido por las funciones ```+, -, *, /``` y los terminales ```numeros y variable x```, en el problema de busqueda de un polinomio en base a sus valores de entrada (x) y salida (y).
## Problema

Dado un **polinomio de una variable** (Ej. ```3x^2 + 2x + 3 + x^3```), encontrar la expresión del polinomio (AST) mediante **programación genetica,** minimizando los errores cuadraticos medios, resultantes de la evaluacion comparada.
## Restricciones

Para el polinomio, se admiten valores de coeficientes entre -5 y 5.

El calculo de erorres cuadraticos medios resulta de evaluar el polinomio esperado y cada individuo con valores de **x** entre -5 y 5.

El error cuadratico minimo aceptable para un individuo perfecto es de 0.1.
## Fitness

Se utiliza la suma de errores cuadrados entre el valor esperado y el valor actual obtenido mediante cada polinomio, para cada x entre -5 y 5.

Por lo que a menor fitness, mejor individuo.
## Seleccion

Por Tournament Selection con k= 2 (modificable)

## Configuracion

Se pueden modificar parametros y el polinomio objetivo dentro del archivo 
```./Global.py```

### Constantes numericas

```
MAX_NUMBER = 5.0  # valor maximo de coeficiente & x
MIN_NUMBER = -5.0 # valor minimo de coeficiente & x
MAX_DEPTH = 5 # profunidad maxima de AST generado aleatoriamente
MIN_ACCEPTABLE_ERROR = 0.1 # error minimo aceptable para ser individuo perfecto
DELTA = 0.1 # Paso de discretizacion de x entre MAX_NUMBER y MIN_NUMBER
```

### Parametros de evolucion

```
POPULATION_SIZE = 1000  # Tamaño de poblacion
CROSSOVER_CHANCE = 0.5  # Probabilidad de hacer crossover, si no heredan genes directos
SEX_CHANCE = 0.8  # Probabilidad de engendrar un hijo
MUTATION_CHANCE = 0.1  # Probabilidad de que ocurra una mutacion en un AST
TOURNAMENT_K = 2  # Elecciones en seleccion por torneo
```

### Expresion objetivo
Aparte de poder configurar el polinomio a gusto, se debe variar la constante ```NUMBER_OF_OPERATIONS``` , para prevenir que se generes AST excesivamente grandes que alenten la ejecucion.

```
NUMBER_OF_OPERATIONS = 8  # Numero de operaciones minimas en el polinomio

def polynomial(x):
    """
    Polinomio ideal al que se quiere converger.
    
    :param x: Valor de evaluacion de x.
    :return: Valor resultado.
    """
    return 3*x**2 + 2*x + 3 + x**3
    ```

```