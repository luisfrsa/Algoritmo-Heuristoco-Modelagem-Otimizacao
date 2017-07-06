#import bisect 
from bisect import insort
from time import time
from math import floor
#import math


class Tabuleiro:

	
	def __init__(self):
		global id_tabuleiro
		self.lista_tabuleiro =  [[0 for x in range(4)] for y in range(4)]  
		self.g = 0
		self.h = 0
		self.pai = 0
		self.id = id_tabuleiro
		id_tabuleiro = id_tabuleiro + 1

	def __lt__(self, other):
		#if (self.g < other.g):
		if (self.g < other.g):
			return True
		return False


	def positivo(self,valor):
		if(valor < 0):
			return valor*-1
		return valor

	def calculaH1(self):
		valor_comparador = 1
		valor_h = 0
		for i in range (0,4):
			for j in range (0,4):
				if(self.lista_tabuleiro[j][i] != valor_comparador):
					valor_h = valor_h + 1
				valor_comparador = valor_comparador + 1
		return valor_h

	def calculaH2(self):
		valor_anterior = self.lista_tabuleiro[0][0]-1
		valor_h = 0
		for i in range(0,4):
			for j in range(0,4):
				if(self.lista_tabuleiro[j][i] != (valor_anterior+1)):
					valor_h = valor_h+1
					valor_anterior = self.lista_tabuleiro[j][i]
		return valor_h

	def calculaH33(self):
		global global_tabuleiro_resolvido
		valor_h = 0
		for i in range (0,4):
			for j in range (0,4):
				valor = self.lista_tabuleiro[i][j];
				if (valor != global_tabuleiro_resolvido[i][j] and valor != 16 ):
					valor_h = valor_h + abs(i - int(abs((4 * (valor / 4 - floor(valor / 4)) - 1)))) + abs(j - int((valor / 4.1)))
		return valor_h
	


	def calculaH3(self):
		valor_comparador = 1
		valor_h = 0
		aux1 = 3
		aux2 = 2 #((4*aux1)/(4*aux2)) +
		for i in range (0,4):
			for j in range (0,4):
				if(self.lista_tabuleiro[j][i] != valor_comparador and self.lista_tabuleiro[j][i]!= 16 ):
					valor_alvo = self.lista_tabuleiro[j][i]-1			
					#alvo_j = (valor_alvo%4)
					#alvo_i = (valor_alvo//4)
					#if(alvo_j > j):
					#	alvo_j =alvo_j + (4*aux1)/(4*aux2)
					#else:
					#	j = j + (4*aux1)/(4*aux2)
					valor_h = valor_h + abs((valor_alvo%4) - j) +  abs((valor_alvo//4) - i)
						#self.printTabuleiro()
						#print("Entra no IF")
						#print(" posicao_esperada ", valor_comparador)
						#print(" encontrado ", valor_alvo+1)
						#print(" JI atual ", j,",",i)
						#print(" JI esperado ", alvo_j,",",alvo_i)
						#print(" Distancia h' ", abs(alvo_j - j) + abs(alvo_i - i)	)
				valor_comparador = valor_comparador+1
		#if(valor_h > 22):
		#	print("-----")
		#	self.printTabuleiro()
		#	print(valor_h)
		#	print("-----")

		#print("----------")		
		#self.printTabuleiro()
		#print("Id->",self.id)
		#if(self.pai):
		#	print("Id PAI->",self.pai.id)
		#print("G->",self.g)
		#print("H->",valor_h)
		return valor_h

	def calculaH4(self,multH1,multH2,multH3):
		valor_comparador = 1 #para h1 e h3
		valor_anterior = self.lista_tabuleiro[0][0]-1 #para h2
		valor_h1 = 0
		valor_h2 = 0
		valor_h3 = 0
		for i in range (0,4):
			for j in range (0,4):	
				if(self.lista_tabuleiro[j][i] != valor_comparador):
					valor_h1 = valor_h1 + 1
				if(self.lista_tabuleiro[j][i] != (valor_anterior+1)):
					valor_h2 = valor_h2 + 1
					valor_anterior = self.lista_tabuleiro[j][i]
				if(self.lista_tabuleiro[j][i] != valor_comparador and self.lista_tabuleiro[j][i]!= 16):
					valor_alvo = self.lista_tabuleiro[j][i]-1			
					alvo_j = valor_alvo%4
					alvo_i = valor_alvo//4
					valor_h3 = valor_h3 + self.positivo(alvo_j - j) + self.positivo(alvo_i - i)					
				valor_comparador = valor_comparador + 1
		return multH1 * valor_h1 +multH2 * valor_h2+multH3 * valor_h3 

	def calculaH5(self):
		valor_comparador = 1 #para h1 e h3
		valor_anterior = self.lista_tabuleiro[0][0]-1 #para h2
		valor_h1 = 0
		valor_h2 = 0
		valor_h3 = 0
		for i in range (0,4):
			for j in range (0,4):	
				if(self.lista_tabuleiro[j][i] != valor_comparador):
					valor_h1 = valor_h1 + 1
				if(self.lista_tabuleiro[j][i] != (valor_anterior+1)):
					valor_h2 = valor_h2 + 1
					valor_anterior = self.lista_tabuleiro[j][i]
				if(self.lista_tabuleiro[j][i] != valor_comparador and self.lista_tabuleiro[j][i]!= 16):
					valor_alvo = self.lista_tabuleiro[j][i]-1			
					alvo_j = valor_alvo%4
					alvo_i = valor_alvo//4
					valor_h3 = valor_h3 + self.positivo(alvo_j - j) + self.positivo(alvo_i - i)					
				valor_comparador = valor_comparador + 1
		return max(valor_h1 , valor_h2, valor_h3)



	def calculaHeuristicas(self):
		global heuristica
		valor_comparador = 1
		if(heuristica==1):
			self.h = self.calculaH1()
		elif(heuristica==2):
			self.h = self.calculaH2()
		elif(heuristica==3):
			self.h = self.calculaH3()
		elif(heuristica==4):
			multH1 = 0.3
			multH2 = 0.1
			multH3 = 0.6
			self.h = self.calculaH4(multH1,multH2,multH3)
		elif(heuristica==5):
			self.h = self.calculaH5()

	def verificaTabuleiroResolvido(self,valor_hash):
		valor_comparador = 1
		global global_hash_tabuleiro_resolvido
		if(valor_hash == global_hash_tabuleiro_resolvido):
			tabuleiro_resolvido = False	
			for i in range (0,4):
				for j in range (0,4):
					if(self.lista_tabuleiro[j][i] != valor_comparador):
						return False
					valor_comparador = valor_comparador+1			
			return True
		return False

	def calculaHash(self):
		self.valor_hash = hash((hash(tuple(self.lista_tabuleiro[0])),
					  hash(tuple(self.lista_tabuleiro[1])),
					  hash(tuple(self.lista_tabuleiro[2])),
					  hash(tuple(self.lista_tabuleiro[3]))))
		return self.valor_hash

	def stringTabuleiroIJ(i,j):
		return "Tabuleiro [",i,"][",j,"]: "

	def inicializaTabuleiro(self,entrada):
		while ("  " in entrada):
			entrada = entrada.replace("  "," ")
		array_entrada = entrada.split(" ")
		indice_entrada = 0
		for i in range (0,4):
			for j in range (0,4):
				valor_inteiro = int(array_entrada[i+(4*j)])
				if(valor_inteiro==0):
					valor_inteiro = 16
				self.lista_tabuleiro[j][i] = valor_inteiro
				indice_entrada=indice_entrada+1	


	def printTabuleiro(self):
		str_result = ""
		str_result = str_result + ("\n .::Print Tabuleiro::.")
		for i in range (0,4):
			temp_tab = self.lista_tabuleiro[i][:]
			words = ["X" if x==16 else x for x in temp_tab]
			str_result = str_result + "\n" + str(words)
		str_result = str_result + "\n" 
		return str_result

	def setPai(self,pai):
		self.g = pai.g+1
		self.pai = pai


class Jogo:

	def __init__(self):
		self.hash_tabuleiros_fechados = set()
		self.hash_tabuleiros_abertos = set()
		self.tabuleiros_abertos = []
		#--
		#self.hash_tabuleiros_fechados = set()
		#self.tabuleiros_abertos = set()
	
	def inicia_resolucao(self,tabuleiro):
		valor_hash = tabuleiro.calculaHash()
		if(not tabuleiro.verificaTabuleiroResolvido(valor_hash)):
			tabuleiro.calculaHeuristicas()
			self.hash_tabuleiros_abertos.add(valor_hash)
			insort(self.tabuleiros_abertos, [(tabuleiro.g+tabuleiro.h),tabuleiro]) 
			return self.resolve_jogo()
		else:
			return tabuleiro

	def resolve_jogo(self):		
		while(len(self.tabuleiros_abertos) > 0):
			tabuleiro = self.tabuleiros_abertos.pop(0)
			#self.hash_tabuleiros_abertos.remove(tabuleiro[1].valor_hash)
			self.hash_tabuleiros_fechados.add(tabuleiro[1].valor_hash)
			tentativa_resolucao = self.gera_opcoes_movimentos(tabuleiro[1])
			if(tentativa_resolucao!=False):
				return tentativa_resolucao
		return False


	def busca_dezesseis(self,tabuleiro):
		for j in range (0,4):
			for i in range (0,4):
				if(tabuleiro.lista_tabuleiro[i][j]==16):
					return [i,j]


	def gera_opcoes_movimentos(self,tabuleiro):

		ij = self.busca_dezesseis(tabuleiro)

		i = ij[0]
		j = ij[1]		

		if(i<=2):
			retorno = self.move_peca(tabuleiro,i,j,(i+1),j)
			if(retorno!=False):
				return retorno
		if(j<=2):		
			retorno = self.move_peca(tabuleiro,i,j,i,(j+1))
			if(retorno!=False):
				return retorno
		if(i>=1):
			retorno = self.move_peca(tabuleiro,i,j,(i-1),j)
			if(retorno!=False):
				return retorno
		if(j>=1):
			retorno = self.move_peca(tabuleiro,i,j,i,(j-1))
			if(retorno!=False):
				return retorno
		return False


	def move_peca(self,tab_pai,i16, j16, iAlvo, jAlvo):
		#tab_copy  = [row[:] for row in tab_pai.lista_tabuleiro]
		tab_copy  = [tab_pai.lista_tabuleiro[0][:],tab_pai.lista_tabuleiro[1][:],tab_pai.lista_tabuleiro[2][:],tab_pai.lista_tabuleiro[3][:]]
		#tab_copy[i16][j16] = tab_copy[iAlvo][jAlvo]
		#tab_copy[iAlvo][jAlvo] = 16
		tab_copy[i16][j16],tab_copy[iAlvo][jAlvo] = tab_copy[iAlvo][jAlvo],16
		#a, b = b, a

		tabuleiro_novo = Tabuleiro()
		tabuleiro_novo.setPai(tab_pai)
		tabuleiro_novo.lista_tabuleiro = tab_copy
		valor_hash = tabuleiro_novo.calculaHash()
		if(tabuleiro_novo.verificaTabuleiroResolvido(valor_hash)):
			return tabuleiro_novo
		else:
			if(tab_pai.pai != 0):
				if (valor_hash == tab_pai.pai.valor_hash):
					#print("false")
					return False

			tabuleiro_novo.calculaHeuristicas()

			if(valor_hash in self.hash_tabuleiros_fechados):
				#print("b")
				"b"
			elif(valor_hash in self.hash_tabuleiros_abertos):
				"a"
				#valorGH = (tabuleiro_novo.g+tabuleiro_novo.h)
				#for b in self.tabuleiros_abertos:
				#	if(b[1].valor_hash==valor_hash and valorGH < b[0]):
				#		print("B: ",b[0]," New: ",valorGH)
			else:
				self.hash_tabuleiros_abertos.add(valor_hash)
				insort(self.tabuleiros_abertos, [(tabuleiro_novo.g+tabuleiro_novo.h),tabuleiro_novo]) 
				#self.hash_tabuleiros_fechados.add(valor_hash)
				#print("---")
				#for i in self.tabuleiros_abertos:
				#	print(i[0]," - ",i[1].g," - ",i[1].h)
				#print("---")
			return False

	def print_run_codes(self,Tabuleiro):
		num_result = 0
		pai = Tabuleiro.pai
		while(pai != 0):
			Tabuleiro = pai
			pai = Tabuleiro.pai
			num_result+=1
		return ("\n Resolvido em: "+str(num_result)+" movimentos")

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



global_hash_tabuleiro_resolvido = hash((hash((1, 5, 9, 13)),hash((2, 6, 10, 14 )),hash((3, 7, 11, 15 )),hash((4, 8, 12, 16))))
global_tabuleiro_resolvido = [[1, 5, 9, 13],[2, 6, 10, 14 ],[3, 7, 11, 15],[4, 8, 12, 16]]
id_tabuleiro = 0
heuristica = 3
run_codes = False


if(not(run_codes)):
		valor_entrada = "6 5 13 0 1 7 9 14 2 8 10 15 3 4 11 12"; # 15 passos
		valor_entrada = "1 5 9 13 2 6 10 14 3 7 16 12 4 8 15 11"; # 6 passos
		valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15"; # 9 passos
		valor_entrada = "9 13 12 8 0 5 7 14 1 11 15 4 6 10 2 3";# 47 passos
		valor_entrada = "2 1 10 9 3 5 11 13 4 0 6 12 7 8 15 14";# 21 passos
		valor_entrada = "1 5 7 0 4 6 12 10 8 2 15 9 3 14 11 13";# 39  passos - 5
		valor_entrada = "2 1 5 0 7 9 10 13 6 4 3 15 8 11 12 14";# 25 passos
		#---------------------------------------------#
		valor_entrada_relatorio = []
		##valor_entrada_relatorio.insert(0,"1#5 13 6 10 1 7 2 9 4 3 15 14 8 0 11 12") #caso 1 - 20->0.003
		##valor_entrada_relatorio.insert(1,"2#2 10 11 9 3 1 0 13 4 6 7 14 5 8 12 15") #caso 2 - 27->0.2
		##valor_entrada_relatorio.insert(2,"3#5 9 13 10 2 6 14 15 1 4 7 12 0 3 11 8") #caso 3 - 27->0.2
		#valor_entrada_relatorio.insert(3,"4#7 11 4 5 0 6 15 8 14 1 3 13 9 12 10 2") #caso 4 - ?
		##valor_entrada_relatorio.insert(4,"5#5 10 9 14 7 3 13 6 1 15 0 12 8 2 4 11") #caso 5 - 34->1.9
		#valor_entrada_relatorio.insert(5,"6#0 9 3 7 1 14 6 4 2 11 12 15 13 8 10 5") #caso 6
		##valor_entrada_relatorio.insert(6,"7#3 9 0 7 2 1 6 5 11 13 4 12 8 14 15 10") #caso 7
		##valor_entrada_relatorio.insert(7,"8#9 6 7 4 2 1 5 12 8 3 11 0 14 15 10 13") #caso 8
		valor_entrada_relatorio.insert(8,"9#2 9 4 5 0 7 11 12 14 6 3 13 1 8 15 10") #caso 9
		##valor_entrada_relatorio.insert(9,"10#7 11 5 12 9 8 6 13 2 3 4 10 14 1 15 0") #caso 10




else:
	valor_entrada = input().strip()


def main(entrada):
	str_result = ""
	jogo = Jogo()

	tabuleiro = Tabuleiro()
	tabuleiro.inicializaTabuleiro(entrada)
	str_result = str_result + tabuleiro.printTabuleiro()
	resultado = jogo.inicia_resolucao(tabuleiro)

	if(resultado!=False):
		#jogo.print_resultado(resultado)
		str_result = str_result + jogo.print_run_codes(resultado)
		if(not(run_codes)):
			conta = 0
			str_result = str_result + ("\nFechados "+str(len(jogo.hash_tabuleiros_fechados)))
			#print(conta)
			str_result = str_result + ("\nAbertos "+str(len(jogo.tabuleiros_abertos)))
		return str_result

if(not(run_codes)):
	
	for e in valor_entrada_relatorio:
		entrada = e.split("#")
		f = open('resultado_'+str(heuristica)+'_'+str(entrada[0])+'.txt','a+')
		str_result = ""
		str_result = str_result + ("\n /*------------------------------*/")
		str_result = str_result + "\n Iniciando jogo: "+entrada[0]+" -> "+entrada[1]
		time_init = time()
		str_result = str_result + main(entrada[1])
		time_fim = time() - time_init
		str_result = str_result +("\n Tempo de execucao do script do jogo"+str(entrada[0])+": "+str(time_fim))
		str_result = str_result +("\n /*------------------------------*/\n\n")
		f.write(str_result)
		f.close()
else:
	main()

