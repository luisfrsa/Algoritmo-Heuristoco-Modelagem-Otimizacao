import bisect 
import time
#import random



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

	def calculaH3(self):
		valor_comparador = 1
		valor_h = 0
		for i in range (0,4):
			for j in range (0,4):
				if(self.lista_tabuleiro[j][i] != valor_comparador and self.lista_tabuleiro[j][i]!= 16):
					valor_alvo = self.lista_tabuleiro[j][i]-1			
					alvo_j = valor_alvo%4
					alvo_i = valor_alvo//4
					valor_h = valor_h + self.positivo(alvo_j - j) + self.positivo(alvo_i - i)
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
			multH1 = 0.0
			multH2 = 0.0
			multH3 = 1
			self.h = self.calculaH4(multH1,multH2,multH3)
		elif(heuristica==5):
			self.h = self.calculaH5()

	def verificaTabuleiroResolvido(self,valor_hash):
		valor_comparador = 1
		global hash_tabuleiro_resolvido
		if(valor_hash == hash_tabuleiro_resolvido):
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
		print(".::Print Tabuleiro::.")
		for i in range (0,4):
			temp_tab = self.lista_tabuleiro[i][:]
			words = ["X" if x==16 else x for x in temp_tab]
			print(words)
		print(" ")

	def setPai(self,pai):
		self.g = pai.g+1
		self.pai = pai


class Jogo:

	def __init__(self):
		self.hash_tabuleiros_visitados = set()
		self.tabuleiros_abertos = []
		#--
		#self.hash_tabuleiros_visitados = set()
		#self.tabuleiros_abertos = set()
	
	def inicia_resolucao(self,tabuleiro):
		valor_hash = tabuleiro.calculaHash()
		if(not tabuleiro.verificaTabuleiroResolvido(valor_hash)):
			tabuleiro.calculaHeuristicas()
			self.hash_tabuleiros_visitados.add(valor_hash)
			bisect.insort(self.tabuleiros_abertos, [(tabuleiro.g+tabuleiro.h),tabuleiro]) 
			return self.resolve_jogo()
		else:
			return Tabuleiro

	def resolve_jogo(self):		
		while(len(self.tabuleiros_abertos) > 0):
			Tabuleiro = self.tabuleiros_abertos.pop(0)
			tentativa_resolucao = self.gera_opcoes_movimentos(Tabuleiro[1])
			if(tentativa_resolucao!=False):
				return tentativa_resolucao
		return False


	def busca_dezesseis(self,Tabuleiro):
		for i in range (0,4):
			for j in range (0,4):
				if(Tabuleiro.lista_tabuleiro[i][j]==16):
					return [i,j]


	def gera_opcoes_movimentos(self,Tabuleiro):

		ij = self.busca_dezesseis(Tabuleiro)

		i = ij[0]
		j = ij[1]		

		if(i<=2):
			retorno = self.move_peca(Tabuleiro,i,j,(i+1),j)
			if(retorno!=False):
				return retorno
		if(j<=2):		
			retorno = self.move_peca(Tabuleiro,i,j,i,(j+1))
			if(retorno!=False):
				return retorno
		if(i>=1):
			retorno = self.move_peca(Tabuleiro,i,j,(i-1),j)
			if(retorno!=False):
				return retorno
		if(j>=1):
			retorno = self.move_peca(Tabuleiro,i,j,i,(j-1))
			if(retorno!=False):
				return retorno
		return False


	def move_peca(self,tab_pai,i16, j16, iAlvo, jAlvo):
		tab_copy  = [row[:] for row in tab_pai.lista_tabuleiro]

		tab_copy[i16][j16] = tab_copy[iAlvo][jAlvo]
		tab_copy[iAlvo][jAlvo] = 16

		tabuleiro_novo = Tabuleiro()
		tabuleiro_novo.setPai(tab_pai)
		tabuleiro_novo.lista_tabuleiro = tab_copy
		valor_hash = tabuleiro_novo.calculaHash()
		if(tabuleiro_novo.verificaTabuleiroResolvido(valor_hash)):
			return tabuleiro_novo
		else:
			if(tab_pai.pai != 0):
				if (valor_hash == tab_pai.pai.valor_hash):
					return False
			if(not(valor_hash in self.hash_tabuleiros_visitados)):
				tabuleiro_novo.calculaHeuristicas()
				self.hash_tabuleiros_visitados.add(valor_hash)
				bisect.insort(self.tabuleiros_abertos, [(tabuleiro_novo.g+tabuleiro_novo.h),tabuleiro_novo]) 
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
		print(num_result)

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

id_tabuleiro = 0
heuristica = 3
run_codes = False
if(not(run_codes)):
		valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15"; # 9 passos
		valor_entrada = "6 5 13 0 1 7 9 14 2 8 10 15 3 4 11 12"; # 15 passos
		valor_entrada = "1 5 9 13 2 6 10 14 3 7 16 12 4 8 15 11"; # 6 passos
		valor_entrada = "2 1 5 0 7 9 10 13 6 4 3 15 8 11 12 14";# 25 passos
		valor_entrada = "2 1 10 9 3 5 11 13 4 0 6 12 7 8 15 14";# 21 passos
		valor_entrada = "9 13 12 8 0 5 7 14 1 11 15 4 6 10 2 3";# 47 passos
		valor_entrada = "1 5 7 0 4 6 12 10 8 2 15 9 3 14 11 13";# 39  passos - 5
else:
	valor_entrada = input().strip()

hash_tabuleiro_resolvido = hash((hash((1, 5, 9, 13)),hash((2, 6, 10, 14 )),hash((3, 7, 11, 15 )),hash((4, 8, 12, 16))))

def main():

	jogo = Jogo()

	tabuleiro = Tabuleiro()
	tabuleiro.inicializaTabuleiro(valor_entrada)

	resultado = jogo.inicia_resolucao(tabuleiro)

	if(resultado!=False):
		jogo.print_run_codes(resultado)
		if(not(run_codes)):
			conta = 0
			#for i in jogo.tabuleiros_abertos:
			#	for j in jogo.tabuleiros_abertos:
			#		if (i[1].lista_tabuleiro == j[1].lista_tabuleiro):
			#			conta = conta + 1
			#print(jogo.hash_tabuleiros_visitados)
			#print(conta)
			print("Visitados",len(jogo.hash_tabuleiros_visitados))
			print("Abertos",len(jogo.tabuleiros_abertos))

if(not(run_codes)):
	time_init = time.time()
	main()
	time_fim = time.time() - time_init
	print("Tempo de execucao do script: ",time_fim)
else:
	main()

