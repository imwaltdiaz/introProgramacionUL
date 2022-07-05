```py
# while 
while comparison:
  #Do this
  # add 1 

# for i in range
for i in range(start, stop, how/step):
  #Do this
  #the stop does not include its number
  #The step cpul be +1(default), -1, or 3 or any int

# Arrays / Lists
n = len(arrayName)
#Returns the numbers of elements

for i in arrayName:
  # You run each element of the list and do something about it

# Bucles anidados



arrayName.append(element)
# add an element inside the array (the last position)

arrayName.pop(number/position)
# deletes or remove the element of an array, remeber, the first position is 0

arrayName.remove(nameOfElement)
# Deletes the element with equeal name or value, only works for the first occurrence of the specified value

arrayName.reverse()
# reverse the array, you cant store this inside a variable, this changes the same array

arrayName.sort()
array.sort(reverse=True|False,)
# sorts the array, reverse true will sort descending, default is reverse = false (ascending)


# Functions
def functionName(parameter1,parameter2):
  # Execute this
functionName(entry1,entry2)
```

# Recursividad

basicamente una funcion arriba para una serie, ejm funcion n + nmbreFuncion(n-1)

# analisis de algoritmos

los for te toman m + 1 o n + 1, si tenemos de n a m, entonces m-n+1 y con lo de adentro pasara igual
un for que incluye  otro for, se multiplicara

operaciones e if toman 1

# Tuplas
tuple = (0,1,2,4)

# Diccionarios
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
thisdict.get("model")
keys() method will return a list of all the keys in the dictionary.
values() method will return a list of all the values in the dictionary.
items() method will return each item in a dictionary, as tuples in a list.

• .get( ) : Devuelve un valor del diccionario.
• .values( ) : Devuelve todos los valores del diccionario.
• .keys( ) : Devuelve todas las claves del diccionario

d.clear()	Removes all the elements from the dictionary
d.copy()	Returns a copy of the dictionary
d.fromkeys()	Returns a dictionary with the specified keys and value
d.get()	Returns the value of the specified key
d.items()	Returns a list containing a tuple for each key value pair
d.keys()	Returns a list containing the dictionary's keys
d.pop()	Removes the element with the specified key
d.popitem()	Removes the last inserted key-value pair
d.setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
d.update()	Updates the dictionary with the specified key-value pairs
d.values()	Returns a list of all the values in the dictionary

# Algoritmos

## Busqueda

**Busqueda secuencial:**

def main():
#define la lista donde se va a buscar
lista1 = [1, 7, 9, 10, 5, 8, 7, 10]
longitud = len(lista1)
print("La lista donde se va a buscar es: ", lista1)
#define el elemento que se va a buscar
buscado = 10
print("Se va a buscar el elemento: ", buscado)
'''
Compara cada elemento de la lista con el valor buscado.
Retorna el indice el primer elemento igual que se haya encontrado.
'''
for x in range(0, longitud):
if(lista1[x] == buscado):
print("El elemento buscado tiene el indice: ", x)
break


**Busqueda binaria:**
Debe estar en orden
Toma la mitad

def main():
  lista = [10, 20, 50, 60, 90, 110]
  pos = -1
  busca = int(input("Numero a buscar: "))
  izq = 0
  der = len(lista) - 1
  while izq <= der:
  medio = (izq + der) // 2
    if busca == lista[medio]:
    pos = medio
      break
    else:
      if busca < lista[medio]:
        der = medio - 1
      else:
        izq = medio + 1
print(pos)


## Ordenamiento

Burbuja:

Recorres una lista con 2 for, uno con el len -1 y el menor iniciando i+1 pero todo el len

def burbuja(lista):
  for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
      if(lista[i] > lista[j]):
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
return lista


Quicksort:
1) Dividir : Si la secuencia S tiene 2 o más elementos,
seleccionar un elemento x de S como pivote. Cualquier elemento
arbitrario, como el último, puede servir. Eliminar los elementos
de S dividiéndolos en 3 secuencias:
  • L, contiene los elementos de S menores que x
  • E, contiene los elementos de S iguales a x
  • G, contiene los elementos de S mayores que x
2) Recursión: De forma recursiva ordenar L y G
3) Vencer: Finalmente, colocar nuevamente los elementos en S
en orden, primero insertar los elementos de L, después E, y los
elementos de G.

Recursividad
Caso base:
  Tamaño <= 1
  Retorna Lista 

Parte recursiva:
  

Tomamos un pivot como 9, de lista de los mayores y lista de menores
Y otra ves ordenarmeos estas listas 

Retyorna 
  Lista Me + Lista Ig + Lista Ma

Esto se repite hasta que el tamaño sea igual al caso base 

```py
def quicksort(lista):
    if len(lista)<=1:
        return lista
    else:
        listaMa = []
        listaMe = []
        listaIg = []
        pivot = lista[0]
        for i in range(0, len(lista)):
            if lista[i]>pivot:
                listaMa.append(lista[i])
            elif lista[i]<pivot:
                listaMe.append(lista[i])
            else:
                listaIg.append(lista[i])
        listaMa = quicksort(listaMa)
        listaMe = quicksort(listaMe)
        return listaMe + listaIg + listaMa
```

# EsPrimo
```py
def esPrimo(n):
  cuentaDivisores = 2
  for i in range (2 , n):
    if n % i == 0:
      cuentaDivisores = cuentaDivisores + 1
  if cuentaDivisores > 2:
    print("n no es primo")
  else:
    print("n es primo")

```