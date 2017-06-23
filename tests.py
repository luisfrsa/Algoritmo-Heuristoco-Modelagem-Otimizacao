def calculaH3(valor,j,i,valor_comparador):
	h=0
	if(valor != valor_comparador):
		posicao_esperada = valor-1
		alvo_j = posicao_esperada%4
		alvo_i = posicao_esperada//4
		h =  positivo((alvo_j - j) + (alvo_i - i))
		print("Valor: ",valor, "posicao[]= ",j,",",i,"Ind comparador",valor_comparador," COM H ",h)

def positivo(valor):
	if(valor < 0):
		return valor*-1
	return valor	
			
for i in range (1,17):
	g = i+1
	calculaH3(i,0,0,g)
