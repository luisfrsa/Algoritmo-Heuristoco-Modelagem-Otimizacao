
import time

# A LISTA DOS ABERTOS ESTA COM G+H', MAS VERIFICAR SE JÁ NÃO EXISTE UM G MENOR QUE G+H' QUE TENHA ACABADO DE SER VISITADO
# se remover um estado m' dos fechados, a consequencia é: 
#eliminiar todos os filhos
time_init = time.time() # calculando quanto tempo demora para executar sciprt

from tabuleiro import Tabuleiro
from jogo import Jogo


valor_entrada = "1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16"; # 0 passos
valor_entrada = "1 5 9 13 2 6 10 14 3 7 16 12 4 8 15 11"; # 6 passos

valor_entrada = "16 12 8 4 15 11 7 3 14 10 6 2 13 9 5 1";# MAX passos

valor_entrada = "6 5 13 0 1 7 9 14 2 8 10 15 3 4 11 12"; # 15 passos
valor_entrada = "9 13 12 8 0 5 7 14 1 11 15 4 6 10 2 3";# undefined passos - 6
valor_entrada = "7 11 3 15 12 14 5 2 8 10 4 9 13 0 6 1";# undefined  passos - 5
valor_entrada = "2 1 5 9 3 6 10 13 4 7 11 14 0 8 12 15"; # 9 passos
valor_entrada = "2 1 5 0 7 9 10 13 6 4 3 15 8 11 12 14";# 25 passos
valor_entrada = "2 1 10 9 3 5 11 13 4 0 6 12 7 8 15 14";# 21 passos



def main():
	jogo = Jogo()

	tabuleiro = Tabuleiro()
	tabuleiro.inicializaTabuleiro(valor_entrada)

	#printTabuleiro(tabuleiro_ordenado)

	resultado = jogo.inicia_resolucao(tabuleiro)
	if(resultado!=False):
		jogo.print_resultado(resultado)
		print("Visitados",len(jogo.hash_tabuleiros_visitados))
		print("Abertos",len(jogo.tabuleiros_abertos))

main()
time_fim = time.time() - time_init

print("Tempo de execucao do script: ",time_fim)

#g(h) = altura da arvore