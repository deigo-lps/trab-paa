import sys
def countingSort(vet):
  output=[0]*len(vet)

  #encontra o maior elemento do vetor
  maior=-1
  for i in vet:
    if i>maior:
      maior=i
  
  #inicializa o vetor contador
  count=[0] * (maior+1)

  #armazena a contagem de cada elemento no vetor contador
  for i in range(0,len(vet)):
    count[vet[i]]+=1

  #armazena a contagem cumulativa
  for i in range(1,maior+1):
    count[i]+=count[i-1]

  #encontra o index de cada elemento do vetor original no vetor contador
  #coloca os elementos no vetor output
  i=len(vet)-1
  while i>=0:
    sys.stdout.write("{}\r".format(i))
    output[count[vet[i]]-1]=vet[i]
    count[vet[i]]-=1
    i-=1

  #retorna elementos ao vetor original
  for i in range(0,len(vet)):
    vet[i]=output[i]
  return vet