#Uma calculadora simples para exercitar meu conhecimento
def Calculadora():
    #conta = Calculadora()
    calculo = int(input(
        'Escolha qual o calculo quer fazer: / (1) - Somar / (2)- subtrair/ (3)- multiplicar/ (4) - dividir. (5)- SAIR: '
        ))
    if calculo == 1:
        n1 = int(input('primeiro número: '))
        n2 = int(input('segundo número: '))
        n3 = n1 + n2
        print(f'Ótimo o resultado é: {n3}' )
        n4 = int(input(' vamos continuar (1) sim / (2) não: '))
        if n4 == 1:
            Calculadora()
        else:
            print('bye, bye')
        

    elif calculo == 2:
        n1 = int(input('primeiro número: '))
        n2 = int(input('segundo número: '))
        n3 = n1 - n2
        print(f'Ótimo o resultado é: {n3}')
        n4= int(input('Vamos continuar (1) sim / (2) não: '))
        if n4 == '1':
            Calculadora()
        else:
            print('bye, bye')

    elif calculo == 3:
        n1 = int(input('primeiro número: '))
        n2 = int(input('segundo número: '))
        n3 = n1 * n2
        print(f'Ótimo o resultado é: {n3}')
        n4= int(input(' vamos continuar (1) sim / (2) não: '))
        if n4 == 1:
            Calculadora()
        else:
            print('bye, bye')  

    elif calculo == 4:
        n1 = int(input('primeiro número: '))
        n2 = int(input('segundo número: '))
        n3 = n1 / n2
        print(f'Ótimo o resultado é: {n3}')
        n4= int(input(' vamos continuar (1) sim / (2) não: : '))
        if n4 == 1:
            Calculadora()
        else:
            print('bye, bye')
    
    elif calculo == 5:
        print('Obrigador, até mais ver!:<3 -_- <3')

    else:
        n1 = int(input('primeiro número: '))
        n2 = int(input('segundo número: '))
        print('Escolha uma opção de 1 a 4')
        

Calculadora()
