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

    # Adiciona um novo elemento no início da lista
    def addElementoNoInicio(self, valorQualquer):
        novo = self.criarNovoElemento(valorQualquer)
        novo.proximo = self.primeiro
        self.primeiro = novo

    # Adicionara um novo valor no meio da lista, de acordo com o valor de referência 
    def addElementoNoMeio(self, novoValor, ValorReferente):
        aux = self.primeiro
        while aux is not None:
            if aux.valor == ValorReferente:
                novo = self.criarNovoElemento(novoValor)
                novo.proximo = aux.proximo
                aux.proximo = novo
                return
            aux = aux.proximo    

#-----------------------------------------------------------------------------------------------------
# Essa parte remove os elementos 

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

    # Remove o primeiro elemento da lista
    def removeOPrimeiroElemento(self):
        if self.primeiro is None:
            return  # Lista vazia, nada a remover
        self.primeiro = self.primeiro.proximo

    def removeOelementoDoMeio(self, ValorReferente):  
        if self.primeiro is None:
            return  # Lista vazia
        if self.primeiro.valor == ValorReferente:
            self.primeiro = self.primeiro.proximo  # Caso especial: é o primeiro
            return
        aux = self.primeiro
        while aux is not None:
            if aux.proximo.valor == ValorReferente:
                aux.proximo = aux.proximo.proximo
                return
            aux = aux.proximo    

##------------------------------------------------##
## MAIN ##

#Criando uma lista VAZIA
minhaLista = Lista()

print("Lista inicial:")
minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)
minhaLista.addElementoNoFinal(94)
minhaLista.imprimeLista()


# Adicionando um elemento no início
minhaLista.addElementoNoInicio(90)
print("Após adicionar um novo elemento no inicio:")
minhaLista.imprimeLista()

## Removendo o último elemento
minhaLista.removeUltimoElemento()
print("Após remover o último elemento:")
minhaLista.imprimeLista()


# removendo o primeiro elemento
print("Após remover o primeiro elemento:")
minhaLista.removeOPrimeiroElemento()
minhaLista.imprimeLista()

# adiciona no meio
minhaLista.addElementoNoMeio(100, 92)
print("Após adicionar um novo elemento no meio:")
minhaLista.imprimeLista()

# Remove o elemento do meio desejado
minhaLista.removeOelementoDoMeio(92)
print("Após remover um elemento no meio:")
minhaLista.imprimeLista