livros = list(range(1, 100001))

def busca_binaria(lista, isbn):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == isbn:
            return meio, iteracoes
        elif lista[meio] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None, iteracoes

def busca_linear(lista, isbn):
    iteracoes = 0
    for i in range(len(lista)):
        iteracoes += 1
        if lista[i] == isbn:
            return i, iteracoes
        
    return None, iteracoes

isbn = 66666
indice_binaria, iteracoes_binaria = busca_binaria(livros, isbn)
indice_linear, iteracoes_linear = busca_linear(livros, isbn)

print(f"Busca binária - Índice: {indice_binaria}, Iterações: {iteracoes_binaria}")
print(f"Busca linear - Índice: {indice_linear}, Iterações: {iteracoes_linear}")