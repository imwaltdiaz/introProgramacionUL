def main():
  num = int(input("Ingrese numero: "))
  while num < 0:
    print("Tiene que ingresar numero positivo")
    num = int(input("Ingrese numero: "))
  while num!=-1:
    if num%2==0:
      print("Ingreso un numero par")
    else:
      print("Ingrese un numero impar")
    num = int(input("ingrese otro número: "))
main()