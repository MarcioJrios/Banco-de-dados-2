import csv
redo = []
redo2 = []
undo = []
arquivo = []
variables = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0}
with open('teste01', newline='') as inputfile:
    for row in csv.reader(inputfile):
        arquivo.append(row)
arquivo.reverse()
res_list = [item for list2 in arquivo for item in list2]
lenght = len(res_list)
i = 0
print("Passo 1")
while res_list[i][:-3] != "<Start CKPT":
    if res_list[i][:8] == "<commit " :
        redo.append(res_list[i][-3:-1])
    if res_list[i][:7] == "<start " :
        if res_list[i][-3:-1] not in redo:
            undo.append(res_list[i][-3:-1])
    i += 1
print(undo)
print(redo)
print("Passo 2")
while res_list[i][-2:-1] != ")" :
    x = redo.count(res_list[i][-2:])
    if x == 0 :
        undo.append(res_list[i][-2:])
    i += 1
i += 1
x = redo.count(res_list[i][-2:])
if x == 0 :
    undo.append(res_list[i][-2:])
print("Fim passo 2")
redo2 = redo.copy()
print(redo)
print(undo)
print("Passo 3")
tamanho = len(undo)
aux = 0
print(undo)
aux2 = len(res_list)
while aux < aux2 - 2:
    if "<start " in res_list[aux] :
        z = redo.count(res_list[aux][-3:-1])
        if z == 1:
            redo.remove(res_list[aux][-3:-1])
    if res_list[aux][1:3] in undo :
        variables[res_list[aux+1]] = res_list[aux+2]
        print("fez undo")
        print(res_list[aux][1:3])
    aux += 1
print("Passo 4")
print(redo)
print(res_list[aux])
tamanho = len(redo2)
i = 0
if tamanho > 0 :
    while tamanho > 0:
        if "<start " in res_list[i]:
            z = redo2.count(res_list[i][-3:-1])
            if z == 1:
                redo2.remove(res_list[i][-3:-1])
        i += 1
        tamanho = len(redo2)
i -= 1
print("Passo 5")
print(res_list[i])
aux = len(res_list)
while i > 0 :
    x = redo.count(res_list[i][1:3])
    if x == 1:
        variables[res_list[i+1]] = res_list[i+3][-3:-1]
        redo.remove(res_list[i][1:3])
        print("fez redo")

    i -= 1
print(undo)
print(redo2)
print(variables)
