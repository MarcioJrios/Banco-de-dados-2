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
