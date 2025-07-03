from Elemento import Elemento

class Lista:
    def __init__(self):
        self.primeiro = None

#fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def imprimeLista(self):
        aux = self.primeiro
        if(aux != None):
            while(aux != None):
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Lista Vazia ---")
            
    # Adiciona um novo elemento no final da lista
    def addElementoNoFinal(self, valorQualquer):
        aux = self.primeiro
        if(aux != None):
            # se nao for vazio JA TEM ELEMENTO
            while(aux.proximo != None):
                aux = aux.proximo
            # neste ponto o aux aponta para o ultimo elemento
            aux.proximo = self.criarNovoElemento(valorQualquer)
        else:
            # NAO TEM ELEMENTO
            self.primeiro = self.criarNovoElemento(valorQualquer)

    # Remove o último elemento da lista
    def removeUltimoElemento(self):
        if self.primeiro is None:
            return  # Lista vazia, nada a remover
        if self.primeiro.proximo is None:
            # Só tem um elemento
            self.primeiro = None
            return
        aux = self.primeiro
        while aux.proximo.proximo is not None:
            aux = aux.proximo
        aux.proximo = None
##------------------------------------------------##
## MAIN ##

#Criando uma lista VAZIA
minhaLista = Lista()

minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)

minhaLista.imprimeLista()

## Removendo o último elemento
minhaLista.removeUltimoElemento()

print("Após remover o último elemento:")
minhaLista.imprimeLista()