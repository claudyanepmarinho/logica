nomes_aprovados = ["João", "Maria", "Pedro", "Lia"]

nome = input("Digite seu nome: ").strip()

if nome.lower() in [n.lower() for n in nomes_aprovados]:
    print(f"{nome} aprovado!")

else:
    print(f"{nome} reprovado!")