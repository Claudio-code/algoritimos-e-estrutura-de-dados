<h3 align="center">
    Algoritmos e estrutura de dados
</h3>


<a id="objetivo"></a>

## :bookmark: Objetivo

- Reaprendendo uma das materias da minha graduação e com certeza a mais importante hoje.
- Alem disso estou adicionando outros algoritmos que não foram ensinados mais que são tambem extremamente importantes.

# Índice

- [Objetivo](#objetivo)

- [Pilha](#pilha) :heavy_check_mark:
- [Fila](#fila) :heavy_check_mark:
- [Deque](#deque) :heavy_check_mark:
- [Fila de Prioridades](#fila_de_prioridades) :heavy_multiplication_x:
- [Disionario](#disionario) :heavy_multiplication_x:
- [Tabela Hash](#tabela_hash) :heavy_multiplication_x:
- [Heap Binaria](#heap_binaria) :heavy_multiplication_x:
- [Arvore Binaria de busca](#arvore_binaria) :heavy_check_mark:
- [Lista Ligada](#lista_ligada) :heavy_check_mark:
- [Grafos](#grafos) :heavy_multiplication_x:


<hr>

<a id="pilha"></a>
### :large_orange_diamond: Pilha

#### Conseito

- Adiciona dados no fim da pilha e remove dados no fim dela também ou onde o ultimo a entra é o primeiro a sair.
- Alem de funcionalidades extras como consultar o tamanho e o topo da pilha e se ela está vazia ou não.

<hr>

<a id="fila"></a>
### :boom: Fila

#### Conseito

- A fila é uma estrutura do tipo <b>FIFO</b> (first-in first-out), onde o primeiro elemento a ser inserido, será o primeiro a ser retirado, ou seja, adiciona-se itens no fim e remove-se itens no fim e remove-se do início.

#### Metodos implementados

- <b>Pop</b> remove do inicio da fila.
- <b>Push</b> adiciona no fim da fila.
- <b>Empty</b> verifica se fila esta vazia.
- <b>Length</b> verifica tamanho da fila.
- <b>Front</b> busca elemento que está no começo da fila.


<a id="deque"></a>
### :loop: Deque

#### Conseito

- Uma fila Duplamente Terminada (ou Deque) é um tipo abstrato de dado que organiza uma fila.
- Onde é posivel inserir e remover tanto do inicio como do fim.


#### Metodos implementados

- <b>Pop_front</b> remove do inicio da fila.
- <b>Pop_back</b> remove do fim da fila.
- <b>Push_back</b> adiciona no fim da fila.
- <b>Push_front</b> adiciona no inicio da fila.
- <b>Empty</b> verifica se fila esta vazia.
- <b>Front</b> busca elemento que está no começo da fila.
- <b>Back</b> busca elemento que está no fim da fila.

<a id="lista_ligada"></a>
### :couple: lista ligada

#### Conseito
- A lista ligada é basicamente um array de objetos onde um sempre sabe qual é o proximo

#### Metodos implementados
- <b>Pop</b> remove em qualquer lugar da lista.
- <b>Push</b> adiciona em qualquer lugar da lista.
- <b>Empty</b> verifica se a lista esta vazia.
- <b>Length</b> verifica tamanho da lista.
- <b>show</b> da print no conteudo da lista.

<a id="arvore_binaria"></a>
### :book: arvore binaria de busca

#### Conseito

- A arvore é baseada em nós onde cada um possui um idice e a posição de cada nó varia de a cordo com o valor do indice.
- Ex: o nó raiz é 89 vamos inserir o 92 como ele é maior nós o inserimos a direita, se formos inserir o 60 ele ficaria a esquerda e assim por diante.