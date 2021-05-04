#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 30/03/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

1 – Leia uma temperatura em graus Celsius e apresente-a convertida em graus
Fahrenheit. A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura
em Fahrenheit e C a temperatura em Celsius.

C = float(input(('Celsius para Fahrenheit:')))
F = C * (9.0 / 5.0)
print('sua resposta é {}°F'.format(F))

-----------------------------------------------------------------------------------

2 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
Celsius. A fórmula de conversão é: C = 5.0 * (F – 32.0) / 9.0, sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius.

F = float(input('Celsius para Fahrenheit:'))
C = 5.0 * (F – 32.0) / 9.0
print('sua resposta é {}°C'.format(C))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 01/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


1 – Modifique o algoritmo anterior de modo que o usuário possa escolher qual conversão
ele deseja fazer: Celsius → Fahrenheit ou Fahrenheit → Celsius. Em seguida, faça o
cálculo e mostre o resultado.

  
A = int(input('0 - Fahrenheit para celsius. 1 - Celsius para Fahrenheit. Qual a sua escolha?'))
if (A == 0):
    F = float(input('Fahrenheit para celsius:'))
    F1 = 5.0*(F-32.0)/9.0
    print('sua resposta é {}'.format(F1))
elif (A == 1):
    C = float(input('Celsius para Fahrenheit:'))
    C1 =  C *(9.0/5.0) + 32.0
    print('sua resposta é {}'.format(C1))
else:
    print('você deve escolher entre 0 é 1')


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 05/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é: M = K / 3.6, sendo K a velocidade em km/h e M em m/s.

K = float(input('insira a velocidade de KM/H para que possa ser convertida em M/S :'))
M =  K / 3.6
print('o resultado da conversão de km/h para m/s é {}'.format(B))

-----------------------------------------------------------------------------------

Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.

M = float(input('insira a velociade em M/S para que possa ser convertido em KM/H :'))
K = M * 3.6
print('o resultado da conversão de M/S para Km/h é {}'.format(K))

-----------------------------------------------------------------------------------

O algoritmo deve permitir que o usuário possa escolher qual conversão ele deseja fazer: km/h -> m/s ou m/s -> km/h.

A = int(input('1 - km/h -> m/s ou 2 - m/s -> km/h :'))
if(A == 1):
    K = float(input('insira a velocidade de KM/H para que possa ser convertida em M/S :'))
    M =  K / 3.6
    print('o resultado da conversão de km/h para m/s é {:.1f} m/s'.format(M))
elif(A == 2):
    M = float(input('insira a velociade em M/S para que possa ser convertido em KM/H :'))
    K = M * 3.6
    print('o resultado da conversão de M/S para Km/h é {:.1f} Km/h'.format(K))
else:
    print('o numeros devem ser 1 - km/h -> m/s ou 2 - m/s -> km/h ')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 06/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres. 
A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres.

M = float(input('insira m² para converter em acres :'))
A = M * 0.000247
print('{} acres'.format(A))

-----------------------------------------------------------------------------------

Leia um valor de área em acres e apresente-o convertido em metros quadrados m2. 
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.

A = float(input('insira acres para converter em m² :'))
M = A * 4048.58
print('{} m²'.format(M))

-----------------------------------------------------------------------------------

O algoritmo deve permitir que o usuário possa escolher qual conversão ele deseja fazer: m2 -> acres ou acres -> m2.

O = int(input('insira 1 para m2 -> acres. ou 2 acres -> m2'))

if(O== 1):
    M = float(input('insira m² para converter em acres :'))
    A = M * 0.000247
    print('{} acres'.format(A))
elif(O==2):
    A = float(input('insira acres para converter em m² :'))
    M = A * 4048.58
    print('{} m²'.format(M))
else:
    print('deve escolher entre o numero 1 ou 2')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 07/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
A = int(input('escolha um conversor sendo 1-clima, 2-velocidade, 3-metros, 4-peso, 5-horas, 6-litros, 7-bytes. qual sua escolha?'))

if(A==1):
    AP = int(input('1 - Fahrenheit para celsius. 2 - Celsius para Fahrenheit. Qual a sua escolha?'))
    if (AP == 1):
        P = float(input('Fahrenheit para celsius:'))
        FP = 5.0*(P-32.0)/9.0
        print('sua resposta é {}'.format(FP))
    elif (AP == 2):
        CP = float(input('Celsius para Fahrenheit:'))
        CS =  CP *(9.0/5.0) + 32.0
        print('sua resposta é {}'.format(CS))
    else:
        print('você deve escolher entre 0 é 1')
