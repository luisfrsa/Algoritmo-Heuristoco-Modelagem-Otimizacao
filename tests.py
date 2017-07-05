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

class Jogo:
	def __init__(self):
		self.gg = 0
		self.izi = 0

	def __lt__(self, other):
		if (self.gg < other.gg):
			return True
		return False

	def __le__(self, other):
		if (self.gg < other.gg):
			return True
		return False

def positivo(valor):
	if(valor < 0):
		return valor*-1
	return valor	


import bisect
import random
l = []
for i in range(30):
	bisect.insort(l,random.randint(0,50))

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return False
print(index(l,10))

#asd = set()
#asd.add(5067)
#asd.add(-16309)
#asd.add(-12534)
#asd.add(190)
#asd.add(-13495)
#print(asd)
#print(next(x for x in asd))
#print(next(x for x in asd))

#set2 = set()
#set2.add(3)
#set2.add(1)
#set2.add(2)
#set2.add(5)
#set2.add(4)
#
#pope = set2.pop()
#print(pope)
#print(set2)
#
#
#jogo1 = Jogo()
#jogo2 = Jogo()
#jogo3 = Jogo()
#jogo4 = Jogo()
#gg = set()
#
#gtuple2 = (2, jogo2)
#gtuple1 = (1, jogo1)
#gtuple4 = (4, jogo4)
#gtuple3 = (3, jogo3) 
#
#gg.add(gtuple1)
#gg.add(gtuple3)
#gg.add(gtuple4)
#gg.add(gtuple2)
#mini = min(gg)
#print(mini)
#gg.remove(mini)
#print(gg)
#if(2 in gg):
#	print('achou')
#def binary_search(alist, item):
#    first = 0
#    last = len(alist)-1
#    found = False
#
#    while first<=last and not found:
#        midpoint = (first + last)//2
#        if alist[midpoint] == item:
#            found = True
#        else:
#            if item < alist[midpoint]:
#                last = midpoint-1
#            else:
#                first = midpoint+1
#
#    return found
#array_find = [-3814, 808, -12684, -16309, -12534, 5067, 190, -13495, 761, 9354, 4484, 1689, 14830, -265, -5838, 9967, 10760, 13089, -2943, -4213, 3745, 15884, 18112, -8628, -7301, -6808, 15397, 12440, -18328, 14323, -8853, 16154, 16610, -2051, -2274, -10236, 14991, 19634, -8897, 11886, -9622, 3069, -14006, 12262, 16497, -14008, -10367, 19053, 3018, -17033, 7250, 11802, -7497, 19736, 18605, -18229, 13016, -407, -9587, 1455, 12308, -5607, 7936, -15316, 12985, -3890, -4241, -727, 11963, 12706, 1535]
#len_find = len(array_find)
#
#import time
#import bisect
#import random

#list_rand = set()
#while (len(list_rand) <= 100000):
#	r = random.randint(-300000,300000)
#	if(not(r in list_rand)):
#		list_rand.add(r)
#strin = ', '.join(map(str, list_rand))
#f = open('array_rand.txt','a+')
#f.write(strin)
#f.close()

#f = open('array_rand.txt','r')
#gg = f.read().split(",")
#f.close()
#arr = set()
#for i in gg:
#	arr.add(int(i))
#
#
#var_set = set()
#var_list = []
#time_init = time.time()
#ind_find = 0
#
#for i in arr:
#	if(array_find[ind_find%(len_find)] in var_set):
#		print("achou ",array_find[ind_find%(len_find)])
#	var_set.add(i)
#	ind_find = ind_find + 1
#print(var_set)
#print("Fim SET ",(time.time() - time_init))

#time_init = time.time()
#ind_find = 0
#for i in arr:
#	if(binary_search(var_list, array_find[ind_find%(len_find)])  in var_list):
#		a = 0
#	bisect.insort(var_list,i) 
#	ind_find = ind_find + 1
#print("Fim Bisect ",(time.time() - time_init))
#print(len(var_list))

