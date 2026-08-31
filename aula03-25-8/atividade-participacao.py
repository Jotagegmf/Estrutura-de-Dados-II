# Atividade desenvolvida por:
#  João Gabriel Gonçalves
# João Victor Montalvão

lista = [10,20,30]

# Exibir a lista inicial e seu id(); ok
# Adicionar um elemento ao final com append(); ok
# Inserir um elemento em uma posição específica com insert();
# Remover um elemento pelo valor utilizando remove();
# Remover um elemento pela posição utilizando pop();
# Alterar o valor de um elemento existente;
# Limpar os elementos utilizando clear().

print(f"{'-'*10} exibir lista inicial e o id {'-'*10}")
print(lista)
print(id(lista))

print(f"{'-'*10} adicionar elemento {'-'*10}")
lista.append(40)
print(lista)
print(id(lista))

print(f"{'-'*10} inserir elemento por index{'-'*10}")
lista.insert(2,50)
print(lista)
print(id(lista))

print(f"{'-'*10} remover elemento por valor{'-'*10}")
# lista.remove(80)
# print(lista)
#teste para ver o que acontece ao tentar remover um valor que não existe no arr

lista.remove(40)
print(lista)
print(id(lista))

print(f"{'-'*10} remover elemento por índice{'-'*10}")
# lista.pop(8)
# print(lista)
# teste para ver o que acontece ao tentar remover um item pela posição que não existe no arr

lista.pop(0)
print(lista)
print(id(lista))


print(f"{'-'*10} alterar elemento por índice{'-'*10}")
lista[2] = 100
print(lista)
print(id(lista))

print(f"{'-'*10} limpar a lista{'-'*10}")
lista.clear()
print(lista)
print(id(lista))

# Análise dos resultados
#A) Não, pois a lista ela ocupa um espaço inicial na memória
#B) O ponteiro do objeto adicionado é inserido ao final do arr 
# (primeira posição livre). Já por index, há o deslocamento dos 
# ponteiros que estão à direta da inserção, deixando uma vaga "liberada"
#C) O ponteiro ele é desvinculado do array e os elementos que 
# estavam à direita dela, são deslocados para a esquerda
# D) Ele mudou, pois números inteiros são imutáveis.
#  Ao invés dele apontar para o ponteiro que estava naquela posição,
#  ele passa a apontar para o outro 
# E) Os elementos que estão dentro dela, 
# a quantidade e item e os ponteiros que ela armazena, 
# eles podem ser mudados dinamicamente, 
# mas o endereço da memória do objeto princiap (lista) não muda.
# F) Alterar o conteúdo faz com que a lista mude internamente, 
# ou seja, se outra variável tiver apontando para aquele mesmo objeto, 
# ele também sofre essa mudança. Ao criar uma nova lista, 
# ela aloca o conteúdo em outro bloco e memória