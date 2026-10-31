def verificar_resultado(resultado):
      if resultado == int(resultado):
       print("O número é inteiro!")
      if resultado % 2 == 0:
       print("O número é par")
       
def somar():
    numeros = []
    quantidade = int(input("Quantos números deseja somar? "))
    for n in range (quantidade):
     numero = float(input("Entre com os números a serem somados: "))
     numeros.append(numero)
    resultado = sum(numeros)
    print(resultado)
    verificar_resultado(resultado)


def subtrair():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))
    resultado = numero1 - numero2
    print(resultado)
    verificar_resultado(resultado)


def multiplicar():
    numeros = []
    quantidade = int(input("Quantos números deseja multiplicar? "))
    for n in range (quantidade):
     numero = float(input("Entre com os números a serem multiplicados: "))
     numeros.append(numero)
    resultado = 1
    for numero in numeros:
     resultado = resultado * numero
    print(resultado)
    verificar_resultado(resultado)


def dividir():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))

    if numero2 == 0:
        print("Não é possível dividir por zero!")
    else: 
        resultado = numero1 / numero2
        print(resultado)
        verificar_resultado(resultado)



def menu():
    print("__Escolha uma operação__")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")

menu()

opcao = input("Escolha uma operação: ")
if opcao == "1":
    somar()

elif opcao == "2":
    subtrair()

elif opcao == "3":
    multiplicar()

elif opcao == "4":
    dividir()

else:
    print("Operador inválido!")



       

   
