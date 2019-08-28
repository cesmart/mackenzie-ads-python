#Disciplina: Algorítmos e Programação I
#Função: Calcular a média aritmética entre duas notas e informar se o
#aluno foi aprovado ou reprovado. Considerar nota para aprovação >= 7
#Autor: Marcos César Martins
#Data: 11/08/2019

#Captura a primeira nota
nota_1 = float(input('Digite a primeira nota: '))

#Captura a segunda nota
nota_2 = float(input('Digite o segunda nota: '))

#Calcula a média entre as duas notas
media = (nota_1 + nota_2) / 2

#Exibe a média
print('Média = ' + str(media))

#Se a média for maior ou igual a 7.0 exibe a mensagem 'Aprovado'. Senão
#exibe a mensagem 'Reprovado'
if media >= 7 :
	print('Aprovado')
else :
	print('Reprovado')