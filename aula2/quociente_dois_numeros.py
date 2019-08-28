#Disciplina: Algorítmos e Programação I
#Função: Calcular a divisão entre dois números reais
#Autor: Marcos César Martins
#Data: 28/08/2019

#Captura o primeiro número
num_1 = float(input('Digite o primeiro número: '))

#Captura o segundo número
num_2 = float(input('Digite o segundo número: '))

#Se o segundo número for igual a zero não efetua a divisão e exibe a
#mensagem 'Impossível Dividir'
if num_2 == 0 :
	print('Impossível Dividir')
else :
	#Realiza a divisão entre os dois números capturados
	resultado = num_1 / num_2

	#Exibe o resultado da divisão
	print('Divisão = ' + str(resultado))