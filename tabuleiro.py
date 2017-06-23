

class Tabuleiro:
	def __init__(self):
		self.lista_tabuleiro =  [[0 for x in range(4)] for y in range(4)]  
		self.g = 0
		self.h = 0
		self.pai = 0

	def __lt__(self, other):
		if (self.g < other.g):
			return True
		return False

	def setPai(self,pai):
		self.g = pai.g+1
		self.pai = pai

	def calculaH1(self,j,i,valor_comparador):
		if(self.lista_tabuleiro[j][i] != valor_comparador):
			self.h = self.h+1

	def calculaH2(self,j,i,valor_anterior):
		if(self.lista_tabuleiro[j][i] != (valor_anterior+1)):
			self.h = self.h+1	

	def positivo(self,valor):
		if(valor < 0):
			return valor*-1
		return valor	

	def calculaH3(self,j,i,valor_comparador):
		if(self.lista_tabuleiro[j][i] != valor_comparador):
			posicao_esperada = self.lista_tabuleiro[j][i]-1
			alvo_j = posicao_esperada%4
			alvo_i = posicao_esperada//4
			errumar
			self.h = self.h + self.positivo((alvo_j - j) + (alvo_i - i))	


	#aqui será: verificado se tabuleiro resolvido, e calculada heuristica
	def verificaTabuleiroResolvido(self):
		heuristica = 3
		valor_comparador = 1
		valor_anterior_h2 = self.lista_tabuleiro[0][0]-1
		tabuleiro_resolvido = True	
		for i in range (0,4):
			for j in range (0,4):
				if(self.lista_tabuleiro[j][i] != valor_comparador):
					tabuleiro_resolvido = False	
				if(heuristica==1):
					self.calculaH1(j,i,valor_comparador)
				elif(heuristica==2):
					self.calculaH2(j,i,valor_anterior_h2)
					valor_anterior_h2 = self.lista_tabuleiro[j][i]
				elif(heuristica==3):
					self.calculaH3(j,i,valor_comparador)
					a=0
				elif(heuristica==4):
					a=0
				elif(heuristica==5):
					a=0
				valor_comparador = valor_comparador+1	
		#if(tabuleiro_resolvido==True):
			#self.printTabuleiro()
		#print(self.h)
		#self.printTabuleiro()
		return tabuleiro_resolvido

	def stringTabuleiroIJ(i,j):
		return "Tabuleiro [",i,"][",j,"]: "

	def inicializaTabuleiro(self,entrada):
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