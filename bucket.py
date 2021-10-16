import sys
def bucketSort(vet):
  bucket=[]
  #cria os baldes
  for i in range(len(vet)):
    bucket.append([])

  #insere elementos em seus baldes
  for i in vet:
    indice=i%10
    bucket[indice].append(i)

  #ordena cada balde
  for i in range(len(vet)):
    sys.stdout.write("{}\r".format(i))
    bucket[i]=sorted(bucket[i])

  #retorna elementos ao vetor
  k=0
  for i in range(len(vet)):
    for j in range(len(bucket[i])):
      vet[k]=bucket[i][j]
      k+=1
  return vet
