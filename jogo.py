print("-"*20)
print("---JOGO DE PEDRA, PAPEL E TESOURA (2 JOGADORES)---")
print("-"*20)
print("Bem vindos! Cada jogador deve escolher uma das opções:")
opcoes_validas=("Pedra","Papel","Tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("-"*50)

jogador1=input("Jogador 1, faça sua jogada:").capitalize().strip()
jogador2=input("Jogador 2, faça sua jogada:").capitalize().strip()

if jogador1 not in opcoes_validas or jogador2 not in opcoes_validas:
    print("Uma ou ambas jogadas são inválidas! Por favor, use apenas Pedra, papel ou tesoura.")
elif jogador1==jogador2:
    print("Empate")
elif (jogador1=="Tesoura" and jogador2=="Papel") or (jogador1=="Pedra" and jogador2=="Tesoura") or (jogador1=="Papel" and jogador2=="Pedra"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")

print("\n-----Fim de jogo!-----")