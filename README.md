# Árbol Binario Interactivo en Python

este repositorio contiene un programa interactivo en python que permite construir un **árbol binario de búsqueda** a partir de datos ingresados por el usuario. una vez construido, el árbol puede recorrerse en **preorden**, **inorden** y **postorden**, mostrando distintas formas de acceder a su estructura interna.

## objetivo

explorar de forma práctica cómo funciona una estructura de datos jerárquica como el árbol binario. el proyecto busca:
- facilitar la comprensión de cómo se insertan y ordenan los datos en un árbol binario
- mostrar cómo los recorridos afectan la forma en que se accede a los nodos
- reforzar el uso de recursividad como herramienta para recorrer estructuras no lineales

## descripción

el programa solicita al usuario que defina un nodo raíz, y luego permite ingresar sucesivos valores para construir el árbol. se realiza una inserción ordenada: valores menores van a la izquierda, mayores a la derecha. finalmente, el programa imprime los recorridos del árbol:

- **preorden**: raíz → izquierda → derecha  
- **inorden**: izquierda → raíz → derecha  
- **postorden**: izquierda → derecha → raíz

esto permite visualizar claramente la lógica de navegación en árboles binarios.

## cómo usarlo

1. ejecutar el archivo `arbol.py`
2. ingresar un valor para el nodo raíz
3. seguir ingresando valores cuando se solicite
4. escribir `yes` para finalizar la construcción
5. el programa mostrará los recorridos en consola

## dependencias

no se requieren librerías externas. funciona con cualquier versión reciente de python 3.

## video explicativo

[ver demostración](https://www.youtube.com/watch?v=YPaNK7dW0Vw)

## licencia

este proyecto es de uso libre para fines educativos.
