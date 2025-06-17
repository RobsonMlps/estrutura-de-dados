class Elemento:

    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

    def lacoDoFimDoMundo(self):
        while(self.proximo != None):
            print(self.valor)
            self = self.proximo

## MAIN ##
'''elemento1 = Elemento(91,None)
elemento2 = Elemento(92,None)
elemento3 = Elemento(93,None)

print(elemento1.valor)
print(elemento2.valor)
print(elemento3.valor)

elemento1.proximo = elemento2
elemento2.proximo = elemento3
elemento3.proximo = elemento1

print("---------------------")
print(elemento2.proximo.valor)
print(elemento1.proximo.proximo.proximo.valor)
print("---------------------")
print("---------------------")
elemento1.lacoDoFimDoMundo()'''