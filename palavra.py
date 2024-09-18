class Formatar():
    def palavra(self, palavra_escolhida, lista_ignorar):
        palavra = palavra_escolhida.lower().replace(' ','-')
        plv = palavra_escolhida.lower().replace(' ','')
        letras_ocultar = []
        for i in plv:
            letras_ocultar.append(i)
        lista = list(set(letras_ocultar))
        palavra_final = ''
        for i in palavra:
            if i in (lista) and i not in (lista_ignorar):
                palavra_final+='_'
            else:
                palavra_final+=i
        return(palavra_final)

