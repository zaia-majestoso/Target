import time
from time import sleep
sim = 0


print('-'*20, 'TRUCO: ORIGINS ', '-'*20)
time.sleep(1)
n = int(input('pressione 1 para jogar'))
time.sleep(0.5)
if n == 1:
    print("""    A nossa história se passa em meados do século XIX quando um famoso jogo atual estava apenas começando a ser febre entre os poderosos da época.
	Eram tempos de crise ao redor daquela área e os únicos que tinham condições de apostar eram os mais nobres. A cada vez que reuniam-se, mais ia aumentando
a rivalidade entre aquelas famílias e mais ia aumentando a alegria e sede do povo em ver essas disputas estratégicas.
	Porém, quanto mais tempo se passava, mais perigoso ficava, pois as disputas começaram a valer muito dinheiro e, com a crise, todos davam de tudo para ganhar
e enganar os seus adversários no truco.""")

print('-'*20)

m = int(input("pressione 1 para avançar"))
if m == 1:
    print("""   O maior torneio da época, le tour du maître, estava na reta final e os oito finalistas estavam todos com suas devidas duplas, jogando como se não houvesse amanhã.
   Blefe pra cá, gritos de 'TRUCO' e 'SEIS' podiam ser ouvidos de longe, a torcida suando frio e roendo as unhas por conta da tensão era tudo que se podia presenciar.
   Eram dois jogos simultâneos e os dois que conseguissem sobrar, seriam então os vencedores do torneio.""")
    time.sleep(0.5)
t = str(input("(gostaria de ver as regras do truco?) [S/N]")).upper()

while t not in 'SN':
    t = str(input("(gostaria de ver as regras do truco?) [S/N]")).upper()
if t == 'S':
    print('-'*20)
    print('''Em cada rodada, um jogador deve colocar uma de suas cartas na mesa, e o jogador com a carta mais forte vence a rodada. Quem ganhar 2
dessas rodadas ganha a mão e marca 1 ponto, e uma nova mão se inicia. Durante as rodadas, os jogadores têm a opção de pedir Truco, Seis, Nove
e Doze, aumentando o valor da rodada. A carta mais forte do jogo (fora a manilha) é o 3.''')
    print('-' * 20)
    time.sleep(1)
    sim += 1
if t in 'N' or sim == 1:
    print('Os jogos estavam da seguinte forma:')
print('='*20)
print('''**JOGO 1**
Zai de LaVinn e C.Aike
		x
Frank Madero e Vitchello Fumapód


**JOGO 2**
Lukka De Salão e Sir Mustache
		x
Edward McDonald e Pete Gun-lightyear''')
print('='*20)
m = int(input("pressione 1 para avançar"))
if m == 1:
    print('''   Os dois vencedores, numa melhor de três, de cada jogo se enfrentaria na final para decidir o campeão. 
Entretanto, no meio da segunda partida, pouco tempo após o intervalo, se ouve da plateia:
"O que é aquilo?"
Todos os olhos se voltam para o mesmo lugar...
''')
print('''   Um homem sai do banheiro mostrando um baralho adulterado, com cartas de número 3 milimetricamente menores do que as demais.
Esse tipo de baralho é muito eficiente para roubos e claramente foi usado e alguém esqueceu ao ir ao banheiro.
O jogo para e a briga entre os jogadores se instaura. Xingamentos pra ca e para lá mas ninguém podia provar nada.''')
m = int(input("pressione 1 para avançar"))
if m == 1:
    print('\n' * 50)
print('''Você controlará a Detetive Ralf Kellyson e trará o pilantra que tentou roubar o prêmio à justiça.
Tudo que recebeu foi uma série de descrições sobre os únicos 9 que poderiam ter planejado o crime.''')
print( '''Você pode acusar alguém a qualquer hora apertando 'p', mas terá que justificar o porquê está acusando, de forma que quem esteja sendo acusado
se encaixe nos 5 quadros (os quadros referidos serão mostrados adiante).
O jogador fará isso apresentando os métodos de manipulação usados para chegar em determinada conclusão.
EX: João estava na cena do crime ou viu tudo de longe
    João não viu tudo de longe (...pois é míope)
----------------------------------------------------------
    João estava na cena do crime

Quem quer acusar? R = João

Por que? R = Silogismo Disjuntivo
Segunda justificativa R = ...
Terceira ...

Você perde caso prenda alguém inocente ou não tenha provas o suficiente para prender alguém''')

