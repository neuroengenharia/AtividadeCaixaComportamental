animal_habituado = int(input("O ANIMAL ESTÁ HABITUADO? 0 -> NÃO | 1 -> SIM: "))

if animal_habituado == 0:
    print("ANIMAL AINDA NÃO HABITUADO... MANTER A HABITUAÇÃO...")
elif animal_habituado == 1:
    print("ANIMAL HABITUADO... INICIAR EXPERIMENTO...")
    habituado = 1
else: 
    print("COMANDO INVÁLIDO... TENTE NOVAMENTE...")
