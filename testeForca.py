

palavra = 'amor'


palavra_oculta= '_' * len(palavra)
letra = input('letra:')
posicao = 0

palavra_aux = ""
while posicao < len(palavra):
    if letra == palavra[posicao]:
        palavra_aux += letra 
        
        posicao += 1
    else:
        palavra_aux += '_'
        posicao += 1

palavra_oculta = palavra_aux

print (palavra_oculta)