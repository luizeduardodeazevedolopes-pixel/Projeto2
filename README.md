# 📦 Controle de Fila e Estoque (FIFO)

Este projeto contém a implementação de uma estrutura de dados do tipo **Fila Encadeada** (FIFO - *First-In, First-Out*), desenvolvida totalmente do zero em Python. 

O objetivo principal deste código é criar um sistema de controle de fila e estoque manual, sem utilizar as listas e bibliotecas embutidas do Python, atendendo a requisitos acadêmicos e focando no aprendizado de manipulação de nós na memória.

## 🛠️ Estrutura do Código

O projeto é construído a partir de duas classes principais:

- **`NoFila`**: Representa cada elemento individual (nó) da fila. Armazena o `dado` em si e uma referência (`proximo`) para o próximo elemento da fila.
- **`FilaEncadeada`**: É a estrutura controladora da fila. Mantém o rastreamento do primeiro elemento (`inicio`), do último elemento (`fim`) e da quantidade de itens armazenados (`_tamanho`).

## ⚙️ Métodos Disponíveis

A classe `FilaEncadeada` possui os seguintes métodos:

- `enfileirar(dado)`: Adiciona um novo item no final da fila.
- `desenfileirar()`: Remove e retorna o item que está no início da fila (obedecendo a regra de que o primeiro a entrar é o primeiro a sair). Retorna `None` se a fila estiver vazia.
- `esta_vazia()`: Retorna `True` se a fila estiver completamente vazia e `False` caso contrário.
- `tamanho()`: Retorna a quantidade exata de itens armazenados na fila no momento.

## 🚀 Como testar e usar

Veja um exemplo prático de como importar e utilizar a estrutura no seu código:

```python
# Instanciando a fila
fila = FilaEncadeada()

# Verificando se está vazia (deve retornar True)
print(f"Fila vazia? {fila.esta_vazia()}")

# Adicionando produtos ao estoque (Enfileirar)
fila.enfileirar("Produto A")
fila.enfileirar("Produto B")
fila.enfileirar("Produto C")

# Verificando o tamanho da fila (deve retornar 3)
print(f"Tamanho da fila: {fila.tamanho()}")

# Removendo o primeiro produto (Desenfileirar)
removido = fila.desenfileirar()
print(f"Atendendo / Removendo: {removido}") # Retorna "Produto A"

# Verificando o tamanho atualizado (deve retornar 2)
print(f"Tamanho da
