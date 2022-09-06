input('======= Olá, Seja Bem vindo! =======\n \nAperte a tecla ENTER para continuar!!')

nInicial = int(input('Digite o número Inicial!\n'))
nFinal = int(input('Digite o número Final!\n'))
Incremento = int(input('Digite o Incremento!\n')) 
print()

if (nInicial >= nFinal):
    print('OPSSS !!!')
    print('Há um erro, seu número inicial deve ser maior que o número final!')

elif (Incremento <=0):
    print('ERRO!! Não foi possível executar essa operação...')
    print('Insira um número maior que zero!')

elif (Incremento >= nFinal):
    print('OPSSS !!!')
    print('Por favor, insira um número menor que o número final')

else:
    while (nInicial <= nFinal):
        print(nInicial)
        nInicial += Incremento
        restante = (nFinal - (nInicial - Incremento))
        
if (nInicial != nFinal):
    print('Falta' , restante ,'para concluir!')

print('FIM! ')

