nome = input("Digite o nome que deseja encontrar:").upper()
encontrado = []
arquivo = open('clientes.txt', 'r', encoding="utf8")
clientes = arquivo.readlines()

for x in clientes:
    if nome in x:
        encontrado.append(x)

print ("Foram encontrados {} resultado(s) para sua busca".format(len(encontrado)))
print ('\n'.join(encontrado))






