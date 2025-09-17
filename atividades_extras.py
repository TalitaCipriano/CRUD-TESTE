# ALUNOS E MÉDIA
# alunos = []

# def adicionar_alunos():
#     nome = input("Digite o nome do aluno: ")
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     media = (nota1 + nota2) / 2
#     alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2, "média": media})

# def listar_alunos():
#     for aluno in alunos:
#         print(f"{aluno['nome']} - média: {aluno['média']:.2f}")

# while True:
#     print("\n--- SISTEMA DE ALUNOS ---")
#     print("1 - Adicionar Alunos")
#     print("2 - Listar alunos")
#     print("0 - Sair")
#     opcao = input("Escolha: ")

#     if opcao == "1":
#         adicionar_alunos()
#     elif opcao == "2":
#         listar_alunos()
#     elif opcao == "0":
#         print("Encerrando...")
#         break
#     else:
#         print("Opção inválida")

# JOGO DA FORCA
import random

palavras = ["pernambuco", "ginastica", "futebol", "teclado", "linguagem", 
            "televisao", "ponte", "juiz"]
palavra = random.choice(palavras)
tentativas = []
erros = 0

def validar_chute(chute):
    if len(chute) != 1 or not chute.isalpha():
        print("Apenas letras são aceitas. Tente novamente.")
        return False
    return True

print("\n*** JOGO DA FORCA***")

while True:
    segredo = ""
    for letra in palavra:
        if letra in tentativas:
            segredo += letra + " "
        else:
            segredo += "_ "
    print(segredo)

    if "_" not in segredo:
        print("\n ***** PARABÉNS!!! *****\n     VOCÊ VENCEU")
        break
    
    chute = input("Digite uma letra: ").lower()

    # Valida o chute antes de continuar
    if not validar_chute(chute):
        continue

    if chute in tentativas:
        print("Você já tentou essa letra.")
        continue

    tentativas.append(chute)

    if chute not in palavra:
        erros += 1
        print(f"Errou! Você já tem um total de {erros} erros")
        if erros >= 10:
            print("Você perdeu! A palavra era:", palavra)
            break