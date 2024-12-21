import os

def listar_arquivos(caminho):
    itens = os.listdir(caminho)
    
    for item in itens:
        item_completo = os.path.join(caminho, item)
        if os.path.isfile(item_completo):
            print(item_completo)
        elif os.path.isdir(item_completo):
            listar_arquivos(item_completo)

caminho = r"D:\Desktop\INFNET\2024.4\DR1"
listar_arquivos(caminho)