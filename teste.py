with open("seu_arquivo.py", "rb") as f:
    conteudo = f.read()

with open("seu_arquivo.py", "w", encoding="utf-8") as f:
    f.write(conteudo.decode("latin-1"))
