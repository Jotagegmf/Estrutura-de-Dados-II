def bubbleSort(arrayOriginal):
    novoArr = arrayOriginal.copy()
    n = len(novoArr)

    comparacoes = 0
    trocas = 0

    for i in range(n-1):
        #não precisa ir até n, já que ao chegar na última posição, não há nada a se comparar
        houve_troca = False
        for j in range(0, n - 1 - i):
            comparacoes+=1
            #compara até o último menos o valor de i, pq o maior já vai para as últimas posições
            
            #caso o valor do elemento for maior, ele vai para a direita
            if novoArr[j] > novoArr[j+1]:
                novoArr[j], novoArr[j+1] = novoArr[j+1], novoArr[j]
                trocas+=1
                houve_troca = True
        if not houve_troca:
            break
    
    print(f"Array ordenado: {novoArr}")
    print(f"comparacoes: {comparacoes}")
    print(f"trocas: {trocas}")
    return novoArr, comparacoes, trocas


def quickSort(lista, metricas=None):
    if metricas is None:
        metricas = {'comparacoes': 0}

    if len(lista)<=1:
        return lista
    #3 - escolher o elemento central
    indice_pivo = len(lista)//2
    pivo = lista[indice_pivo]

    #4 - guardar os elementos do pivô
    menores = []
    iguais = []
    maiores = []

    #5 - adicionar nas caixas
    for elemento in lista:
        metricas["comparacoes"]+=1 # aumenta a comparação feita
        if(elemento < pivo):
            menores.append(elemento)
        elif(elemento > pivo):
            maiores.append(elemento)
        else:
            iguais.append(elemento)

    #6 - retorno com recursividade
    return(
        quickSort(menores, metricas)
        + iguais 
        + quickSort(maiores, metricas)
    )

arrDeTeste = [10,2.34,9,32,456,12,34,3,1,2034,-12]
print(quickSort(arrDeTeste))