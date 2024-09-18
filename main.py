from os import system
from boneco import Evol
from time import sleep
from random import choice
from tema import Temas
from palavra import Formatar

ev = Evol()
tm = Temas()
frt = Formatar()

# deve ser escolhido um tema
# deve mostrar quantas letras e espaços tem na palavra
# ao acertar deve ser substiyuido os traços vazios pela letra
# ao errar o boneco deve começar a aparecer na forca (imagem)
# deve mostrar quais letras já foram erradas
# deixar a vista qual o tema escolhido

while True:
    print("""
    ==================================
        BEM-VINDO AO JOGO DA FORCA
    ==================================
             ==========
             ||//     |
             ||/     (_)
             ||      \\|/
             ||       |
             ||      / \\
             ||
           ======

    1. Iniciar Jogo
    2. Instruções
    3. Sair

    ==================================
    Escolha uma opção: 
        """)
    escolha = int(input('(Numero):'))

    if escolha == 3:
        system('cls')
        print('Obrigado por jogar')
        sleep(3)
        system('cls')
        break

    elif escolha == 2:
        system('cls')
        print("""
            O objetivo do jogo da forca é adivinhar uma palavra secreta, 
            escolhida pelo sistema, uma letra por vez, antes de cometer 
            erros suficientes para "enforcar" o boneco. O jogo começa mostrando 
            espaços em branco que representam as letras da palavra, e você 
            deve tentar adivinhar digitando uma letra de cada vez. Se a letra 
            estiver correta, ela será revelada nos espaços; se estiver errada, 
            uma parte do boneco será desenhada na forca. Você tem um número 
            limitado de erros, geralmente seis, para tentar adivinhar a palavra 
            completa antes que o boneco seja totalmente desenhado. Se adivinhar 
            a palavra antes de atingir o limite de erros, você vence. 
            Caso contrário, o jogo termina e a palavra correta será revelada.
        """)
        print()
        print('Presioce enter para voltar')
        input('')
        system('cls')

    elif escolha == 1:
        system('cls')
        print("""
            ==================================
                      ESCOLHA O TEMA!
            ==================================

            1. Games
            2. Filmes
            3. Famosos
            4. Personagens
            5. Musicas
              
            ==================================
            Escolha uma opção: 
        """)
        tema = int(input('(Numero):'))
        temas = ['Games','Filmes','Famosos','Personagens','Musicas']
        if tema <= 5 and tema >= 1:
            lista_escolhida = tm.escolha(tema)
            palavra_oculta = choice(lista_escolhida)
            erros = 0
            acertos = 0
            letras_erradas = []
            letras_corretas = []
            vencer = len(set(palavra_oculta.lower().replace(' ','')))
            letras = list(set(palavra_oculta.lower().replace(' ','')))
            while acertos < vencer:
                if erros < 6:
                    system('cls')
                    print(f'Tema: {temas[tema-1]}')
                    print()
                    print(ev.boneco(erros))
                    print()
                    print(f'Letras erradas: {letras_erradas}')
                    print()
                    print(frt.palavra(palavra_oculta, letras_corretas))
                    print()
                    print('Escolha uma letra:')
                    ltr = input('(letra):')
                    if ltr.lower() in letras_corretas:
                        pass
                    elif ltr.lower() in letras:
                        letras_corretas.append(ltr.lower())
                        acertos += 1
                    else:
                        letras_erradas.append(ltr.lower())
                        erros += 1
                else:
                    system('cls')
                    print(f'DESCULPE, MAS VOCÊ PERDEU, A PALAVRA ERA: {palavra_oculta.upper()}')
                    sleep(5)
                    system('cls')
                    break

            system('cls')
            print(f'PARABÉNS, VOCÊ VENCEU, A PALAVRA ERA: {palavra_oculta.upper()}')
            sleep(5)
            system('cls')

        else:
            system('cls')
            print('Você escolheu uma opção inexistente, tente novamente')
            sleep(3)
            system('cls')

    else:
        system('cls')
        print('Você escolheu uma opção não existente, tente de novo')
        sleep(3)
        system('cls')

