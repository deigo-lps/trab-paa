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
def testeQuick(funcao):
  vet=[]
  funcao(vet,2000)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()

  arquivo.write("2000 entradas: "+str(end - start)+'\n')
  t1=end-start

  vet=[]
  funcao(vet,20000)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()

  arquivo.write("20000 entradas: "+str(end - start)+'\n')
  t2=end-start

  vet=[]
  funcao(vet,200000)

  start = time.time()
  quickSort(vet,0,len(vet)-1)
  end = time.time()

  arquivo.write("200000 entradas: "+str(end - start)+'\n')
  t3=end-start
  return [t1,t2,t3]

def testeGeral(funcao,ordenador):
  vet=[]
  funcao(vet,2000)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write("2000 entradas: "+str(end - start)+'\n')
  t1=end-start

  vet=[]
  funcao(vet,20000)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write("20000 entradas: "+str(end - start)+'\n')
  t2=end-start

  vet=[]
  funcao(vet,200000)

  start = time.time()
  ordenador(vet)
  end = time.time()

  arquivo.write("200000 entradas: "+str(end - start)+'\n')
  t3=end-start
  return [t1,t2,t3]
  

#----------------TESTES-------------------#
arquivo.write('QuickSort\n')
arquivo.write('Desordenado\n')
testeQuick(gerarDesordenado)
arquivo.write('Ordenado\n')
testeQuick(gerarOrdenado)
arquivo.write('Ordenado ao contrario\n')
testeQuick(gerarOrdenadoContrario)

