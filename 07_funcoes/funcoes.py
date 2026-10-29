#função sem retoro e sem parâmetros
def sobre():
    print("Desenvolvido por: Claudyane Marinho")

#função com parâmetros
def turma(turma, ano):
    print(f"Turma: {turma} - {ano}")

    #função com retorno e com parâmetros
def somar(numero1, numero2):
    return numero1+ numero2

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))

sobre()
turma("AD-05", 2026)

resultado = somar(10, 5)
print(f"A soma de 10+ 5 = {resultado}")

#print(f"A soma de {numero1} + {numero2} = {resultado}")