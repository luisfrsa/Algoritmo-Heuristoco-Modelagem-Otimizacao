def calculaH3(j,i,tab,valor_comparador,asrt):
	print("Tabuleiro:",tab," comparado com valor",valor_comparador)
	h = 0
	if(tab != valor_comparador):
		posicao_esperada = valor_comparador
		valor_alvo = tab-1			
		alvo_j = valor_alvo%4
		alvo_i = valor_alvo//4
		h = positivo(alvo_j - j) + positivo(alvo_i - i)	
		print("Entra no IF")
		print(" posicao_esperada ", posicao_esperada)
		print(" JI atual ", j,",",i)
		print(" JI esperado ", alvo_j,",",alvo_i)
		print(" Distancia h' ", positivo(alvo_j - j) + positivo(alvo_i - i)	)
		if(asrt == h):
			print("ASSERT TRUE")
		else:
			print("ASSERT FALSE!")

def positivo(valor):
	if(valor < 0):
		return valor*-1
	return valor	
			

#calculaH3(3,2,2,12,4)
#calculaH3(2,3,1,15,5)
#calculaH3(3,3,1,16,6)
#calculaH3(0,1,10,5,2)

for i in range (1,17):
	alvo = i-1
	alvo_j = alvo%4
	alvo_i = alvo//4
	print(i, " em alvo J ",alvo_j," em alvo I ",alvo_i)