encomendasPorDia = []
dias = 0

print("-"*10,"Sistema de Encomendas", "-"*10)

print(f"Digite o número de dias a serem registrados: ")
dias = int(input())


# for(let i = 0; i < dias; i++){
#     print(f"Quantas encomendas foram feitas no dia {dias[i] + 1}: ")
#     encomenda = int(input);
#     encomendasPorDia.append(encomenda);
# }

for dia in range(dias):
    print(f"Quantas encomendas foram feitas no dia {dia + 1}: ")
    encomenda = int(input())
    encomendasPorDia.append(encomenda)


# for(let i = 0; i < dias; i++){
#     print(f"Quantidade de encomendas do dia {i+1}: {encomendasPorDia[i]}")
# } 

# for dia in range(dias):
#     print(f"Quantidade de encomendas do dia {dia + 1}: {encomendasPorDia[dia]}")

for i,encomenda in enumerate(encomendasPorDia):
    print(f"Quantidade de encomendas do dia {i + 1}: {encomenda}")


print("-"*10,"Estatística","-"*10)
#achar o maior valor, o menor valor e a media

maiorValor = max(encomendasPorDia)
menorValor = min(encomendasPorDia)
valorTotal = sum(encomendasPorDia)
mediaEncomendas = valorTotal/len(encomendasPorDia)

print(f'O maior valor foi: {maiorValor}')
print(f'O menor valor foi: {menorValor}')
print(f'A média dos valores foi: {mediaEncomendas:.2f}')

# como funcionam esses métodos anteriores?
#max e  min fazem uma busca linear de (O(n)), aonde é definido o primeiro elemento como referência e após isso, é feito a comparação com os posteriores, em caso positivo, ele é substituído.
# Já o sum, é feito um laço com acumulador

print("-"*10,"Pesquisa","-"*10)

valorDePesquisa = int(input("Qual quantidade deseja pesquisa"))

if(valorDePesquisa in encomendasPorDia):
    print("Valor encontrado!")
else:
    print("Valor não encontrado!")

#Mostrar a posição aonde ele foi encontrado
if(valorDePesquisa in encomendasPorDia):
    posicao = encomendasPorDia.index(valorDePesquisa)
    print(f"Essa quantidade, {valorDePesquisa}, foi encontrado na posição {posicao}")

#O operador in é um loop linear sequencial que faz a verificação da lista comparando para ver se há o item desejado. Se tiver, retorna True, caso contrário, False.

print("-"*10,"Ordenação","-"*10)

listaCrescente = sorted(encomendasPorDia)
listaDecrescente = sorted(encomendasPorDia, reverse=True)
print(listaCrescente)
print(listaDecrescente)

#O método sorted, retorna uma nova lista
# Ele usa o método de iteração TimSorted