contatos = [
    {"nome": "Andressa Guerra", "telefone": "98296-7397"},
    {"nome": "Bruce Guerra", "telefone": "98364-9672"},
    {"nome": "Gabriel Guerra", "telefone": "95436-9998"}
]

def busca_contato(lista, nome):
    for contato in lista:
        if contato["nome"] == nome:
            return contato["telefone"]
    return None

nome = "Andressa Guerra"
resultado = busca_contato(contatos, nome)

if resultado:
    print(f"O telefone de {nome} é {resultado}.")
else:
    print(f"O contato {nome} não foi encontrado.")