F = str(input('pressione F para ver a lista de suspeitos')).upper()
while F not in 'F':
    F = str(input('pressione F para ver a lista de suspeitos')).upper()
print('='*50)
print ('''       -------------------------------------------------------------------------------
       |Sir Mustache  ----- Bigode suspeito, arrogante                                |
       |Zai de LaVinn ----- Esnobe, confiante, germofóbico                            |
       |Frank Madero  ----- Blefa sempre, Corajoso, Olhar penetrante                  |
       |(Juiz) Antonietto Pauline ---- Humilde, meio-irmão de Pete, cristão           |
       |Conde Aike    ----- Recém divorciado, Conde, seguro de si                     |
       |Edward McDonald ---- comédia, usa humor pra distração, sente muita sede       |
       |Pete Gun-lightyear ---- Ex militar, falido, fuma muito                        |
       |Lukka De Salão ----- calado, frio, não se sabe muito dele                     |
       |Vitchello Fumapód ---- não completou o ensino médio, mágico, fofoqueiro       |
       --------------------------------------------------------------------------------''')
print('\n')
print('''                               A PESSOA QUE PRENDER TEM QUE SE ENCAIXAR NOS SEGUINTES QUADROS:
FOI UM DOS 5 ÚLTIMOS A SAIR DO BANHEIRO 
NÃO ESTAVA PERDENDO(desconsidere se for o juíz)
ATITUDE SUSPEITA(tem motivo para roubar, mentiu)
ESTAVA NO BANHEIRO DURANTE A BRIGA'''  )
time.sleep(1.5)
pergunta1 = '1 - Como estava indo seu jogo?'
pergunta2 = '2- O que fez no intervalo?'

print('\n'*2)
print('''       A) Sir Mustache
       B) Zai de LaVinn
       C) Frank Madero
       D) Juíz Antonietto Pauline
       E) Conde Aike
       F) Edward McDonald
       G) Pete Gun-Lightyear
       H) Lukka De Salão
       I) Vitchello Fumapód''')
opcao =  str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
while opcao != 'P':
    while opcao == 'A':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Sir Mustache?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'B':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Zai de LaVinn?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'C':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Frank Madero'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'D':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Juíz Antonietto Pauline?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'E':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para C.Aike?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('''legal''')
            print('-' * 50)
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'F':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Edward McDonald?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'G':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Pete Gun-Lightyear?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
    while opcao == 'H':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Lukka De Salão?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')
    while opcao == 'I':
        print(f'{pergunta1} {pergunta2}')
        pergunta = int(input('O que deseja perguntar para Vitchello Fumapód?'))
        if pergunta == 1:
            print('legal')
            print('\n')
        elif pergunta == 2:
            print('massa')
            print('\n')

        opcao = str(input("Selecione para quem deseja perguntar ou pressione 'p' para acusar")).upper()
print('''       A) Sir Mustache
       B) Zai de LaVinn
       C) Frank Madero
       D) Juíz Antonietto Pauline
       E) Conde Aike
       F) Vitchello Fumapód
       G) Pete Gun-Lightyear
       H) Lukka De Salão
       I) Vitchello Fumapód''')
acusar = str(input('Quem você gostaria de acusar?')).upper()
while acusar not in 'ABCDEFGHI':
    print('Opção inválida.')
    acusar = str(input('Quem você gostaria de acusar?')).upper()
while acusar in 'ABCDEFGHI':
    print('''                1 - ADIÇÃO
				2 - SIMPLIFICAÇÃO
				3 - CONJUNÇÂO
				4 - MODUS PONENS
				5 - MODUS TOLLENS
				6 - SILOGISMO DISJUNTIVO
				7 - SILOGISMO HIPOTÉTICO
				8 - DILEMA CONSTRUTIVO
				9 - DILEMA DESTRUTIVO''')

    pq = int(input('Por que? '))
    pq2 = int(input('Segunda justificativa '))
    pq3 = int(input('Terceira justificativa '))
    if acusar == 'B' and pq == 1 and pq2 == 2 and pq3 == 3:
        print('''Você prendeu Zai De Lavinn, o ladrão por trás de tudo isso e ainda provou sua culpa.'
                                    PARABÉNS, DETETIVE! VOCÊ VENCEU!''')
        break
    else:
        print('''Você prendeu o suspeito injustamente e sem provas o suficiente para provar sua culpa.
                                       VOCÊ PERDEU''')
        break















































