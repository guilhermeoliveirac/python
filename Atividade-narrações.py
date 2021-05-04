#########################################################################################
                                Atividade
#########################################################################################
1-Faça um fluxograma/narração que descreve a 
leitura de três valores positivos e imprima a 
soma deles.

A = int(input('digite:'))
B = int(input('digite:'))
C = int(input('digite:'))
soma = A+B+C
if(A>=0 and B>=0 and C>=0):
    print('a some de {} + {} = {}'.format(A,B,C,soma))
else:
    print('precisa ser numero positivo')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
2)Faça um fluxograma/narração que descreve o cálculo da média final de
um aluno que realizou três provas no semestre. É considerado “aprovado”
se a média for igual ou superior a 7,00, senão “reprovado”.

A = float(input('digite:'))
B = float(input('digite:'))
C = float(input('digite:'))

media = (A +B + C) / 3
if (media >= 7):
    print('aprovado')
elif (media <7):
    print('reprovado')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
3)Faça um fluxograma/narração que leia um número inteiro e imprima o seu
antecessor e o seu sucessor.

A = int(input('coloque um número'))

me = (A - 1)
ma = (A + 1)

print('o seu antecessor é {}, já o seu sucessor é {}'.format(me, ma))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
4)Faça um fluxograma/narração que leia dois números e mostre o maior. Se
os dois números forem iguais, imprima a mensagem “Números iguais”.

A = int(input('insira:'))
B = int(input('insira:'))

if (A > B):
    print('{} maior'.format(A))
elif (A < B):
    print('{} menor'.format(B))
else:
    print('números iguais')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
5)Faça um fluxograma/narração que leia 3 números e informe qual o maior
entre eles. Se os três números forem iguais, imprima a mensagem
“Números iguais”.

A = int(input('insira:'))
B = int(input('insira:'))
C = int(input('insira:'))

if(A > B):
    print('o maior entre eles é {}'.format(A))
elif(B > C):
    print('o maior é {}'.format(B))
elif(C > B):
    print('o maior {}'.format(C))

elif(A == B == C):
    print('numeros iguais')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
6)Faça um fluxograma/narração que leia um número diferente de zero e
diga se este número é positivo ou negativo

A = int(input('insira:'))

if(A > 0):
    print('positivo')
elif(A < 0):
    print('negativo')
elif(A == 0):
    print('coloque um número maior que zero')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
7)Faça um fluxograma/narração que leia um número inteiro positivo. Se o
número for maior que 10, imprima o número ao quadrado. Senão, imprima
o número ao cubo.

A = int(input('insira:'))
if(A > 10):
    print('sua resposta é {}'.format(A**2))
else:
    print('sua respostas é {}'.format(A**3))
    

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
8)Faça um fluxograma/narração que leia um número real. Se o número for
positivo imprima a raiz quadrada. Caso contrário, imprima o número ao
quadrado.


from math import sqrt, trunc
A = int(input('insira:'))
R = (sqrt(A))
if( A > 0):
    print('o resultado é {}'.format(trunc(R)))
else:
    print('o resultado é {}'.format(A**2))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
9)Faça um fluxograma/narração que leia um número inteiro e verifique se
este número é par ou ímpar.

A = float(input('insira:'))
B =  A % 2
from math import trunc

if(B == 0):
    print('seu numero {} é par'.format(trunc(A)))
else:
    print('seu número {} é impar'.format(trunc(A)))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
10)Faça um fluxograma/narração que leia o salário de um trabalhador e o
valor da parcela de um empréstimo. Se a parcela for maior que 20% do
salário, imprima: “Empréstimo não concedido”. Caso contrário, imprima
“Empréstimo concedido”.

salario = float(input('isira seu salario:'))
emprestimo = int(input('insira su emprestimo'))
resultado = emprestimo >(salario * 2) 
if(salario > 1.100 and emprestimo > 1):
    print('aprovado')
else:
    print('reprovado')


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

