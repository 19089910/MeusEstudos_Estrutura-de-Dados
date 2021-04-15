# Vetor Não Ordenado
"""

import numpy as np#biblioteca de numeros complexos

class VetorNaoOrdenado:#criando vetro para o nao ordenado
  def __init__(self, capacidade): #contrutor (parametro this,parametro capacidade maxima do vetor)
    self.capacidade = capacidade
    self.ultima_posicao = -1 #como 0(sem valor), mas o 0 na programacao tem valor 1*celula
    self.valores = np.empty(self.capacidade, dtype=float)#vetor tem que ter um tipo = float

  def imprime(self):
    if self.ultima_posicao == -1:#se a utima possisao for vazio(-1)
      print('O vetor está vazio')#imprime=
    else:
      for i in range(self.ultima_posicao + 1):#para i sera faichaDeApartir(celula 0)...i sera o vetor completa
        print(i, ' - ', self.valores[i])#imprima(celula,-,valor da celula)

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:#se capacidade foi atingida
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1 #inserir um nova celula
      self.valores[self.ultima_posicao] = valor #adiciona o valor na celula

  def pesquisar(self, valor):#valor que quer pesquisar
    for i in range(self.ultima_posicao + 1):#para i sera faichaDeApartir(celula 0)
      if valor == self.valores[i]:#se valor pesquisado = valor da celula
        return i#retornar celula do calor 
    return -1#nao encontrou em toda faichaDeApartir


  def excluir(self, valor):#dar o valor para apagar
    posicao = self.pesquisar(valor)#o seu lugar=pesquisa a celula do(valor a apagar)
    if posicao == -1:#nao achou
      return -1#imprime -1
    else:
      for i in range(posicao, self.ultima_posicao):para i sera faichaDeApartir(da posicao do valor a apagar ate a utima posicao do vetor)
        self.valores[i] = self.valores[i + 1]#valor da celula que estar na faichaDeApartir. = celula da frente...assim atribuindo o valor da celula da frente na celula que quer excluir o valor
      
      self.ultima_posicao -= 1#subitrair o utima posicao para nao deixa-la vazia
