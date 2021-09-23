import random
import time

print("********************************")
print("Bem-vindo à biblioteca de livros")
print("********************************")

lista = []


def adicionar_livro():
    livro = lista.append(input("Digite o nome do livro ou 0 para finalizar: "))
    while livro != "0":
        livro = input("Digite o nome do livro ou 0 para finalizar: ")
        if livro != "0":
            lista.append(livro)
    else:
        print("Seus livros estão sendo sorteados...")
        livro_escolhido = random.choice(lista)
        print("O livro escolhido foi {}".format(livro_escolhido))
        decisao = input("Para repetir o sorteio tecle 1, ou zero para reiniciar o programa ou fechar")
        if decisao != "0":
            repetir_sorteio()
        else:
            fechar()


def fechar():
    lista.clear()
    escolha = input("Digite x para fechar o programa ou outra tecla para reiniciar")
    if escolha != "x":
        adicionar_livro()
    else:
        print("Obrigado por utilizar a biblioteca S2 S2")
        time.sleep(5)
        exit()


def repetir_sorteio():
    coiso = "s"
    while coiso == "s":
        print("Seus livros estão sendo sorteados novamente...")
        livro_escolhido = random.choice(lista)
        print("O livro escolhido foi {}".format(livro_escolhido))
        coiso = input("Você quer repetir o sorteio? Se sim digite s ou x para sair")
    else:
        fechar()


adicionar_livro()
