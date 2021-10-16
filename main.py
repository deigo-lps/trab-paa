# Realize testes com entradas pequenas, e aumente gradativamente até um tamanho
# considerável.
# Realize testes com a entrada ordenada de forma crescente, desordenada e
# ordenada de forma decrescente.

from bucket import bucketSort
from counting import countingSort
from insertion import insertionSort
from merge import mergeSort
from quick import quickSort
from shell import shellSort


from random import seed
from random import random
import time
import sys
import os
sys.setrecursionlimit(10**6)
seed(1)
arquivo=open('testes_paa','w')


#---------------Funções Geradoras----------------#
def gerarDesordenado(vet,size):
  for i in range(0,size):
    vet.append(int(random()*1000000+1))

def gerarOrdenado(vet,size):
  for i in range(0,size):
    vet.append(i)

def gerarOrdenadoContrario(vet,size):
  for i in range(size,0,-1):
    vet.append(i)
#-----------------Funções Teste-------------------#
def testeQuick(funcao,q1,q2,q3):
  vet=[]
  funcao(vet,q1)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()
  arquivo.write(str(q1)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q1)+" entradas: "+str(round(end - start,7))+'\n')
  t1=round(end - start,7)

  vet=[]
  funcao(vet,q2)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()
  arquivo.write(str(q2)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q2)+" entradas: "+str(round(end - start,7))+'\n')
  t2=round(end - start,7)

  vet=[]
  funcao(vet,q3)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()
  arquivo.write(str(q3)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q3)+" entradas: "+str(round(end - start,7))+'\n')
  t3=round(end - start,7)
  return round((t1+t2+t3)/3,7)

def testeGeral(funcao,ordenador,q1,q2,q3):
  vet=[]
  funcao(vet,q1)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write(str(q1)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q1)+" entradas: "+str(round(end - start,7))+'\n')
  t1=round(end - start,7)

  vet=[]
  funcao(vet,q2)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write(str(q2)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q2)+" entradas: "+str(round(end - start,7))+'\n')
  t2=round(end - start,7)

  vet=[]
  funcao(vet,q3)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write(str(q3)+" entradas: "+str(round(end - start,7))+'\n')
  print(str(q3)+" entradas: "+str(round(end - start,7))+'\n')
  t3=round(end - start,7)
  return round((t1+t2+t3)/3,7)
  

#----------------TESTES-------------------#
arquivo.write('QuickSort\n')
arquivo.write('Desordenado\n')
quickDesordenado=testeQuick(gerarDesordenado,1000,5000,10000)

arquivo.write('Ordenado\n')
quickOrdenado=testeQuick(gerarOrdenado,1000,5000,10000)

arquivo.write('Ordenado ao contrario\n')
quickInverso=testeQuick(gerarOrdenadoContrario,1000,5000,10000)

arquivo.write('\nBucketSort\n')
arquivo.write('Desordenado\n')
bucketDesordenado=testeGeral(gerarDesordenado,bucketSort,1000,5000,10000)
arquivo.write('Ordenado\n')
bucketOrdenado=testeGeral(gerarOrdenado,bucketSort,1000,5000,10000)
arquivo.write('Ordenado ao contrario\n')
bucketInverso=testeGeral(gerarOrdenadoContrario,bucketSort,1000,5000,10000)

arquivo.write('\nCountingSort\n')
arquivo.write('Desordenado\n')
countingDesordenado=testeGeral(gerarDesordenado,countingSort,1000,5000,10000)
arquivo.write('Ordenado\n')
countingOrdenado=testeGeral(gerarOrdenado,countingSort,1000,5000,10000)
arquivo.write('Ordenado ao contrario\n')
countingInverso=testeGeral(gerarOrdenadoContrario,countingSort,1000,5000,10000)

arquivo.write('\nInsertionSort\n')
arquivo.write('Desordenado\n')
insertionDesordenado=testeGeral(gerarDesordenado,insertionSort,1000,5000,10000)
arquivo.write('Ordenado\n')
insertionOrdenado=testeGeral(gerarOrdenado,insertionSort,1000,5000,10000)
arquivo.write('Ordenado ao contrario\n')
insertionInverso=testeGeral(gerarOrdenadoContrario,insertionSort,1000,5000,10000)

arquivo.write('\nMergeSort\n')
arquivo.write('Desordenado\n')
mergeDesordenado=testeGeral(gerarDesordenado,mergeSort,1000,5000,10000)
arquivo.write('Ordenado\n')
mergeOrdenado=testeGeral(gerarOrdenado,mergeSort,1000,5000,10000)
arquivo.write('Ordenado ao contrario\n')
mergeInverso=testeGeral(gerarOrdenadoContrario,mergeSort,1000,5000,10000)

arquivo.write('\nShellSort\n')
arquivo.write('Desordenado\n')
shellDesordenado=testeGeral(gerarDesordenado,shellSort,1000,5000,10000)
arquivo.write('Ordenado\n')
shellOrdenado=testeGeral(gerarOrdenado,shellSort,1000,5000,10000)
arquivo.write('Ordenado ao contrario\n')
shellInverso=testeGeral(gerarOrdenadoContrario,shellSort,1000,5000,10000)

arquivo.write('\nMEDIAS\n')
arquivo.write('QuickSort Desordenado: {}\n'.format(quickDesordenado))
arquivo.write('QuickSort Ordenado: {}\n'.format(quickOrdenado))
arquivo.write('QuickSort Inverso: {}\n\n'.format(quickInverso))

arquivo.write('BucketSort Desordenado: {}\n'.format(bucketDesordenado))
arquivo.write('BucketSort Ordenado: {}\n'.format(bucketOrdenado))
arquivo.write('BucketSort Inverso: {}\n\n'.format(bucketInverso))

arquivo.write('CountingSort Desordenado: {}\n'.format(countingDesordenado))
arquivo.write('CountingSort Ordenado: {}\n'.format(countingOrdenado))
arquivo.write('CountingSort Inverso: {}\n\n'.format(countingInverso))

arquivo.write('InsertionSort Desordenado: {}\n'.format(insertionDesordenado))
arquivo.write('InsertionSort Ordenado: {}\n'.format(insertionOrdenado))
arquivo.write('InsertionSort Inverso: {}\n\n'.format(insertionInverso))

arquivo.write('MergeSort Desordenado: {}\n'.format(mergeDesordenado))
arquivo.write('MergeSort Ordenado: {}\n'.format(mergeOrdenado))
arquivo.write('MergeSort Inverso: {}\n\n'.format(mergeInverso))

arquivo.write('ShellSort Desordenado: {}\n'.format(shellDesordenado))
arquivo.write('ShellSort Ordenado: {}\n'.format(shellOrdenado))
arquivo.write('ShellSort Inverso: {}\n\n'.format(shellInverso))


