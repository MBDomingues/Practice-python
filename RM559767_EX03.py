#3 – Na oferta de um produto de crédito aos clientes, três informações são muito importantes
#apresentar ao cliente: valor da dívida, a taxa de juros e o número de parcelas para pagamento
#do empréstimo contraído junto à Fintech. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

#Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.



#VARIAVEIS
juros = float
valor_total = float
valor_parcela = float
valor_juros = float


#VALOR DA DÍVIDA
valor_divida = float(input("Por favor informe a sua dívida:"))


#DÍVIDA EM UMA PARCELA
print(f'\nTotal:R$ {valor_divida} Juros:R$0.00 Número de parcelas:1 Valor da parcela:R$ {valor_divida}')


#DÍVIDA COM JUROS
for tabela_de_parcelas in range (3, 12 + 1, 3):
    if tabela_de_parcelas == 3:
        juros = 0.1
    elif tabela_de_parcelas == 6:
        juros = 0.15
    elif tabela_de_parcelas == 9:
        juros = 0.2
    elif tabela_de_parcelas == 12:
        juros = 0.25

    valor_total = valor_divida + valor_divida * juros
    valor_parcela = valor_total / tabela_de_parcelas
    valor_juros = valor_divida * juros
    valor_parcela_arredondado = round(valor_parcela, 2)


    print(f'Total:R$ {valor_total} Juros:R$ {valor_juros} Número de parcelas: {tabela_de_parcelas} Valor da Parcela:R$ {valor_parcela_arredondado}')