def insertionSort(vet):
  #percorre o vetor a partir do segundo elemento armazenando ele em aux
  for i in range(1,len(vet)):
    aux=vet[i]
    j=i-1
    #enquanto j for positivo, e o elemento na posição j for maior que aux
    #passa j para traz
    while j>=0 and vet[j]>aux:
      vet[j+1]=vet[j]
      j-=1
    #coloca aux no devido lugar
    vet[j+1]=aux
  return vet