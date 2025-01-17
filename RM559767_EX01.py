#1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas, gastos, dívidas e investimentos.
# Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria financeira.
# Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
# da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.
#Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição.
#É importante o programa validar a possibilidade de empate.




#NUMERO DE COLABORADORES
colaboradores = int(input('Informe o número de colaboradores:'))


#VARIAVEL DOS VOTOS
voto_segunda = 0
voto_terca = 0
voto_quarta = 0
voto_quinta = 0
voto_sexta = 0


#CONTABILIZANDO OS VOTOS
for colaborador in range(1, colaboradores +1, 1):
    votos = input('Informe o dia de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira):')
    if votos == 'segunda-feira':
        voto_segunda = voto_segunda + 1
    elif votos == 'terça-feira':
        voto_terca = voto_terca + 1
    elif votos == 'quarta-feira':
        voto_quarta = voto_quarta + 1
    elif votos == 'quinta-feira':
        voto_quinta = voto_quinta + 1
    elif votos == 'sexta-feira':
        voto_sexta = voto_sexta + 1


#CALCULO DO DIA MAIS VOTADO
if voto_segunda > voto_terca and voto_segunda > voto_quarta and voto_segunda > voto_quinta and voto_segunda > voto_sexta:
    print('\nO dia escolhido pelos colaboradores foi segunda-feira.')


elif voto_terca > voto_segunda and voto_terca > voto_quarta and voto_terca > voto_quinta and voto_terca > voto_sexta:
    print('\nO dia escolhido pelos colaboradores foi terça-feira.')


elif voto_quarta > voto_segunda and voto_quarta > voto_terca and voto_quarta > voto_quinta and voto_quarta > voto_sexta:
    print('\nO dia escolhido pelos colaboradores foi quarta-feira.')


elif voto_quinta > voto_segunda and voto_quinta > voto_terca and voto_quinta > voto_quarta and voto_quinta > voto_sexta:
    print('\nO dia escolhido pelos colaboradores foi quinta-feira.')



elif voto_sexta > voto_segunda and voto_sexta > voto_terca and voto_sexta > voto_quarta and voto_sexta > voto_quinta:
    print('\nO dia escolhido pelos colaboradores foi sexta-feira.')



#EMPATE DE VOTOS

elif voto_segunda == voto_terca and voto_segunda > voto_quarta and voto_segunda > voto_quinta and voto_segunda > voto_sexta:
    print('\nHouve um empate entre segunda-feira e terça-feira, por favor realize a votação novamente!')

elif voto_segunda == voto_quarta and voto_segunda > voto_terca and voto_segunda > voto_quinta and voto_segunda > voto_sexta:
    print('\nHouve um empate entre segunda-feira e quarta-feira, por favor realize a votação novamente!')

elif voto_segunda == voto_quinta and voto_segunda > voto_terca and voto_segunda > voto_quarta and voto_segunda > voto_sexta:
    print('\nHouve um empate entre segunda-feira e quinta-feira, por favor realize a votação novamente!')

elif voto_segunda == voto_sexta and voto_segunda > voto_terca and voto_segunda > voto_quarta and voto_segunda > voto_quinta:
    print('\nHouve um empate entre segunda-feira e sexta-feira, por favor realize a votação novamente!')

elif voto_terca == voto_quarta and voto_terca > voto_segunda and voto_terca > voto_quinta and voto_terca > voto_sexta:
    print('\nHouve um empate entre terça-feira e quarta-feira, por favor realize a votação novamente!')

elif voto_terca == voto_quinta and voto_terca > voto_segunda and voto_terca > voto_quarta and voto_terca > voto_sexta:
    print('\nHouve um empate entre terça-feira e quinta-feira, por favor realize a votação novamente!')

elif voto_terca == voto_sexta and voto_terca > voto_segunda and voto_terca > voto_quarta and voto_terca > voto_quinta:
    print('\nHouve um empate entre terça-feira e sexta-feira, por favor realize a votação novamente!')

elif voto_quarta == voto_quinta and voto_quarta > voto_segunda and voto_quarta > voto_terca and voto_quarta > voto_sexta:
    print('\nHouve um empate entre quarta-feira e quinta-feira, por favor realize a votação novamente!')

elif voto_quarta == voto_sexta and voto_quarta > voto_segunda and voto_quarta > voto_terca and voto_quarta > voto_quinta:
    print('\nHouve um empate entre quarta-feira e sexta-feira, por favor realize a votação novamente!')

elif voto_quinta == voto_sexta and voto_quinta > voto_segunda and voto_quinta > voto_terca and voto_quinta > voto_quarta:
    print('\nHouve um empate entre quinta-feira e sexta-feira, por favor realize a votação novamente!')










