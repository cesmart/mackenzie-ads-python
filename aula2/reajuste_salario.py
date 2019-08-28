#Disciplina: Algorítmos e Programação I
#Função: : Calcular o novo salário de um funcionário, considerando a
#seguinte regra: os funcionários que possuem salário de até R$500,00 terão
#aumento de 20%. Os demais terão aumento de 10%
#Autor: Marcos César Martins
#Data: 11/08/2019

#Captura o salário atual do funcionário
salario_atual = float(input('Digite o salário atual do funcionário: '))

#Define o novo salário com o mesmo valor do salário atual
novo_salario = salario_atual

#Se o salário atual for menor ou igual a 500 concede 20% de reajuste. Caso #contrário, apenas 10%
if salario_atual <= 500 :
	novo_salario = salario_atual * 1.20
else :
	novo_salario = salario_atual * 1.10

#Exibe o novo salário
print('Novo salário: ', str(novo_salario))
