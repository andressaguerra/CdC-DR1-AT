fila_chamados = []

def adicionar_chamado(chamado): #"..sete dias.."
    fila_chamados.append(chamado)
    print("> Chamado adicionado!")

def atender_chamado():
    if not fila_chamados:
        print("Você respondeu todos, parabéns!")
        return
    fila_chamados.pop(0)
    print("> Atendendo chamado...")

def exibir_chamados():
    if not fila_chamados:
        print("\nChamados: [...]\n")
    else:
        print(f"\nChamados: {fila_chamados}\n")

#resultado esperado: exibe vazia, adiciona 3, exibe, atende 1, exibe, atende +1, exibe, adiciona +1, exibe, atender +3 sendo que o ultimo vazio, exibe vazio
exibir_chamados()

adicionar_chamado("Bruce fez xixi")
adicionar_chamado("Limpar olhos do Bruce")
adicionar_chamado("O almoço do Bruce não estava tão gostoso")
#eh um sistema de hã... um sistema de chamados em que o cliente é meu cachorro

exibir_chamados()

atender_chamado()
exibir_chamados()

atender_chamado()
exibir_chamados()

adicionar_chamado("Bruce quer brincar")
exibir_chamados()

atender_chamado()
atender_chamado()
atender_chamado()
exibir_chamados()