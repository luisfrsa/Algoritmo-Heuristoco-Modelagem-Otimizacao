import math
import time

time_init = time.time() # calculando quanto tempo demora para executar sciprt

valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15";
valor_entrada_ordenada = "1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16";



#def printTabuleiro(Tab):
#		for i in range (0,4):
#			print(Tab[i+(4*0)]," ",Tab[i+(4*1)]," ",Tab[i+(4*2)]," ",Tab[i+(4*3)])
#
#array_entrada = valor_entrada.split(" ")
#indice_entrada = 0
#
#Tab = [0 for x in range(16)]
#for i in range (0,4):
#	for j in range (0,4):
#		Tab[j+(4*i)] = array_entrada[i+(4*j)]
#
#printTabuleiro(Tab)
#
#solução, usar matriz, converter cada array dentro da matris em tupla, converter cada tupla em hash (array de hash, converter em tupla e em hash novamente)
#ou continuar usando array, converter em tupla, e em hash posteriormente
#asd =  [[0 for x in range(4)] for y in range(4)] 
#j1 = tuple(asd)
#print(j1)
#print(hash(j1))





def inicializaTabuleiro(entrada):
	tabuleiro =  [[0 for x in range(4)] for y in range(4)] 
	
	array_entrada = entrada.split(" ")
	indice_entrada = 0
	for i in range (0,4):
		for j in range (0,4):
			tabuleiro[j][i] = int(array_entrada[i+(4*j)])
			indice_entrada=indice_entrada+1	
	return tabuleiro

def printTabuleiro(tabuleiro):
	for i in range (0,4):
		print(tabuleiro[i])

def stringTabuleiroIJ(i,j):
	return "Tabuleiro [",i,"][",j,"]: "

def verificaTabuleiroResolvido(tabuleiro):
	valor_comparador = 1	
	for i in range (0,4):
		for j in range (0,4):
			if(tabuleiro[j][i] != valor_comparador):
				print(stringTabuleiroIJ(j,i)," Esperado: ",valor_comparador," enconrado: ",tabuleiro[j][i])
				return False
			valor_comparador = valor_comparador+1	
	return True



class Jogo:

	def __init__(self):
		self.hash_tabuleiros = []
	
	def verifica_sequencia_repetida(self,hash_tabuleiro):
		if(self.hash_tabuleiro[hash_tabuleiro]==True)
			return False
		self.hash_tabuleiro[hash_tabuleiro] = True

	def converte_tabuleiro_hash(self,tabuleiro):
		tabuleiro_temp = []
		for i in range (0,4):
			tabuleiro_temp.append(hash(tuple(tabuleiro[i])))
		self.verifica_sequencia_repetida(hash(tuple(tabuleiro_temp)))
		



jogo = Jogo()
jogo_ordenado = Jogo()

tabuleiro = inicializaTabuleiro(valor_entrada)
tabuleiro_ordenado = inicializaTabuleiro(valor_entrada_ordenada)

printTabuleiro(tabuleiro)
printTabuleiro(tabuleiro_ordenado)



jogo.converte_tabuleiro_hash(tabuleiro)
jogo_ordenado.converte_tabuleiro_hash(tabuleiro_ordenado)




time_fim = time.time() - time_init

print("Tempo de execucao do script: ",time_fim)
#g(h) = altura da arvore