import sys
def partition(vet,E,D):
  #escolhe o ultimo elemento como pivo
  pivo=vet[D]

  #aponta para o maior elemento
  i=E-1

  
  for j in range(E,D):
    #se menor que pivo, troque com i
    if vet[j]<=pivo:
      i=i+1
      #troca i com j
      (vet[i],vet[j])=(vet[j],vet[i])
  #troca pivo com i
  (vet[i+1],vet[D]) = (vet[D],vet[i+1])

  #retorna onde partição está feita
  return i+1

def quickSort(vet,E,D):
  sys.stdout.write("{}\r".format(D))
  if E<D:
    aux = partition(vet,E,D)
    quickSort(vet, E, aux - 1)
    quickSort(vet, aux + 1, D)
  return vet