
a = list ()
for a1 in range(0,10):
    a.append (float(input('digite: ')))
print(f'os números selecionados foram {a}')
print('os números selecionados foram {}'.format(a))
b = int(input('escolha uma opção: 1-Média, 2-mediana, 3-variância ou 4-desvio. Qual sua escolha? '))

if(b==1):
    s1 = sum(a)/len(a)
    print(f'o resultado da média é {s1}')
elif(b==2):
    s2 = sorted(a)
    s3 = len(s2)
    s4 = round(len(s2)/2)
    if ((s3 % 2) != 0): ### IMPAR
        median = s3[s4]
        print(median)
    else:
        s4 = s2[0:-1]
        primeiro = round((len(s2)/2)-1)
        segundo = primeiro + 1
        median = (s4[primeiro]+s4[segundo])/2
        print(median) 