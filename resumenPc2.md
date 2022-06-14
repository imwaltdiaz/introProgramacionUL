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