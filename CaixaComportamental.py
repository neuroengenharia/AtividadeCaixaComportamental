habituado = 0 #Variável de controle (habituado ou não habituado)
animal_habituado = int(input("O ANIMAL ESTÁ HABITUADO? 0 -> NÃO | 1 -> SIM: "))

if animal_habituado == 0:
    print("ANIMAL AINDA NÃO HABITUADO... MANTER A HABITUAÇÃO...")
elif animal_habituado == 1:
    print("ANIMAL HABITUADO... INICIAR EXPERIMENTO...")
    habituado = 1
else: 
    print("COMANDO INVÁLIDO... TENTE NOVAMENTE...")

primeiro_controle = 0 #Variável de controle (passou desta etapa ou não)
if habituado == 1:
    comprimento_caixa = 30
    aproximacao_animal = float(input("QUANTOS CENTÍMETROS O ANIMAL SE APROXIMOU? "))
    
    if aproximacao_animal > 0 and aproximacao_animal <= comprimento_caixa:
        print("LIBERAR 0.5ML DE RECOMPENSA...")
        primeiro_controle = 1 #Passou
    elif aproximacao_animal == 0:
        print("NÃO LIBERAR RECOMPENSA...")
    else:
        print("VALOR INVÁLIDO...")

segundo_controle = 0 #Variável de controle (passou desta etapa ou não)
if primeiro_controle == 1: #Se passou pela etapa anterior
    toques_barra = int(input("O ANIMAL TOCOU 20 VEZES NA BARRA? 0 -> NÃO | 1 -> SIM: "))
    if toques_barra == 0:
        print("AINDA NÃO PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO. CONTINUE TREINANDO O ANIMAL...")
    elif toques_barra == 1:
        print("PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...")
        segundo_controle = 1 #Passou
    else: 
        print("COMANDO INVÁLIDO...")

terceiro_controle = 0 #Variável de controle (passou desta etapa ou não)
if  primeiro_controle == 1: #Se passou pela etapa anterior        
        print('Suas opções de som e barra: ')
        print('1-Som 1: Phi')
        print('2-Som 2: Trill')
        print('3-Barra direita')
        print('4-Barra esquerda')
        som = int(input('Digite o som reproduzido: '))
        Barra = int(input('Qual barra foi tocada: '))
        if som == 1 and Barra == 4:
            print('Recompensa liberada!')
            print('PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...')
        elif som == 2 and Barra == 3:
            print('Recompensa liberada!')
            print('PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...')
        else:
            print('Repetir o teste até que seja descriminado o som/barra.')

