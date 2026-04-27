import random



def checarLetra(tentativa,palavra_sorteada):
    return tentativa in palavra_sorteada



comidas = ['arroz','feijao','macarrao','pizza','hamburguer','sushi','lasanha','tapioca','cuscuz','salada','frango','carne','peixe','omelete',\
'panqueca','queijo','batata','cenoura','brocolis','abacaxi','banana','estrogonofe','laranja','sorvete','morango','chocolate','sorvete','bolo','biscoito','pastel']

# palavra_sorteada = random.choice(comidas)

palavra_sorteada = 'arroz'



rodando = True
vidas = 6
palavra_oculta= '_' * len(palavra_sorteada)

while vidas > 0:
    tentativa = input('Digite uma letra ou tente adivinhar a palavra:')
    checarLetra(tentativa,palavra_sorteada)
    if checarLetra == False:
        print ('Você errou, tente novamente.')
        vidas -= 1
    else:
        posicao = 0
        palavra_aux = ""
        while posicao < len(palavra_sorteada):
            if tentativa == palavra_sorteada[posicao]:
                palavra_aux += tentativa
                    
                posicao += 1
            else:
                palavra_aux += '_'
                posicao += 1

        palavra_oculta = palavra_aux


        

