habituado = 0 #Variável de controle (habituado ou não habituado)
animal_habituado = 0 

while animal_habituado != 1:
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
    aproximacao_animal = 0
    while not(aproximacao_animal > 0 and aproximacao_animal <= comprimento_caixa):

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
    contador_barra = 20
    contador_toques = 0
    while contador_barra > 0:
        toque_barra = float(input("O ANIMAL TOCOU NA BARRA? "))
        if toque_barra == 1:
            contador_barra = contador_barra - 1
            contador_toques = contador_toques + 1
            print("0/ Toque: ", contador_toques)
    segundo_controle = 1 
    print("PASSOU PARA A PROXIMA ETAPA DO EXPERIMENTO...")

terceiro_controle = 0 #Variável de controle (passou desta etapa ou não)
quantidade_experimentos = 5 #Digite a quantidade de experimentos
if  segundo_controle == 1: #Se passou pela etapa anterior
    while quantidade_experimentos > 0:
        print("Suas opções de som e barra: ")
        print("1-Som 1: Phi")
        print("2-Som 2: Trill")
        print("3-Barra direita")
        print("4-Barra esquerda")
        som = int(input("Digite o som reproduzido: "))
        Barra = int(input("Qual barra foi tocada: "))
        if som == 1 and Barra == 4:
            print("LIBERAR 0.5ML DE RECOMPENSA...")
            terceiro_controle = 1
        elif som == 2 and Barra == 3:
            print("LIBERAR 0.5ML DE RECOMPENSA...")
            terceiro_controle = 1
        else:
            print("Repetir o teste até que seja descriminado som e barra.")
        quantidade_experimentos = quantidade_experimentos - 1

#Verificando se o experimento foi realizado 50x no intervalo de 30' e, conseguiu atingir o percentual mínimo de acertos
if terceiro_controle == 1:
    quantVezesMinuto = int(input("O EXPERIMENTO FOI REALIZADO 50x EM 30 MINUTOS? 0 -> NÃO | 1 -> SIM:"))
    porcentagem_acerto = float(input("QUAL FOI A PORCENTAGEM DE ACERTO? (PERCENTUAL MÍNIMO DE 62%) "))
    #Se fez o total de experimentos no tempo limite e obteve o percentual minimo, passa para a próxima etapa.
    if quantVezesMinuto == 1 and porcentagem_acerto >= 62.0 and porcentagem_acerto <= 100.0:
        print("PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...")
    else: #Se as condições anteriores não foram satisfeitas, não passa para a proxima etapa.
        print("AINDA NÃO PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO. CONTINUE TREINANDO O ANIMAL...")