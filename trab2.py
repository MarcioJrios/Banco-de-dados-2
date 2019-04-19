import csv

Redo = []
Undo = []
variables = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0}
#arquivo = open(teste.txt, 'r')
arquivo = []
with open('teste.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        arquivo.append(row)

arquivo.reverse()
res_list = [item for list2 in arquivo for item in list2]

for item in res_list:
	instrucao = item
	#remove os sinais de maior e menos so pra n dar merda
	#instrucao = instrucao.replace("<","")
	instrucao = instrucao.replace(">","")
	#aqui ele começa verificando se há commit
	if 'commit' in instrucao:
		lista1 = list(instrucao.split(' ', 2))
		print(lista1[1])
		Redo.append(lista1[1])
	else :
		#aqui vão os casos das outras instruções
		if 'start' in instrucao:
			lista3 = list(instrucao.split(' ', 2))
			print(lista3[0])
			tr = lista3[0]
			if tr not in Redo:
				Undo.append(lista3[1])
			else :
				if 'Start' in instrucao:
					#por enquanto o checkpoint não faz diferença
					pass
				else:
					#a ultima instrução que faltou foi a opereção
					lista1 = list(instrucao.split(',', 4))
					if lista1[0] not in Redo:
						if lista1[0] in Undo:
							pass
						else:
							Undo.append(lista1[0])
					else:
						pass

#o segundo backlog que executa os Undo
for item in res_list:
	instrucao = item
	instrucao.replace("<","")
	instrucao.replace(">","")
	lista2 = list(instrucao.split(',', 4))
	if 'commit' in instrucao:
		pass
	else:
		#aqui vão os casos das outras instruções
		if 'start' in instrucao:
			pass
		else :
			if 'Start' in instrucao:
				#por enquanto o checkpoint não faz diferença
				pass
			else:
				#a ultima instrução que faltou foi a opereção
				if lista2[0] in Undo:
					variables[lista2[1]] = lista2[2]
				else:
					pass

#agora executa os redo
arquivo.reverse()
for item in arquivo:
	instrucao = item
	
print(Redo)
print(Undo)
