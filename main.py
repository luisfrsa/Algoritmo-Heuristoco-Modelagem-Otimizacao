
import time
import random


time_init = time.time() # calculando quanto tempo demora para executar sciprt

valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15";
valor_entrada_ordenada = "1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16";

if " 0"  in valor_entrada:
	valor_entrada = valor_entrada.replace(" 0", " 16")
if "0 "  in valor_entrada:
	valor_entrada = valor_entrada.replace("0 ", "16 ")
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
	print(".::Print Tabuleiro::.")
	for i in range (0,4):
		print(tabuleiro[i])
	print(" ")

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
		self.hash_tabuleiro = set()
		self.tabuleiros_abertos = []
		
	def verifica_sequencia_repetida(self,tabuleiro,valor_hash):
		if(valor_hash in self.hash_tabuleiro):
			return False
		self.hash_tabuleiro.add(valor_hash)
		self.tabuleiros_abertos.append(tabuleiro)

	def converte_tabuleiro_hash(self,tabuleiro):
		tabuleiro_temp = []
		for i in range (0,4):
			tabuleiro_temp.append(hash(tuple(tabuleiro[i])))
		self.verifica_sequencia_repetida(tabuleiro,hash(tuple(tabuleiro_temp)))

	def busca_dezesseis(self,tabuleiro):
		for i in range (0,4):
			for j in range (0,4):
				if(tabuleiro[i][j]==16):
					#i = 3, j = 0
					return [i,j]


	def gera_opcoes_movimentos(self,tabuleiro):
		ij = self.busca_dezesseis(tabuleiro)

		i = ij[0]
		j = ij[1]

		if(i+1 <=3):
			self.move_peca(tabuleiro,i,j,(i+1),j)
		if(j+1 <=3):
			self.move_peca(tabuleiro,i,j,i,(j+1))
		if(i-1 >=0):
			self.move_peca(tabuleiro,i,j,(i-1),j)
		if(j-1 >=0):
			self.move_peca(tabuleiro,i,j,i,(j-1))

	def move_peca(self,tabuleiro,i16, j16, iAlvo, jAlvo):
		tabuleiro[i16][j16] = tabuleiro[iAlvo][jAlvo]
		tabuleiro[iAlvo][jAlvo] = 16
		self.converte_tabuleiro_hash(tabuleiro)


jogo = Jogo()
jogo_ordenado = Jogo()

tabuleiro = inicializaTabuleiro(valor_entrada)
tabuleiro_ordenado = inicializaTabuleiro(valor_entrada_ordenada)

printTabuleiro(tabuleiro)
#printTabuleiro(tabuleiro_ordenado)

jogo.gera_opcoes_movimentos(tabuleiro)
tabuleiros = jogo.tabuleiros_abertos
for x in tabuleiros:
	printTabuleiro(x)

#jogo.converte_tabuleiro_hash(tabuleiro)
#jogo_ordenado.converte_tabuleiro_hash(tabuleiro_ordenado)


time_fim = time.time() - time_init

print("Tempo de execucao do script: ",time_fim)
#g(h) = altura da arvore