elif(A==2):
    AS = int(input('1 - km/h -> m/s ou 2 - m/s -> km/h. Qual a sua escolha ?'))
    if(AS == 1):
        KP = float(input('insira a velocidade de KM/H para que possa ser convertida em M/S :'))
        MP =  KP / 3.6
        print('o resultado da conversão é {:.1f} m/s'.format(MP))
    elif(AS == 2):
        MS = float(input('insira a velociade em M/S para que possa ser convertido em KM/H :'))
        KS = MS * 3.6
        print('o resultado da conversão é {:.1f} Km/h'.format(KS))
    else:
        print('o numeros devem ser 1 - km/h -> m/s ou 2 - m/s -> km/h ')
elif(A==3):
    OP = int(input('insira 1- m² -> acres. ou 2- acres -> m². Qual a sua escolha?'))
    if(OP == 1):
        QP = float(input('insira m² para converter em acres :'))
        DP = QP * 0.000247
        print('{} acres'.format(DP))
    elif(O==2):
        wp = float(input('insira acres para converter em m² :'))
        ep = wp * 4048.58
        print('{} m²'.format(ep))
    else:
        print('deve escolher entre o numero 1 ou 2')
elif(A==4):
    RP= int(input('insira 1- Kg -> ton. ou 2- ton -> Kg. Qual a sua escolha?'))
    if(RP==1):
        RT = float(input('insira Kg para converter em ton :'))
        TT = RT /1000
        print('seu resultado é {}'.format(TT))
    elif(RP==2):
        rt = float(input('insira ton para converter em kg :'))
        tt = rt * 1000
        print('seu resultado é {}'.format(tt))
    else:
        print('tem que escolher entre o número 1 ou 2 :')
elif(A==5):
    WP = int(input('insira 1- horas -> min. ou 2- min -> horas. Qual a sua escolha'))
    if(WP==1):
        dd = float(input('insira horas para converter em min'))
        bb = dd*60
        print('seu resultado é {}'.format(bb))
    elif(WP==2):
        pp = float(input('insira min para converter em horas'))
        aa = pp/60 
        print('seu resultado é {}'.format(aa))
    else:
        print('tem que ser entre 1 ou 2')
elif(A==6):
    ll = int(input('insira 1-Litros -> militros. ou 2- militros -> litros. Qual a sua escolha'))
    if(ll==1):
        LD = float(input('insira Litros para converter em militros'))
        ld = LD * 1000
        print('seu resultado é {}'.format(ld))
    elif(ll==2):
        pa = float(input('insira militros para converter em litros'))
        Pa = pa / 1000
        print('seu resultado é {}'.format(Pa))
    else:
        print('tem que ser entre 1 ou 2')
elif(A==7):
    zz =  int(input('insira 1 - Bytes -> bits. ou 2 - bits -> bytes. Qual a sua escolha?'))
    if(zz==1):
        BY = int(input('insira Bytes para converter em bits: '))
        by = BY * 8
        print('sua resposta é {]'.format(by))
    elif(zz==2):
        BT = int(input('insira bits para converter Bytes: '))
        bt = BT/8
        print('sua resposta é {}'.format(bt))
    else:
        print('presisa ser 1 ou 2')
else:
    print('precisa ser um dos 7 números.')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 09/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
Faça a leitura de 10 valores e armazene em uma lista. Em seguida, 
o usuário deverá escolher qual variável estatística ele deseja visualizar:
Média, mediana, variância ou desvio padrão.
Apresente o resultado de acordo com a seleção feita pelo usuário.

import statistics as st
a1 = int(input('insira: '))
a2 = int(input('insira: '))
a3 = int(input('insira: '))
a4 = int(input('insira: '))
a5 = int(input('insira: '))
a6 = int(input('insira: '))
a7 = int(input('insira: '))
a8 = int(input('insira: '))
a9 = int(input('insira: '))
a10 = int(input('insira: '))

a11 = int(input('1-Média, 2-mediana, 3-variância ou 4-desvio padrão. Qual sua escolha? '))
if(a11==1):
  print(st.mean([a1,a2,a3,a4,a5,a6,a7,a8,a9,10]))
elif(a11==2):
  print(st.median([a1,a2,a3,a4,a5,a6,a7,a8,a9,10]))
elif(a11==3):
  print(st.variance([a1,a2,a3,a4,a5,a6,a7,a8,a9,10]))
elif(a11==4):
  print(st.stdev([a1,a2,a3,a4,a5,a6,a7,a8,a9,10]))
  
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                                 ATIVIDADE DIA- 20/04/21
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
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