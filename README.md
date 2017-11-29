# Genetic-Programming

En base a las funciones ```+, -, *, /``` y los terminales ```numeros, variable x```. 
Dado un conjunto de valores de X y de valores reales (float), encuentra el **polinomio** que mejor se ajusta, mediante GP.

## Restricciones
Para la prediccion, se aceptara un rango de valores de x entre -1 y 1.
Para los numeros terminales, pueden tomar valores entre -5 y 5.

## Fitness
Se utiliza la suma de errores cuadrados entre el valor esperado y el valor actual obtenido mediante cada polinomio, para cada x.

* Condicion esperada (de terminación): Fitness menor a 0.1

## Seleccion
or Tournament con k= 2.

## Parametros
* Tama?o de poblacion: 4
* Probabilidad de cross over: 50%
* Probabilidad de reproduccion: 25%
* Probabilidad de mutacion en un subtree: 25%
* Limite de tama?o de arbol: Infinito

