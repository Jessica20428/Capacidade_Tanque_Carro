#Construa um programa que calcule: Quanto custa encher o tanque do carro 
#que tem 50 litros de capacidade, está com 20 litros de combustível atualmente e o custo do combustível é de 
#R$5,80/litro?

#Declarando a variável capacidade_tanque recebendo o valor de 50
capacidade_tanque = 50
#Declarando a variável volume_atual recebendo o valor de 20
volume_atual = 20
#Declarando a constante custo_litro recebendo o valor de 5.80
custo_litro = 5.80

#Descobrindo qual a quantidade que ainda falta para encher o tanque do carro, subtraindo a capacidade do tanque pelo valor que foi enchido
litros_encher = capacidade_tanque - volume_atual
#Descobrindo o custo de quantos litros vai precisar pagar para encher a capacidade que ainda falta do tanque de combustível do carro, multiplicando os litros que ainda
#falta para encher * o custo do combustível por litro
custo_total = litros_encher * custo_litro
#Exibindo o resultado final do custo que iremos pagar
print(custo_total)

#E se fôssemos encher com diesel, a R$5.03 o litro?

#capacidade_tanque = 50
#volume_atual = 20
#custo_litro = 5.03

#litros_encher = capacidade_tanque - volume_atual
#custo_total = litros_encher * custo_litro

#print(custo_total)