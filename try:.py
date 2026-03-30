try:
    arquivo = open("dados.txt","r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
except FileNotFoundError:
    print("arquivo nao encontrado.")