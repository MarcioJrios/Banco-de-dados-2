#https://www.techbeamers.com/python-tutorial-step-by-step/
import csv

Redo = []
Undo = []

#arquivo = open(teste.txt, 'r')
arquivo = []
with open('teste.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        arquivo.append(row)

arquivo.reverse()
print(arquivo)
print(len(arquivo))

for item in arquivo:
	instrucao = item
	instrucao.replace("<","")
	instrucao.replace(">","")
	#aqui ele começa verificando se há commit
	if 'commit' in instrucao:
		lista1 = list(instrucao.split('', 1))
		Redo.append(lista1[0][1])
	else
		#aqui vão os casos das outras instruções
		if 'start' in instrucao:
			lista1 = list(instrucao.split('', 1))
			if lista2[0][1] not in Redo:
				Undo.append(lista1[0][1])
			else 
				if 'Start' in instrucao:
					#por enquanto o checkpoint não faz diferença
					pass
				else
					#a ultima instrução que faltou foi a opereção
					lista1 = list(instrucao.split(',', 4))
					if lista1[0][0] not in Redo:
						if lista1[0][0] in Redo:
							pass
						else
							Undo.append(lista1[0][0])
					else
						pass
