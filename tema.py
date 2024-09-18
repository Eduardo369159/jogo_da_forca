class Temas():
    def escolha(self, num):
        listas = [
            [
                'Minecraft',
                'Fortnite',
                'Among Us',
                'Doom',
                'Portal'
            ],
            [
                'Tropa de Elite',
                'Cidade de Deus',
                'O Auto da Compadecida',
                'Minha Mae e uma Peca',
                'Se Eu Fosse Voce'
            ],
            [
                'Pele',
                'Anitta',
                'Ayrton Senna',
                'Taylor Swift',
                'Cristiano Ronaldo'
            ],
            [
                'Harry Potter',
                'Sherlock Holmes',
                'Darth Vader',
                'Homer Simpson',
                'James Bond'
            ],
            [
                'Garota de Ipanema',
                'Aquarela',
                'Mas Que Nada',
                'E Preciso Saber Viver',
                'O Mundo e um Moinho'
            ]
        ]
        return(listas[num-1])