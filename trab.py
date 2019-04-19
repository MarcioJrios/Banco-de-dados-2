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
	if 'commit' in instrucao:
		lista1 = list(instrucao.split('', 1))
		Redo.append(lista1[0][1])
	else
		#aqui vão os casos das outras instruções
