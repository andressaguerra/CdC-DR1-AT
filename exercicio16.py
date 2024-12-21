def criar_no(chave):
    return{"chave": chave, "esquerda": None, "direita": None}

def inserir(raiz, chave):
    if raiz is None:
        return criar_no(chave)
    elif chave < raiz["chave"]:
        raiz["esquerda"] = inserir(raiz["esquerda"], chave)
    elif chave > raiz["chave"]:
        raiz["direita"] = inserir(raiz["direita"], chave)
    return raiz

def encontrar_minimo(raiz):
    atual = raiz
    while atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual

def remover(raiz, chave):
    if raiz is None:
        return raiz
    elif chave < raiz["chave"]:
        raiz["esquerda"] = remover(raiz["esquerda"], chave)
    elif chave > raiz["chave"]:
        raiz["direita"] = remover(raiz["direita"], chave)
    else:
        if raiz["esquerda"] is None and raiz["direita"] is None:
            return None
        elif raiz["esquerda"] is None:
            return raiz["direita"]
        elif raiz["direita"] is None:
            return raiz["esquerda"]
        else:
            sucessor = encontrar_minimo(raiz["direita"])
            raiz["chave"] = sucessor["chave"]
            raiz["direita"] = remover(raiz["direita"], sucessor["chave"])
    return raiz

def ordernar(raiz):
    if raiz:
        ordernar(raiz["esquerda"])
        print(raiz["chave"], end=" ")
        ordernar(raiz["direita"])

codigos = [45, 25, 65, 20, 30, 60, 70]
raiz = None

for codigo in codigos:
    raiz = inserir(raiz, codigo)

print("BST em ordem:")
ordernar(raiz)
print("\n")

remocoes = [20, 25, 45]

for codigo in remocoes:
    raiz = remover(raiz, codigo)
    print(f"> Código {codigo} removido!\n")
    print("BST em ordem:")
    ordernar(raiz)
    print("\n")