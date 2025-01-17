# 2– A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um
# carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da
# parcela. Considere o seguinte:

# a) O preço final para compra à vista tem um desconto de 20%:
# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:



#VARIAVEIS
valor_veiculo = float( input('Digite o valor do carro que deseja comprar:'))
valor_veiculo_total = 0
juros = None
valor_parcela = float(10)


#MODO DE PAGAMENTO À VISTA
print(f'\nO preço final à vista com desconto de 20% é de:R${valor_veiculo - valor_veiculo * 0.2}')


#MODO DE PAGAMENTO PARCELADO
for pagamento_parcelado in range (6, 60 + 1, 6):
    if pagamento_parcelado == 6:
        juros = 0.03
    elif pagamento_parcelado ==12:
        juros = 0.06
    elif pagamento_parcelado == 18:
        juros = 0.09
    elif pagamento_parcelado == 24:
        juros = 0.12
    elif pagamento_parcelado == 30:
        juros = 0.15
    elif pagamento_parcelado == 36:
        juros = 0.18
    elif pagamento_parcelado == 42:
        juros = 0.21
    elif pagamento_parcelado == 48:
        juros = 0.24
    elif pagamento_parcelado == 54:
        juros = 0.27
    elif pagamento_parcelado == 60:
        juros = 0.30


#CALCULO VALOR TOTAL E PARCELAS
    valor_veiculo_total = valor_veiculo + valor_veiculo * juros
    valor_parcela = valor_veiculo_total/pagamento_parcelado
    arredondado = round(valor_parcela, 2)

    print(f'O preço final parcelado em {pagamento_parcelado}x é de R${valor_veiculo_total} com parcelas de R${arredondado}')





