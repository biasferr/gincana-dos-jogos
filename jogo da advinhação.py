#jogo da advinhação

import random


#escolher quem vai adivinhar:
print ('--- JOGO DA ADIVINHAÇÃO ---')
modo = int(input('Digite 1 se você deseja adivinhar um numero e 2 caso você deseje pensar em um número para o computador adivinhar:'))

if modo == 1:
    print ('Você escolheu adivinhar!')
    numero_sorteado = random.randint(1,1023)

    nTentativas = 1
    tentativa = int(input('Digite um número:'))


    while tentativa != numero_sorteado:
        if tentativa > numero_sorteado:
            print (-1)
        elif tentativa < numero_sorteado:
            print (1)
        tentativa = int(input('Digite um número:'))
        nTentativas += 1

    print (0)
    print (f'Você adivinhou o numero em {nTentativas} tentativas.')

elif modo == 2:
    print ('O computador vai adivinhar!')
    print ('Pense em um número de 1 a 1023')
    print ('Se o computador chutar um numero maior digite -1, se chutar um numero menor digite 1,\
se acertar digite 0.')
    resposta = ''

    chute = random.randint(1,1023)
    menorChute = 1
    maiorChute = 1023
    nTentativas = 1

    while resposta != '0':
        print (f'chute: {chute}')
        resposta = input('Digite -1, 1 ou 0:')
        if resposta not in '-1,1,0':
            print ('Digite uma resposta válida.')
        elif resposta == '-1':
            maiorChute = chute - 1
            chute = random.randint(menorChute, maiorChute )
            nTentativas += 1
        elif resposta == '1':
            menorChute = chute + 1
            chute = random.randint(menorChute,maiorChute)
            nTentativas += 1

    print (f'O computador adivinhou em {nTentativas} tentativas! O numero era {chute}.')

else: 
    print ('Você deve escolher um modo de jogo digitando 1 ou 2.')