lista = [10,30,50,70]
print(lista)
print(id(lista))
lista2 = lista
print(id(lista2))

for i in range(len(lista)):
    print(id(lista[i]))

# lista = []
# valorInicial = int(input((f'Digite o primeiro valor: ')))
# vezesASerAcrescido = int(input((f'Quantas vezes eles será incrementado?'))
# )
# valorAIncrementar = int(input(f'Em quanto ele será acrescido?'))

# lista.append(valorInicial)
# for i in range(vezesASerAcrescido):
#    valorInicial+=valorAIncrementar
#    lista.append(valorInicial) 
#print(lista)