#Disciplina: Algorítmos e Programação I
#Função: : Calcular o valor de crédito oferecido ao cliente de um determinado banco baseado no saldo médio do mesmo no último ano
#Autor: Marcos César Martins
#Data: 11/08/2019

valor_credito = 0.0

#Captura o saldo médio
saldo_medio = float(input('Informe o saldo médio: '))

#Calcula o valor do crédito
if (saldo_medio <= 200.0):
	valor_credito = saldo_medio * 0.1
else :
	if (saldo_medio <= 300.0) :
		valor_credito = saldo_medio * 0.2
	else :
		if (saldo_medio <= 400.0) :
			valor_credito = saldo_medio * 0.25
		else :
			valor_credito = saldo_medio * 0.3

#Exibe o valor do crédito
print('Saldo médio de R$ {:5.2f}'.format(saldo_medio) + ' terá um crédito de R$ {:5.2f}'.format(valor_credito))
