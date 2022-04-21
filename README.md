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



**Construccion de algoritmos**

Operaciones basicas
Escribir un algorimo que lea una longitud medida en pies y la convierta en metros y muestre un resultado

```js
Pies es la entrada y pies es la salida

//Entradas: Longitud en pies

//salidas: longitud en metros

//Objetivo: Convertir pies a metros

/* 
Inicio
    Ingresar longitud en pies y asignar a P
    Calcular P * 0.3048 y asignar a Resultado
    Mostrar "El resultado es", Resultado
Fin
*/ 

Otro caso es

/* 
Inicio
    Ingresar y asignar a P
    Asignar 0.3048 a Cons
    Calcular P + Cons y asignar a R
    Mostrar "El resultado es", R
Fin
*/ 
```

Escribir algoritmo que ingrese subtotal y tasa de gratuitidad

Entradas: Subtotal y tasa gratuidad
Salidas: Gratuidad y total
Objetivo: Calcular gratuidad y total

```
Inicio
    Ingresar subtotal (S/) y asignar a ST
    Ingresar tasa de gratuidad (%) y asignar a TG
    Calcular ST * TG y asignar a G
    Calcular ST + G y asignar a Tot
    Mostrar "Gratuidad", G
    Mostrar "Total", Tot
Fin
```

**Combinación de operaciones básicas**

```js
Inicio
    Ingresar el monto ahorrado mensual($) y asignar a ahorroConst
    Ingresar tasa efectiva anual(%) y asignar a TEA 
    Calcular ((1+TEA)^(1/12)-1) y asignar a TEM
    Calcular (1 + TEM) y asignar a oTEM
    Calcular (ahorroConst*oTEM) y asignar a M1
    Calcular (ahorroConst + M1)*oTEM y asignar a M2
    Calcular (ahorroConst + M2)*oTEM y asignar a M3
    Calcular (ahorroConst + M3)*oTEM y asignar a M4
    Mostrar "Monto Mes 4", M4
Fin
```


```js
Inicio
    Ingresar Monto Mensual y asignar a Monto
    Asignar 1 + 0.00407 a Incremento
    Calcular Monto * Incremento y asignar a M1
    Calcular (Monto+M1) * Incremento y asignar a M2
    Calcular (Monto+M2) * Incremento y asignar a M3
    Calcular (Monto+M3) * Incremento y asignar a M4
    Mostrar "Monto Mes 4", M4
Fin
```

**Estructuras de Decisión**
Debes elegir si vas a un lado o vas por el otro

```py
# Esto es un comentario
"""
Esto también  es un comentario
"""
def main():
    pass
#pass hace que vayas a la sgte linea
main()
```

```py
# Esta es la plantilla de trabajo
def main():
    pass
main()
```
py no trabaja de arriba a abajo, debes avisarle cual es la función principal

ejercicio de clase:
```py
def main():
    fahren = float(input("Ingrese teperatura en Fahrenheit: "))
    # va a recibir un input y lo va a solicitar recibir como float
    celsius = (fahren - 32)*(5/9)
    print("La temperatura en celsius es: ", celsius)
    if celsius <= 17:
        print("Es un dia frío")
    if celsius > 17:
        print("Es un dia caluroso")
    
main()
```

Y mi opción para que te cargue con solo 2 decimales:
```py
def main():
    fahren = float(input("Ingrese teperatura en Fahrenheit: "))
    celsius = (fahren - 32)*(5/9)
    print("La temperatura en celsius es: ", '%.2f' %celsius)
    if celsius <= 17:
        print("Es un dia frío")
    if celsius > 17:
        print("Es un dia caluroso")
    
main() 
```

La forma de poner la función principal es:
```py
if __name__ == "__main__",
    main()
```

Selectiva de decisión "Two ways"
```py
def main():
    fahren = float(input("Ingrese teperatura en Fahrenheit: "))
    # va a recibir un input y lo va a solicitar recibir como float
    celsius = (fahren - 32)*(5/9)
    print("La temperatura en celsius es: ", '%.2f' %celsius)
    if celsius <= 17:
        print("Es un dia frío")
    else:
        print("Es un dia caluroso")
    
main() 
```
Elif es else if

EJercicios 2:

1
```js
INICIO
    Ingresar monto de pago($) y asignar a MONTO
    Si MONTO <= 100 entonces
        Mostrar "Pago con efectivo"
    Sino si MONTO > 100 y MONTO <= 300
        Mostrar "Pago con Débito"
    Sino 
        Mostrar "Pago con Credito"
FIN
```

Otra solución

```js
INICIO
    Ingresar monto de pago($) y asignar a MONTO
    SI MONTO <= 100 entonces
        Mostrar "Pago con Efectivo"
    SINO
        SI MONTO > 100 y MONTO <= 300
            Mostrar "Pago con Debito"
        Sino 
            Mostrar "Pago con Crédito"
FIN
```
En py
```py
def main():
  monto = float(input("Ingrese monto: "))
  # if monto <= 100:
  #   print("Pago con efectivo")
  # elif monto>100 and monto <=300:
  #   print("Pago con debito")
  # else:
  #   print("Pago con crédito")
  if monto <= 100:
    print("Pago con efectivo")
  else: 
    if monto>100 and monto <=300:
      print("Pago con débito")
    else:
      print("Pago con crédito")
main()
```

2
```js
INICIO
    Ingresar dividendo y asignar a DIVIDENDO
    Ingresar divisor y asignar a DIVISOR
    Si DIVISOR es igual a 0 entonces
        Mostrar "No se puede dividir entre 0"
    SINO
        Si DIVIDENDO $ DIVISOR es igual a 0 entonces
            Mostrar "Division Exacta"
        Sino
            Mostrar "División No Exacta"

FIN
```

en py
```py
def main():
  dividendo = float(input("Ingrese el dividendo: "))
  divisor = float(input("Ingrese el divisor: "))
  if divisor == 0:
    print("No existe la división entre 0")
  else:
    result = dividendo/divisor
    print("El resultado de la división es ", result)
    if dividendo%divisor == 0:
      print("Division exacta")
    else:
      print("Division no exacta")
main()
```
4
```js
INICIO
    Ingresar año actual y asignar a Actual
    Ingresar año cualquier y asignar a X 
    Calcular ACTUAL - X y asignar a DIF
    Si DIF es menor a 0
        Mostrar "Faltan", DIF, "Años"
    Sino 
        Si DIFE es igual a 0 entonces
            Mostrar "Años iguales"
        Sino
            Mostrar "Han pasado", DIFE, "años" 
FIN
```

Ahora en py
