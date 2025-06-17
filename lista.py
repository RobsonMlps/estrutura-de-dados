from Elemento import Elemento

class Lista:
    def __init__(self):
        self.primeiro = None

#fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e
##------------------------------------------------##
## MAIN ##

#Criando uma lista VAZIA
minhaLista = Lista()

#Criando um elemento qualquer
e1 = minhaLista.criarNovoElemento(12)

#Adicionando um elemento à lista
minhaLista.primeiro = e1

#Testando o primeiro elemento da lista
print(minhaLista.primeiro.valor)


#Criando um elemento qualquer
minhaLista.primeiro.proximo = minhaLista.criarNovoElemento(23)

print(minhaLista.primeiro.proximo.valor)
