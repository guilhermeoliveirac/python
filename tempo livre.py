a1 = float(input('digite: '))
a2 = float(input('digite: '))


b= int(input('escolha uma opção: 1-Média, 2-mediana, 3-variância ou 4-desvio. Qual sua escolha? '))

if(b==1):
    s1 = (a1+a2)/2
    print(f'o resultado da média é {s1}')
elif(b==2):
    
    s2 = (a1,a2)
    s3 = sorted(s2)
    s4 = (a1+a2)/2
    print(f'o seu mediana é {s4}')
elif(b==3):
    s5 = (a1+a2)/2#
    s6 = (a1-s5)+(a2-s5)/2
    s7 = s6**2
    s8 = s7/2
    print(s8)
elif(b==4):
    from math import sqrt
    s5 = (a1+a2)/2#
    s6 = (a1-s5)+(a2-s5)/2
    s7 = s6**2
    s8 = s7/2
    s9 = sqrt(s8)
    print(s9)
else:
    print('os números devem ser entre 1,2,3 ou 4')