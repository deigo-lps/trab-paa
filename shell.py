import sys
def shellSort(vet):
  intervalo=len(vet)//2
  while intervalo > 0:
    for i in range(intervalo,len(vet)):
      sys.stdout.write("{}\r".format(i))
      aux=vet[i]
      j=i
      while j>= intervalo and vet[j - intervalo] > aux:
        vet[j]=vet[j-intervalo]
        j-=intervalo
      vet[j]=aux
    intervalo//=2
  return vet