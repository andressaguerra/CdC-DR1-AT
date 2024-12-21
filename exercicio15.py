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
    return atual["chave"]

def ecnontrar_maximo(raiz):
    atual = raiz
    while atual["direita"] is not None:
        atual = atual["direita"]
    return atual["chave"]

def ordernar(raiz):
    if raiz:
        ordernar(raiz["esquerda"])
        print(raiz["chave"], end=" ")
        ordernar(raiz["direita"])

notas = [85, 70, 95, 60, 75, 90, 100]
raiz = None

for nota in notas:
    raiz = inserir(raiz, nota)

print("BST em ordem:")
ordernar(raiz)
print()

minimo = encontrar_minimo(raiz)
print(f"Nota mínima: {minimo}")

maximo = ecnontrar_maximo(raiz)
print(f"Nota máxima: {maximo}")