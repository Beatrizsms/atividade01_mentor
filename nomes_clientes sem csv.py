nome = input("Digite o nome que deseja encontrar:").upper()
encontrado = []


clientes =['CLEVERSON PIRES', 'BEATRIZ MAGALHÃES', 'AMANDA SANTANA','JESSICA BARBOSA', 'JESSICA SANTANA', 'MIGUEL MARTINS',
'GABRIEL PEREIRA', 'GABRIELE PEREIRA', 'RAFAEL PEIXOTO', 'BEATRIZ SANTANA', 'CATARINA FERNANDES', 'JOÃO SOUZA', 'GABRIELE SOUZA',
'MARIA SOUZA', 'MARIA ANTÔNIA', 'JOÃO SILVA', 'ARTHUR FREITAS', 'JAQUELINE LIÑARES', 'CARLA MENDES', 'VITOR SANTOS']
for x in clientes:
    if nome in x:
        encontrado.append(x)

print ("Foram encontrados {} resultado(s) para sua busca".format(len(encontrado)))
print (','.join(encontrado))














