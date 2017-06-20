

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
		
			
	#aqui será: verificado se tabuleiro resolvido, e calculada heuristica
	def verificaTabuleiroResolvido(self):
		heuristica = 1
		valor_comparador = 1
		tabuleiro_resolvido = True	
		for i in range (0,4):
			for j in range (0,4):
				if(self.lista_tabuleiro[j][i] != valor_comparador):
					tabuleiro_resolvido = False	
				if(heuristica==1):
					self.calculaH1(j,i,valor_comparador)
				elif(heuristica==2):
					a=0
				elif(heuristica==3):
					a=0
				elif(heuristica==4):
					a=0
				elif(heuristica==5):
					a=0

				valor_comparador = valor_comparador+1	
		#if(tabuleiro_resolvido==True):
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