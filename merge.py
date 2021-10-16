def mergeSort(vet):
  if len(vet) > 1:
    meio=len(vet)//2
    E=vet[:meio]
    D=vet[meio:]

    mergeSort(E)
    mergeSort(D)

    i=j=k=0

    #adiciona o menor elemento dentre os dois vetores
    while i<len(E) and j<len(D):
      if E[i] < D[j]:
        vet[k]=E[i]
        i+=1
      else:
        vet[k]=D[j]
        j+=1
      k+=1

    #adiciona o restante dos elementos que sobrarem de um dos vetores
    while i<len(E):
      vet[k]=E[i]
      i+=1
      k+=1

    while j<len(D):
      vet[k]=D[j]
      j+=1
      k+=1
  return vet