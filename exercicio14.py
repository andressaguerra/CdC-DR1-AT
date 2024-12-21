def criar_no(chave):
    return {"chave": chave, "esquerda": None, "direita": None}

def inserir(raiz, chave):
    if raiz is None:
        return criar_no(chave)
    elif chave < raiz["chave"]:
        raiz["esquerda"] = inserir(raiz["esquerda"], chave)
    elif chave > raiz["chave"]:
        raiz["direita"] = inserir(raiz["direita"], chave)
    return raiz

def buscar(raiz, chave):
    if raiz is None:
        return None
    elif raiz["chave"] == chave:
        return raiz
    elif chave < raiz["chave"]:
        return buscar(raiz["esquerda"], chave)
    return buscar(raiz["direita"], chave)

def ordenar(raiz):
    if raiz:
        ordenar(raiz["esquerda"])
        print(raiz["chave"], end=" ")
        ordenar(raiz["direita"])

precos = [100, 50, 150, 30, 70, 130, 170]
raiz = None

for preco in precos:
    raiz = inserir(raiz, preco)

print("BST em ordem:")
ordenar(raiz)
print()

resultado = buscar(raiz, 70)
if resultado:
    print(f"Preço {resultado['chave']} encontrado.")
else:
    print(f"Preço não encontrado.")