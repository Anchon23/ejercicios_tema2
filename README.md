# ejercicios_tema2

# Ejercicio 1: Construye tu Propio Universo Estelar


En este ejercicio emocionante, trabajarás en simular un universo lleno de planetas, estrellas y asteroides usando conceptos de geometría espacial y programación orientada a objetos. No se trata de hacer cálculos complejos; es más sobre poner en práctica tu creatividad para simular un cosmos interconectado.

Punto de partida

Esto es más que un simple ejercicio de programación. Estás a punto de simular un universo entero. Si la astronomía o la física no son lo tuyo, estás en libertad de saltarte este ejercicio. Sin embargo, ten en cuenta que te perderás una de las aventuras más fascinantes de este curso.

Conceptos Básicos
Espacio Tridimensional: Imagina un espacio en tres dimensiones, formado por tres ejes perpendiculares entre sí: ,  y .
Coordenadas y Puntos: Similar al plano cartesiano, pero con una dimensión extra. Un punto se representa como .
Vectores Espaciales: Un vector es simplemente un segmento orientado en el espacio 3D, que va desde un punto inicial a un punto final.
Ejercicio
Crea una clase llamada Estrella con tres coordenadas ,  y .
Añade un método constructor para generar estrellas fácilmente. Si no se reciben coordenadas, las coordenadas por defecto serán cero.
Implementa el método __str__ para que al imprimir la estrella, las coordenadas aparezcan en el formato .
Agrega un método galaxia para determinar en qué galaxia del universo podría estar ubicada la estrella basada en sus coordenadas.
Implementa un método distancia para calcular la distancia entre dos estrellas usando la fórmula de distancia en el espacio 3D.
Nota: Para el cálculo de la distancia, puedes usar la raíz cuadrada que se encuentra en el módulo math de Python: import math; math.sqrt().



Experimentación
Crea las estrellas A(2, 3, 1), B(4, 4, 4), y C(-3, -1, 0) y imprímelas por pantalla.
Determina en qué galaxias podrían estar estas estrellas.
Calcula y muestra la distancia entre las estrellas A y B, y entre B y C.
(Opcional) Encuentra qué estrella está más lejos del origen .


# Ejercicio 2: El Diálogo Zen
Tu tarea es transformar un texto en bruto en una conversación formateada sin cambiar directamente el texto. Utiliza tus habilidades en el manejo de cadenas y listas en Python para hacerlo más legible.

Texto original:

un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

Resultado deseado:

Un día que el viento soplaba con fuerza...

Mira como se mueve aquella banderola -dijo un monje.
Lo que se mueve es el viento -respondió otro monje.
Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.

# Ejercicio 3: La Magia de las Listas Numéricas
Crea una función llamada magia_numerica() que realice varias transformaciones en una lista de números sin modificar la lista original. Las tareas son las siguientes:

Eliminar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Sumar todos los números que quedan.
Colocar esta suma como el primer elemento de la lista.
Verifica que la suma de todos los números a partir del segundo elemento es igual al primer número de la lista.

