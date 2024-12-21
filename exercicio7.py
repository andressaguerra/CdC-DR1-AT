def verificar_duplicatas(lista):
    tabela_hash = {}
    for elemento in lista:
        if elemento in tabela_hash:
            return True
        tabela_hash[elemento] = True
    return False

lista = [1, 2, 3, 4, 5, 6]
lista_duplicada = [1, 6, 3, 4, 5, 6]

print(f"Lista sem duplicatas: {verificar_duplicatas(lista)}")
print(f"Lista com duplicatas: {verificar_duplicatas(lista_duplicada)}")