with open("pablo.txt","r") as arquivo:
    pablo = arquivo.readlines()
print('\n')
if len(pablo)>10:
    print('4')
elif len(pablo)==10:
    print('3')
elif len(pablo)==7:
    print('2')
else:
    print('1')
print('\n')

for i in range(len(pablo)):
    if 'U' in pablo[i]:
        if i == 1:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            uniao = x + y
            h = []
            for g in range(len(uniao)):
                if uniao[g] not in h:
                    h.append(uniao[g])
            print(f'União: conjunto 1 {x}, conjunto 2 {y}. Resultado: {h}')
            print('\n')

        elif i == 4:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            uniao = x + y
            h = []
            for g in range(len(uniao)):
                if uniao[g] not in h:
                    h.append(uniao[g])
            print(f'União: conjunto 1 {x}, conjunto 2 {y}. Resultado: {h}')
            print('\n')
        elif i == 7:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            uniao = x + y
            h = []
            for g in range(len(uniao)):
                if uniao[g] not in h:
                    h.append(uniao[g])
            print(f'União: conjunto 1 {x}, conjunto 2 {y}. Resultado: {h}')
            print('\n')
        elif i == 10:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            uniao = x + y
            h = []
            for g in range(len(uniao)):
                if uniao[g] not in h:
                    h.append(uniao[g])
            print(f'União: conjunto 1 {x}, conjunto 2 {y}. Resultado: {h}')
            print('\n')

    if 'I' in pablo[i]:
        if i == 1:
            oi=[]
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            for w in range(len(x)):
                for j in range(len(y)):
                    if x[w] == y[j]:
                        v = oi.append(x[w])
            print(f'Interseção: conjunto 1 {x}, conjunto 2 {y}. Resultado: {oi}')
            print('\n')
        elif i == 4:
            oi=[]
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            for w in range(len(x)):
                for j in range(len(y)):
                    if x[w] == y[j]:
                        v = oi.append(x[w])
            print(f'Interseção: conjunto 1 {x}, conjunto 2 {y}. Resultado: {oi}')
            print('\n')
        elif i == 7:
            oi=[]
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            for w in range(len(x)):
                for j in range(len(y)):
                    if x[w] == y[j]:
                        v = oi.append(x[w])
            print(f'Interseção: conjunto 1 {x}, conjunto 2 {y}. Resultado: {oi}')
            print('\n')
        elif i == 10:
            oi=[]
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            for w in range(len(x)):
                for j in range(len(y)):
                    if x[w] == y[j]:
                        v = oi.append(x[w])
            print(f'Interseção: conjunto 1 {x}, conjunto 2 {y}. Resultado: {oi}')
            print('\n')

    if 'D' in pablo[i]:
        if i == 1:
            s = pablo[i+1]
            v = pablo[i+2]
            z = s.replace(',','')
            q = v.replace(',','')
            x = z.split()
            y = q.split()
            d = []
            for t in range(len(x)):
                if x[t] not in y:
                    d.append(x[t])
            print(f'Diferença: conjunto 1 {x}, conjunto 2 {y}. Resultado: {d} ')
            print('\n')
        elif i == 4:
            s = pablo[i+1]
            v = pablo[i+2]
            z = s.replace(',','')
            q = v.replace(',','')
            x = z.split()
            y = q.split()
            d = []
            for t in range(len(x)):
                if x[t] not in y:
                    d.append(x[t])
            print(f'Diferença: conjunto 1 {x}, conjunto 2 {y}. Resultado: {d} ')
            print('\n')
        elif i == 7:
            s = pablo[i+1]
            v = pablo[i+2]
            z = s.replace(',','')
            q = v.replace(',','')
            x = z.split()
            y = q.split()
            d = []
            for t in range(len(x)):
                if x[t] not in y:
                    d.append(x[t])
            print(f'Diferença: conjunto 1 {x}, conjunto 2 {y}. Resultado: {d} ')
            print('\n')
        elif i == 10:
            s = pablo[i+1]
            v = pablo[i+2]
            z = s.replace(',','')
            q = v.replace(',','')
            x = z.split()
            y = q.split()
            d = []
            for t in range(len(x)):
                if x[t] not in y:
                    d.append(x[t])
            print(f'Diferença: conjunto 1 {x}, conjunto 2 {y}. Resultado: {d} ')
            print('\n')

    if 'C' in pablo[i]:
        if i == 1:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            print(f'Cartesiano: conjunto 1 {x}, conjunto 2 {y}. Resultado: ')
            for c in range(len(x)):
                for j in range(len(y)):
                    print(f'[{x[c]}, {y[j]}]')
            print('\n')
        elif i == 4:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            print(f'Cartesiano: conjunto 1 {x}, conjunto 2 {y}. Resultado: ')
            for c in range(len(x)):
                for j in range(len(y)):
                    print(f'[{x[c]}, {y[j]}]')
            print('\n')
        elif i == 7:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            print(f'Cartesiano: conjunto 1 {x}, conjunto 2 {y}. Resultado: ')
            for c in range(len(x)):
                for j in range(len(y)):
                    print(f'[{x[c]}, {y[j]}]')
            print('\n')
        elif i == 10:
            s = pablo[i+1]
            v = pablo[i+2]
            q = v.replace(',','')
            z = s.replace(',','')
            x = z.split()
            y = q.split()
            print(f'Cartesiano: conjunto 1 {x}, conjunto 2 {y}. Resultado: ')
            for c in range(len(x)):
                for j in range(len(y)):
                    print(f'[{x[c]}, {y[j]}]')
            print('\n')
