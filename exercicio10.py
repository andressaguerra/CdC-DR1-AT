#quando clica voltar, a pagina atual vai pra avancar
#quando clica avancar, a pagina atual vai para voltar
#quando navega p outro site, o historico de avancar some

voltar = []
avancar = []
pagina_atual = None

def navegar_para(pagina):
    global pagina_atual
    if pagina_atual:
        voltar.append(pagina_atual)
    pagina_atual = pagina
    avancar.clear()
    print(f"> Navegando para {pagina_atual}...")

def voltar_pagina():
    global pagina_atual
    if not voltar:
        print("> Imagine o botão de voltar cinza aqui.")
        return
    avancar.append(pagina_atual)
    pagina_atual = voltar.pop()
    print(f"> Voltando para {pagina_atual}...")

def avancar_pagina():
    global pagina_atual
    if not avancar:
        print("> Imagine o botão de avançar cinza aqui.")
        return
    voltar.append(pagina_atual)
    pagina_atual = avancar.pop()
    print(f"> Avançando para {pagina_atual}...")

navegar_para("andressa.com.br")
voltar_pagina()
avancar_pagina()

navegar_para("bruce.com.br")
voltar_pagina()
avancar_pagina()