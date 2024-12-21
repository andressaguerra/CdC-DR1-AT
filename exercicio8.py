#vamos assumir que seja um jogo de gartic de 3 rodadas com 3 jogadores
jogadores = [
    {"nome": "Andressa", "pontos": 72},
    {"nome": "Bruce", "pontos": 63},
    {"nome": "Gabriel", "pontos": 70}
]

def seletcion_sort(lista):
    n = len(lista)
    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if lista[j]["pontos"] > lista[indice]["pontos"]:
                indice = j
        lista[i], lista[indice] = lista[indice], lista[i]

seletcion_sort(jogadores)

for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontos']} pontos")