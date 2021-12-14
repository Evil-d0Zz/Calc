#!/bin/python3
# n3w.elf 
# contacts: irc.saude.gov.be

### Libs
from time import sleep
from os import system
import math

# tabela de Cores
R = "\033[1;31m"
Y = "\033[1;33m"
G = "\033[1;32m"
C = "\033[1;34m" # mto pika

# fundo 
while True:
  system('clear')
  print(f"""{C}
 ________________________
 +  .   {C}by: {G}n3w.elf{C}     +
 |   ▄───▄           .  |
 | █▀█▀█ .    .         |
 | █▄█▄█            .   |
 | ─███──▄▄     .       |
 | ─████▐█─█            |
 | ─████───█       .    |
 | ─▀▀▀▀▀▀▀    .        |
 |                  .   |
 | [{G}01{C}] - Multiplicaçao |
 | [{G}02{C}] - Subtraçao     |
 | [{G}03{C}] - Divisao       |
 | [{G}04{C}] - Adiçao        |
 | [{G}05{C}] - Raiz      .   |
 | [{G}06{C}] - Sair   .   .  |
 +______________________+
  """)

  try:
    cmd = int(input(f'[*] - {C}Escolha uma opçao:{G} '))
  except:
    print(f"{R}Apenas numeros!")
    exit()
    
  if cmd == 4:
    n1 = int(input(f'{C}Numero_1: {G}'))
    n2 = int(input(f'{C}Numero_2: {G}'))
    print(f"{C}Resultado da soma é: {G}{n1+n2}{C}")
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")
  
  elif cmd == 2:
    n1 = int(input('Numero_1: '))
    n2 = int(input('Numero_2: '))
    print(f"{C}Resultado da subtração é: {G}", n1-n2f, f"{C}")
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")

  elif cmd == 1:
    n1 = int(input('Numero_1: '))
    n2 = int(input('Numero_2: '))
    print(f"Resultado da multiplicação: {R}", n1*n2, f"{C}")
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")

  elif cmd == 3:
    n1 = int(input('Numero_1: '))
    n2 = int(input('Numero_2: '))
    print(f"Resultado da divisão: {R}", n1/n2, f"{C}")
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")

  elif cmd == 5:
    n1 = float(input('Numero_1: '))
    print("Resultado da raiz: ", math.sqrt(n1))
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")
  elif cmd == 6:
    print(f"{R}[!] - SAINDO....")
    sleep(2)
    exit()

  else:
    print(f"{RED}[!] - Opção Invalida! :(")
    exit()  
