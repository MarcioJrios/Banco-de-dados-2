import csv

Redo = []
Undo = []
Check = []
variables = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0}
arquivo = []
with open('teste03.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        arquivo.append(row)

arquivo.reverse()
res_list = [item for list2 in arquivo for item in list2]
tam = len(res_list)
i=0
#o primeiro backlog que define o que deve ser Undo e Redo
for item in res_list:
	instrucao = item
	#remove os sinais de maior e menor so pra n dar merda
	instrucao = instrucao.replace("<","")
	instrucao = instrucao.replace(">","")
	#aqui ele começa verificando se há commit
	if 'commit' in instrucao:
		lista1 = list(instrucao.split(' ', 2))
		Redo.append(lista1[1])
	else :
		#aqui vão os casos das outras instruções
		if 'start' in instrucao:
			lista3 = list(instrucao.split(' ', 2))
			tr = lista3[1]
			if tr in Redo:
				pass
			else :
				Undo.append(tr)
		else:
			if 'Start' in instrucao:
				Check = Redo
			else:
				#a ultima instrução que faltou foi a opereção
				pass
			
	i=i+1

CKPT = 'false'
save = -1
i = 0
#o segundo backlog que executa os Undo e Redo comitados antes do CKPT
for item in res_list:
	instrucao = item
	instrucao = instrucao.replace("<","")
	instrucao = instrucao.replace(">","")
	#lista2 = list(instrucao.split(',', 4))
	if 'commit' in instrucao:
		lista1 = list(instrucao.split(' ', 2))
		if CKPT == 'true':
			Redo.remove(lista1[1])
		else:
			pass
	else:
		#aqui vão os casos das outras instruções
		if 'start' in instrucao:
			pass
		else :
			if 'Start' in instrucao: #considera o checkpoint
				if CKPT = 'false':
					save = i; #salva a posição em que o checkpoint foi encontrado
					CKPT = 'true'
				else:
					pass
			else:
				if instrucao[:1] == 'T':
					if instrucao in Undo:
						variables[res_list[i+1]] = res_list[i+2]
					else:
						pass
				else:
					pass
	i = i+1
	if CKPT == 'true':
		while i != save:
			if res_list[i][:1] == 'T':
				#a ultima instrução que faltou foi a opereção
				if instrucao in Redo:
					variables[res_list[i+1]] = res_list[i+3].replace(">", "")
				else:
					pass
			else:
				if res_list[i][:1] == 'c':
					lista1 = list(res_list[i].split(' ', 2))
					Redo.remove(lista1[1])
				else:
					pass
		i = i-1
					

i=0
#agora executa os redo
arquivo.reverse()
res_list = [item for list2 in arquivo for item in list2]
for item in res_list:
	instrucao = item
	instrucao = instrucao.replace("<","")
	instrucao = instrucao.replace(">","")
	if 'commit' in instrucao:
		pass
	else:
		if 'start' in instrucao:
			pass
		else :
			if 'Start' in instrucao:
				#o checkpoint não faz diferença
				pass
			else:
				if instrucao[:1] == 'T':
					#a ultima instrução que faltou foi a opereção
						if instrucao in Redo:
							variables[res_list[i+1]] = res_list[i+3].replace(">", "")
						else:
							pass
				else:
					pass
	i = i+1


print(res_list)
print(Redo)
print(Undo)
print(variables)
