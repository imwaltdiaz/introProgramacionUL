# 4.	Escriba un programa en Python que genere 300 números aleatorios entre 2 y 3000. Debe ingresar a una lista aquellos v alores sean primos y ordenar la lista de mayor a menor utilizando el método sort().
# Finalmente, muestre cuantos números de la lista son mayores que 100 utilizando búsqueda secuencial.
import random

def primo(num):
    divisores=2
    for i in range(2,num):
        if num%i==0:
            divisores=divisores+1
            break
    if divisores==2:
        return True
    else:
        return False

def mayores100(lista):
    conta=0
    for i in range(len(lista)):
        if lista[i]>100:
            conta=conta+1
    return conta        

def main():
    lista=[]
    for i in range(300):
        num=random.randint(2, 3000)
        if primo(num):
            lista.append(num)
    lista.sort(reverse=True)
    print("Los valores mayores a 100 son: ",mayores100(lista))
            
main()
