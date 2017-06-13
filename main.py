valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15";
#valor_entrada = "1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16";



def printTabuleiro(Tab):
		for i in range (0,4):
			print(Tab[i+(4*0)]," ",Tab[i+(4*1)]," ",Tab[i+(4*2)]," ",Tab[i+(4*3)])

array_entrada = valor_entrada.split(" ")
indice_entrada = 0

Tab = [0 for x in range(16)]
for i in range (0,4):
	for j in range (0,4):
		Tab[j+(4*i)] = array_entrada[i+(4*j)]

printTabuleiro(Tab)

#solução, usar matriz, converter cada array dentro da matris em tupla, converter cada tupla em hash (array de hash, converter em tupla e em hash novamente)
#ou continuar usando array, converter em tupla, e em hash posteriormente
asd =  [[0 for x in range(4)] for y in range(4)] 
j1 = tuple(asd)
print(j1)
print(hash(j1))




if "0"  in valor_entrada: 
    espaco_vazio = "0"
else:
    espaco_vazio = "16"


class Tabuleiro2:

	Tabuleiro =  [[0 for x in range(4)] for y in range(4)] 

	def inicializaTabuleiro(self,entrada):
		array_entrada = entrada.split(" ")
		indice_entrada = 0
		for i in range (0,4):
			for j in range (0,4):
				self.Tabuleiro[i][j] = int(array_entrada[indice_entrada])
				indice_entrada=indice_entrada+1				

	def printTabuleiro(self):
		for i in range (0,4):
			print(self.Tabuleiro[i])

	def stringTabuleiroIJ(self,i,j):
		return "Tabuleiro [",i,"][",j,"]: "

	def verificaTabuleiroResolvido(self):
		valor_comparador = 1	
		for i in range (0,4):
			for j in range (0,4):
				if(self.Tabuleiro[j][i] != valor_comparador):
					print(self.stringTabuleiroIJ(j,i)," Esperado: ",valor_comparador," enconrado: ",self.Tabuleiro[j][i])
					return False
				valor_comparador = valor_comparador+1	
		return True

#jogo = Jogo()
#jogo.inicializaTabuleiro(valor_entrada)
#jogo.printTabuleiro()
#jogo.verificaTabuleiroResolvido()

#g(h) = altura da arvore