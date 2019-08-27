habituado = 0 #Variável de controle (habituado ou não habituado)
animal_habituado = int(input("O ANIMAL ESTÁ HABITUADO? 0 -> NÃO | 1 -> SIM: "))

if animal_habituado == 0:
    print("ANIMAL AINDA NÃO HABITUADO... MANTER A HABITUAÇÃO...")
elif animal_habituado == 1:
    print("ANIMAL HABITUADO... INICIAR EXPERIMENTO...")
    habituado = 1
else: 
    print("COMANDO INVÁLIDO... TENTE NOVAMENTE...")

primeira_fase = 0 #Variável de controle (passou da primeira fase ou não)
if habituado == 1:
    comprimento_caixa = 30
    aproximacao_animal = float(input("QUANTOS CENTÍMETROS O ANIMAL SE APROXIMOU? "))
    
    if aproximacao_animal > 0 and aproximacao_animal <= comprimento_caixa:
        print("LIBERAR 0.5ML DE RECOMPENSA...")
        primeira_fase = 1
    elif aproximacao_animal == 0:
        print("NÃO LIBERAR RECOMPENSA...")
    else:
        print("VALOR INVÁLIDO...")