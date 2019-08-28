#Disciplina: Algorítmos e Programação I
#Função: : Calcular o novo preço de um produto, sabendo que foi concedido um desconto #de 10% no preço original
#Autor: Marcos César Martins
#Data: 11/08/2019

#Captura o preço atual do produto
preco_atual = float(input('Digite o preço atual do produto: '))

#Define o novo preço, aplicando o desconto de 10%
novo_preco = preco_atual - (preco_atual * 0.1)

#Exibe o novo preço
print('Novo preço: ', str(novo_preco))