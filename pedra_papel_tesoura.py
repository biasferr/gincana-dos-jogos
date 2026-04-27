import random 

def condicao_de_vitoria(jogada_usuario,jogada_computador):
    if (jogada_usuario == 'pedra' and jogada_computador == 'tesoura'):
        return True
    elif (jogada_usuario == 'tesoura' and jogada_computador == 'papel'): 
        return True
    elif (jogada_usuario == 'papel' and jogada_computador == 'pedra'):
        return True
    else:
        return False


jogadas_possiveis = ['pedra','papel','tesoura']

jogando = True
pontuação_jogador = 0
pontuação_comp = 0

while jogando == True:
    print ('--- PEDRA, PAPEL E TESOURA ---')


    jogada_usuario = input ('Qual é sua jogada?')
    if jogada_usuario not in jogadas_possiveis:
        print ('Você deve digitar "pedra", "papel" ou "tesoura"')
    else: 
        jogada_comp = random.choice(jogadas_possiveis)
        print (f'USUÁRIO: {jogada_usuario} X COMPUTADOR: {jogada_comp}')
        if jogada_comp == jogada_usuario:
            print ('Empate.')
        elif condicao_de_vitoria(jogada_usuario,jogada_comp) == True:
            print ('Vitória do usuário.')
            pontuação_jogador += 1
        elif condicao_de_vitoria(jogada_usuario,jogada_comp) == False:
            print ('Vitória do computador')
            pontuação_comp += 1

    print (f'Pontuação do usuário: {pontuação_jogador}')
    print (f'Pontuação do computador: {pontuação_comp}')    
    jogarDeNovo = input('Deseja jogar de novo? (Digite "s" ou "n"): ')
    if jogarDeNovo == 'n':
        jogando = False

    



