def somar():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))
    resultado = numero1+ numero2
    print(resultado)


def subtrair():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))
    resultado = numero1 - numero2
    print(resultado)

def multiplicar():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))
    resultado = numero1 * numero2
    print(resultado)

def dividir():
    numero1 = float(input("Adicione o primeiro número: "))
    numero2 = float(input("Adicione o segundo número: "))

    if numero2 == 0:
        print("Não é possível dividir por zero!")
    else: 
        resultado = numero1 / numero2
        print(resultado)





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