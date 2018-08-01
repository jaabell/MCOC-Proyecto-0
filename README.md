# MCOC-Proyecto-0
MCOC-Proyecto-0

Introducción
==============

En este proyecto deben ilustrar con algun ejemplo, distinto de este, el efecto de perdida de significancia. 
Ver [enunciado oficial](https://www.dropbox.com/s/pzxwx4c03tqra9t/proyecto0.pdf?dl=0). 

Este ejemplo
==============


Aquí pueden ver, a modo de ejemplo, el caso discutido en clases.Se muestra como la operación de promedio `sp.mean` pierde significancia al aumentar el tamaño de la muestra a promediar. Esto es una version mas elaborada de la discución en la [documentación de scipy](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html).

Se implementan y comparan 5 ideas.

 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `sp.mean` a lo bruto. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float64` y usar `sp.mean` a lo bruto. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `sp.mean` con un acumulador interno de tipo `sp.float64`.
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar una función de promedio `smart_mean` diseñada para minimizar el error de redondeo sacrificando más uso de memoria. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float64` y usar una función de promedio `smart_mean`.

Resultados
==============

Se define el error relativo como 

	ERROR = (Promedio_Calculado - Resultado_Exacto) / Resultado_Exacto

Abajo se muestra como va creciendo el error relativo en la medida en que se consideran cada vez mas números. Esto ocurre debido a la perdida de significancia en la operacion suma usada internamente por el algoritmo de `sp.mean`. 

![Results](loss-of-significance.png)

Output de la consola:

	N = 32768
	  mean_1 = 0.549999952316   (error_1 = 0.000008669767%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000000%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 65536
	  mean_1 = 0.550000190735   (error_1 = 0.000034679066%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000000%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 131072
	  mean_1 = 0.550000190735   (error_1 = 0.000034679066%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000000%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 262144
	  mean_1 = 0.549999237061   (error_1 = 0.000138716264%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000000%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 524288
	  mean_1 = 0.549999237061   (error_1 = 0.000138716264%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000001%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 1048576
	  mean_1 = 0.550003051758   (error_1 = 0.000554865057%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000001%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 2097152
	  mean_1 = 0.550003051758   (error_1 = 0.000554865057%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000002%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)
	N = 4194304
	  mean_1 = 0.549987792969   (error_1 = 0.002219460227%)
	  mean_2 = 0.550000000000   (error_2 = 0.000000000002%)
	  mean_3 = 0.550000000745   (error_3 = 0.000000135465%)
	  mean_4 = 0.550000011921   (error_4 = 0.000002167442%)
	  mean_5 = 0.550000000000   (error_5 = 0.000000000000%)


Recursos
==============

+ Para escribir su `README.md` [https://help.github.com/articles/basic-writing-and-formatting-syntax]
+ Articulo wiki sobre el tema: [https://en.wikipedia.org/wiki/Loss_of_significance]
+ [https://en.wikiversity.org/wiki/Numerical_Analysis/Loss_of_Significance]
+ [https://www.youtube.com/watch?v=0MSaJwjYtmU]
+ [http://www.physics.utah.edu/~detar/lessons/c++/quadratic/node3.html]
+ [http://www.math.pitt.edu/~trenchea/math1070/MATH1070_2_Error_and_Computer_Arithmetic.pdf]