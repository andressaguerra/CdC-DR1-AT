def knapsack(capacidade, pesos, valores, n):
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                tabela[i][w] = 0
            elif pesos[i - 1] <= w:
                tabela[i][w] = max(
                    valores[i - 1] + tabela[i - 1][w - pesos[i - 1]],
                    tabela[i - 1][w]
                )
            else:
                tabela[i][w] = tabela[i - 1][w]

    return tabela[n][capacidade]

pesos = [6, 10, 8, 2]
valores = [4, 5, 5, 2]
capacidade = 18
n = len(pesos)

resultado = knapsack(capacidade, pesos, valores, n)
print(f"Valor máximo que pode ser obtido: {resultado}")