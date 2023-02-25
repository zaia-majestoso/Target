##FIBONACCI

vet = [0, 1]

n = int(input("digite um número: "))

for i in range(n-2):
    vet.append(vet[i] + vet[i+1])

if n in vet:
    print(vet)
    print("seu numero esta na sequencia")
else:
    print(vet)
    print("seu numero nao esta na sequencia")
    
    
    
##PERCENTUAL
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
total = 180759.98

n = int(input("""digite qual estado você gostaria de visualizar o percentual de contribuição
sendo SP[1], RJ[2], MG[3], ES[4], OUTROS[5]"""))

if n == 1:
    SP = (SP*100)/total
    print(f"O estado selecionado contribuiu com um percentual de {SP}")
elif n == 2:
    RJ = (RJ*100)/total
    print(f"O estado selecionado contribuiu com um percentual de {RJ}")
elif n == 3:
    MG = (MG*100)/total
    print(f"O estado selecionado contribuiu com um percentual de {MG}")
elif n == 4:
    ES = (ES*100)/total
    print(f"O estado selecionado contribuiu com um percentual de {ES}")
elif n == 5:
    OUTROS = (OUTROS*100)/total
    print(f"O estado selecionado contribuiu com um percentual de {OUTROS}")
    
    
    
##Inverte palavra
n = (input("Escreva sua palavra para ser escrita ao contrario: "))
print(n[::-1])



##Faturamento
faturamento = [1300, 2000, 900, 350, 0, 1500, 3000, 1200, 950, 0, 3400]
maior = 0
menor = 0
som = 0
med = 0
n = int(input("""Digite o que deseja visualizar:
[1]O menor valor de faturamento ocorrido em um dia do mês
[2] O maior valor de faturamento ocorrido em um dia do mês
[3] Número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""))

if n == 1:
    for i in range(len(faturamento)):
        menor = faturamento[0]
        if faturamento[i]<menor:
            menor = faturamento[i]
    print(f"o menor faturamento foi de {menor} no dia {i}")
elif n == 2:
    for i in range(len(faturamento)):
        maior = faturamento[0]
        if faturamento[i] > maior:
            maior = faturamento[i]
    print(f"o maior faturamento foi de {maior} no dia {i}")
elif n == 3:
    for i in range(len(faturamento)):
        som = som + faturamento[i]
    med = som/i
    print(med)
    for i in range(len(faturamento)):
        if faturamento[i] > med:
            print(f"o faturamento do dia {i} foi maior que a media")
