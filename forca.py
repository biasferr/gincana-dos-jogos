import random

def apenasLetras(tentativa):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for caractere in tentativa:
        if caractere not in alfabeto:
            return False
    return True



def desbloquearLetra(letra,palavra_oculta,palavra_sorteada):
    posicao = 0
    palavra_aux = ""
    while posicao < len(palavra_sorteada):
        if palavra_oculta[posicao] != '_':
            palavra_aux += palavra_oculta[posicao]  
        elif letra == palavra_sorteada[posicao]:
            palavra_aux += letra 
        else:
            palavra_aux += '_'
        posicao += 1
            
    return palavra_aux


#listas

comidas = ['arroz','feijao','churrasco','pizza','hamburguer','sushi','lasanha','tapioca','cuscuz','salada','frango','carne','peixe','omelete',\
'panqueca','queijo','batata','cenoura','brocolis','abacaxi','banana','strogonoff','laranja','sorvete','morango','chocolate','sorvete','bolo','biscoito','pastel']

# palavra_sorteada = random.choice(comidas)


#variaveis
jogando = True

while jogando == True:
    print ('--- FORCA ---')
    palavra_sorteada = random.choice(comidas)
    palavra_oculta= '_' * len(palavra_sorteada)
    vidas = 6
    rodando = True
    print (palavra_oculta)

    while rodando == True:
        if vidas == 0:
            print (f'Suas vidas acabaram! A palavra era: {palavra_sorteada}')
            rodando = False
        elif '_' not in palavra_oculta:
            print ('Você ganhou!')
            rodando = False
        else:
            tentativa = input('Digite uma letra ou tente acertar a palavra:')
            if apenasLetras(tentativa) == False:
                print ('Você deve digitar uma letra ou uma palavra.')
            elif len(tentativa) > 1:
                if tentativa == palavra_sorteada:
                    print ('Você acertou a palavra!')
                    rodando = False
                else:
                    vidas -= 1
                    print (f'Você errou a palavra, agora você tem {vidas} vidas.')
            else: 
                if tentativa in palavra_sorteada:
                    palavra_oculta = desbloquearLetra(tentativa,palavra_oculta,palavra_sorteada)
                    print ('Você acertou a letra!')
                    print (palavra_oculta)
                else:
                    vidas -= 1
                    print(f'Você errou a letra, agora você tem {vidas} vidas')

    print ('FIM DE JOGO')
                
    jogarDeNovo = (input('Deseja jogar novamente? (digite "S" ou "N"):'))
    if jogarDeNovo == 'N':
        jogando = False

