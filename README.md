# introProgramacionUL

## Concepto de Variable 

Las variables son utilizadas para referenciar (apuntar) información en memoria

La variable debe estar en un contenedor

La variable tieneun identificador para acceder a la información

Una variable puede tener valores diferentes durante el desarrollo de su programa 

"Garbage collector" proceso que consiste de liberar espacios de memoria que no almacenan ninguna variable

## Concepto de variable

<variable> = <expresion>

La asignación se da de derecha a izquierda

Todo lo que captures del usuario debe ir a un contenedor o variable

La expresión podría ser una formula

Java es tipado y py es no tipado

## Tipos de datos - Definición 

Variables numericos
- int: con numeros enteros
- float: condecimales

Variables alfanuméricas
- Cadenas de texto

Variables lógicas
- Con un valor booleano (true or false)

```py
a = 10
type(a)
<class = 'int'>

a = 10.5
type(a)
<class = 'float'>

a = 'luis'
type(a)
<class = 'string'>

a = 'Luis23'
type(a)
<class = 'string'>

a = True
type(a)
<class = 'bool'>
```

**Representación de algoritmos numéricos**

Utilización de constantes
- Adms de variables, un algoritmo requiere de constantes 

Variables númericas - Tipo int
- Permite almacerar números enteros, esto es variables que no son fracciones ni podran serlo

Variables tipo - float
- Contienen decimal, si no tiene decimal, trabaja con int, y con decimal trabaja con float

```py
a = True or False
print(a)
True
type(a)
<class = 'bool'>

a = 'Luis'
b = 'Borjas'
print(a,b)
Luis Borjas

print(a+b)
Luisborjas
```

## Definición de algoritmo
Secuencia de instrucciones que representa la solución de un problema o situación determinada

Que consta un algoritmo??
- Entrada
    - Que se necesita para realizar los pasos

- Salida
    - Que se obtiene al final del algoritmo

- Proceso
    - De transformación, hace los pasos

- Tipos de datos
    - Números: enteros, reales, complejos
    - Texto: letras, palabras, frases
    - Otros


Características
- Preciso
- Definido
- Finito
- Debe producir un resultado

**Técnicas de representación**
- Diagramas de flujo
- Pseudocódigo
- Lenguaje natural
- Formulas matemáticas

**Diagramas**
Permite representar solución tras paso a paso de que hacer el proceso
> Insertar imagen

**Pseudocodigo**
Permite representar el algoritmo pero con palabras imperativas

Se debe representar lo que se quiere ahí

Osea verbos de acción: Inicie,  calcule, lea, imprima, finalice

**Construccion**
Ejemplo
- Objetivo: calcular el precio de una manzana
- Entradas
    - Precio (en soles) del kilo de manzanas [K]
    - Peso (en gramos) promedio de una manzana [P]
- Salida
    - Precio (en soles) de una manzana [M]

```py
Inicio
    Ingresar valor de K y P
    Calcular G = K/1000
    Calcular M = G x P
    Devolver el Valor de M
Fin
```

> Insertar modo de diagrama de flujo