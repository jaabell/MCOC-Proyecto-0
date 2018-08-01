# MCOC-Proyecto-0
MCOC-Proyecto-0

Intro
======

En este proyecto deben ilustrar con algun ejemplo, distinto de este, el efecto de perdida de significancia. 
Ver [enunciado oficial](https://www.dropbox.com/s/pzxwx4c03tqra9t/proyecto0.pdf?dl=0). 

Aquí pueden ver, a modo de ejemplo, el caso discutido en clases.Se muestra como la operación de promedio `sp.mean` pierde significancia al aumentar el tamaño de la muestra a promediar. Esto es una version mas elaborada de la discución en la [documentación de scipy](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html).

Se implementan y comparan 5 ideas.

 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `sp.mean` a lo bruto. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float64` y usar `sp.mean` a lo bruto. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar `sp.mean` con un acumulador interno de tipo `sp.float64`.
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float32` y usar una función de promedio `smart_mean` diseñada para minimizar el error de redondeo sacrificando más uso de memoria. 
 1. Definir el arreglo `a` con tipo de datos `dtype=sp.float64` y usar una función de promedio `smart_mean`.

Se define el error relativo como 


![Results](loss-of-significance.png)


Recursos
############

+ Para escribir su `README.md` [https://help.github.com/articles/basic-writing-and-formatting-syntax]
+ Articulo wiki sobre el tema: [https://en.wikipedia.org/wiki/Loss_of_significance]
+ [https://en.wikiversity.org/wiki/Numerical_Analysis/Loss_of_Significance]
+ [https://www.youtube.com/watch?v=0MSaJwjYtmU]
+ [http://www.physics.utah.edu/~detar/lessons/c++/quadratic/node3.html]
+ [http://www.math.pitt.edu/~trenchea/math1070/MATH1070_2_Error_and_Computer_Arithmetic.pdf]