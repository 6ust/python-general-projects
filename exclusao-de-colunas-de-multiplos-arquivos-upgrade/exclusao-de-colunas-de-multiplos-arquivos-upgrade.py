# Descriptor: Automatização de Exclusão Múltipla de Colunas em Arquivos de Texto
# Author:     Gust Guedes 

# Comandos do Sistema Operacional - OS 
import os
import sys
import shutil

# RegEX
import re

# Variaveis de Construção e Identificação do Caminho
pathRead  = "./originais/"
newFolder = "atualizados" 
pathSave  = "./" + newFolder + "/"


# Inicialização do Sistema
print("\n\n")
print("ATENÇÃO NÃO COLOQUE SEUS ARQUIVOS NA PASTA: [atualizados]")
print("POIS ELA SERA ATUALIZADA!")
print("Coloque seus arquivos na pasta: [originais].")
print("Pressione Enter, quando estiver pronto...")

# Limite de Coluna estabelecido para salvamento/Atualização
print("\n\n")
limitColumnUser = int(input("informe um limite: "))
searchUser = str(input("O que gostaria de deletar do(s) Arquivo(s): "))
confirmExec = str(input("Confirme se quer realmente utilizar esse texto\npara exclusão de linhas\n[s] - sim | [n] - não | [exit] - finalizar: "))

while (confirmExec != 'exit'):
	if (confirmExec == 's'):
		if(limitColumnUser > 0 or limitColumnUser == 78):
			limitColumn = limitColumnUser -  1
		elif(limitColumnUser <= 0):
			limitColumn = 78 - 1
		# exclui um diretório e todo o seu conteúdo.
		shutil.rmtree(pathSave)

		# Criar Diretorio
		os.mkdir(pathSave)

		print("\n\n")

		fileDir = os.listdir(pathRead)
		for file in fileDir:
			# Leitura de Documento/ Arquivo
			readFile = open(pathRead + file, "r", encoding="utf8")


			# Exibe o Nome do Arquivo
			print("------------------------------------")
			print(str(file) + " - Atualizado")

			# Salvamento de Documento/ Arquivo
			saveFile = open(pathSave + file, "a", encoding="utf8")
			for readLineFile in readFile:
				searchLine = re.search(searchUser,readLineFile)
				if(not searchLine):
					saveFile.write(str(readLineFile[:][:limitColumn]) + "\n")

			saveFile.close
			readFile.close
		print("------------------------------------")
		confirmExec = "exit"
	elif (confirmExec == 'n'):
		print("\n\n")

		# Inicialização do Sistema
		print("ATENÇÃO NÃO COLOQUE SEUS ARQUIVOS NA PASTA: [atualizados]")
		print("POIS ELA SERA ATUALIZADA!")
		print("Coloque seus arquivos na pasta: [originais].")
		print("Pressione Enter, quando estiver pronto...")

		# Limite de Coluna estabelecido para salvamento/Atualização
		print("\n\n")
		limitColumnUser = int(input("informe um limite: "))
		searchUser = str(input("O que gostaria de deletar do(s) Arquivo(s): "))
		confirmExec = str(input("Confirme se quer realmente utilizar esse texto\npara exclusão de linhas\n[s] - sim | [n] - não | [exit] - finalizar:"))