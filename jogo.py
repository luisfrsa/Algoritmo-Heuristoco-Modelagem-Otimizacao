import bisect 
from tabuleiro import Tabuleiro
import time
import sys
import random

def db(s):
	if(random.randint(0,10)==1):
		for x in s:
			x[1].printTabuleiro()	
		sys.exit(0)
class Jogo:

	def __init__(self):
		self.hash_tabuleiros_visitados = set()
		#self.hash_tabuleiros_visitados = []
		self.tabuleiros_abertos = []
	
	def inicia_resolucao(self,Tabuleiro):
		if(not Tabuleiro.verificaTabuleiroResolvido()):
			self.converte_tabuleiro_hash(Tabuleiro)
			return self.resolve_jogo()
		else:
			return Tabuleiro

	def resolve_jogo(self):
		
		while(len(self.tabuleiros_abertos) > 0):
			Tabuleiro = self.tabuleiros_abertos.pop(0)
			tentativa_resolucao = self.gera_opcoes_movimentos(Tabuleiro[1])
			if(tentativa_resolucao!=False):
				print("Jogo Resolvido!!!")
				return tentativa_resolucao
		print("Impossivel resolver jogo")
		return False

	def verifica_sequencia_repetida(self,Tabuleiro,valor_hash):
		if(valor_hash in self.hash_tabuleiros_visitados):
			return False
		self.hash_tabuleiros_visitados.add(valor_hash)
		bisect.insort(self.tabuleiros_abertos, [(Tabuleiro.g+Tabuleiro.h),Tabuleiro]) 
	
	def verifica_sequencia_repetida2(self,Tabuleiro,valor_hash):		
		if(self.binary_search(self.hash_tabuleiros_visitados,valor_hash)!=False):		
			return False
	
		bisect.insort(self.hash_tabuleiros_visitados, valor_hash) 
		bisect.insort(self.tabuleiros_abertos, [(Tabuleiro.g+Tabuleiro.h),Tabuleiro]) 
	
	def binary_search(self,alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
		
	def converte_tabuleiro_hash_str(self,Tabuleiro):		
		tabuleiro_temp = []
		strTab = ''
		for i in range (0,4):
			for j in range (0,4):
				strTab=strTab+str(Tabuleiro.lista_tabuleiro[j][i])+" "
		self.verifica_sequencia_repetida(Tabuleiro,hash(strTab))

	def converte_tabuleiro_hash(self,Tabuleiro):		
		tabuleiro_temp = []
		for i in range (0,4):
			tabuleiro_temp.append(hash(tuple(Tabuleiro.lista_tabuleiro[i])))
		self.verifica_sequencia_repetida(Tabuleiro,hash(tuple(tabuleiro_temp)))

	def busca_dezesseis(self,Tabuleiro):
		for i in range (0,4):
			for j in range (0,4):
				if(Tabuleiro.lista_tabuleiro[i][j]==16):
					#i = 3, j = 0
					return [i,j]


	def gera_opcoes_movimentos(self,Tabuleiro):
		#print(Tabuleiro.lista_tabuleiro)

		ij = self.busca_dezesseis(Tabuleiro)

		i = ij[0]
		j = ij[1]		

		if(i+1 <=3):
			retorno = self.move_peca(Tabuleiro,i,j,(i+1),j)
			if(retorno!=False):
				return retorno
		if(j+1 <=3):		
			retorno = self.move_peca(Tabuleiro,i,j,i,(j+1))
			if(retorno!=False):
				return retorno
		if(i-1 >=0):
			retorno = self.move_peca(Tabuleiro,i,j,(i-1),j)
			if(retorno!=False):
				return retorno
		if(j-1 >=0):
			retorno = self.move_peca(Tabuleiro,i,j,i,(j-1))
			if(retorno!=False):
				return retorno
		return False


	def move_peca(self,tab_pai,i16, j16, iAlvo, jAlvo):
		tab_copy  = [row[:] for row in tab_pai.lista_tabuleiro]

		tab_copy[i16][j16] = tab_copy[iAlvo][jAlvo]
		tab_copy[iAlvo][jAlvo] = 16

		Tabuleiro_novo = Tabuleiro()
		Tabuleiro_novo.setPai(tab_pai)
		Tabuleiro_novo.lista_tabuleiro = tab_copy
		#Tabuleiro_novo.printTabuleiro()
		#time.sleep(1)
		if(Tabuleiro_novo.verificaTabuleiroResolvido()):
			return Tabuleiro_novo
		else:
			self.converte_tabuleiro_hash(Tabuleiro_novo)
			return False

	def print_resultado2(self,Tabuleiro):
		num_result = 0
		pai = Tabuleiro.pai
		while(pai != 0):
			Tabuleiro = pai
			pai = Tabuleiro.pai
			num_result+=1

			
		print("Jogo resolvido em ",num_result," passos")	

	def print_resultado(self,Tabuleiro):
		lista_resultado = []
		lista_resultado.append(Tabuleiro)
		pai = Tabuleiro.pai
		while(pai != 0):
			Tabuleiro = pai
			lista_resultado.append(Tabuleiro)
			pai = Tabuleiro.pai

		for t in lista_resultado[::-1]:
			t.printTabuleiro()	
		print("Jogo resolvido em ",(len(lista_resultado)-1)," passos")

