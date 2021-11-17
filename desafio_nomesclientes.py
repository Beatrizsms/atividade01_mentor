"""import csv
nome = input("Digite o nome que deseja encontrar:")
encontrado = []
with open ("clientes.csv","r") as arquivo:
    nomearquivo = csv.reader(arquivo)
    for x in nomearquivo:
        if "nome" in x:
            encontrado.append(x)

    print(encontrado)"""

import csv
nome = input("Digite o nome que deseja encontrar:")
encontrado = []
with open ('clientes.csv', 'r') as arquivo:
    nomearquivo = csv.reader(arquivo)
    lista_nome = (nomearquivo)
    for x in lista_nome:
        if nome in x:
            encontrado.append(x)

    print("Foram encontrados {} resultado(s) para sua busca".format(len(encontrado)))
    print(encontrado)








