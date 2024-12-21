perfis = {
    "andguerra": {"nome": "Andressa Guerra", "email": "andressa.guerra@al.infnet.edu.br", "idade": 28},
    "batbulldog": {"nome": "Bruce Guerra", "email": "bruce@email.com", "idade": 7},
    "black_cat": {"nome": "Gabriel Guerra", "email": "gabriel@email.com", "idade": 16}
}

def buscar_perfil(tabela, usuario):
    return tabela.get(usuario)

usuario = "andguerra"
resultado = buscar_perfil(perfis, usuario)

print(f"Informações de {usuario}: {resultado}")