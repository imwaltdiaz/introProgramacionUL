def invertir(n):
  a = ""
  for i in range (len(n)-1, -1, -1):
    a = a + n[i]
  return a

def esPalindromo(n):
  numInvertido = invertir(n)
  if n == numInvertido:
    print("Es palindromo")
  else:
    print("No es palindromo")

def main():
  num = str(input("Ingrese numero: "))
  print("El numero invertido es", invertir(num))
  esPalindromo(num)

main()  