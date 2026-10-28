# 📦 Controle de Fila e Estoque (FIFO)

Este projeto contém a implementação de uma estrutura de dados do tipo **Fila Encadeada** (FIFO - *First-In, First-Out*), desenvolvida totalmente do zero em Python, integrada a um sistema de controle de lotes e produtos. 

O objetivo principal deste código é criar um sistema de controle de estoque manual, sem utilizar as listas e bibliotecas embutidas do Python para a fila, atendendo a requisitos acadêmicos e focando no aprendizado de manipulação de nós na memória e lógica de negócios.

## 🛠️ Estrutura do Código

O projeto é construído a partir de estruturas de controle de dados e classes de domínio:

- **`NoFila`**: Representa cada elemento individual (nó) da fila. Armazena o `dado` em si e uma referência (`proximo`) para o próximo elemento.
- **`FilaEncadeada`**: É a estrutura controladora da fila. Mantém o rastreamento do primeiro elemento (`inicio`), do último elemento (`fim`) e da quantidade de itens armazenados.
- **`LoteEstoque`**: Representa um lote individual de produtos, armazenando `quantidade`, `preco_compra` e `data_validade`.
- **`ProdutoEstoque`**: Gerencia um produto específico e seus lotes organizados em formato de fila (garantindo o consumo via FIFO: o lote mais antigo sai primeiro).

## ⚙️ Métodos Disponíveis

### `FilaEncadeada`
- `enfileirar(dado)`: Adiciona um novo item no final da fila.
- `desenfileirar()`: Remove e retorna o item que está no início da fila. Retorna `None` se a fila estiver vazia.
- `esta_vazia()`: Retorna `True` se a fila estiver completamente vazia e `False` caso contrário.
- `tamanho()`: Retorna a quantidade exata de itens armazenados na fila no momento.

### `ProdutoEstoque`
- `adicionar_lote(lote)`: Enfileira um novo lote de mercadorias.
- `quantidade_total()`: Soma o estoque total percorrendo a fila sem destruí-la.
- `abaixo_do_minimo()`: Verifica se o estoque atual está abaixo do limite mínimo configurado.
- `retirar(quantidade)`: Dá baixa no estoque seguindo estritamente a ordem FIFO entre os lotes. Retorna `False` se não houver saldo suficiente.

## 🚀 Como testar e usar

Veja um exemplo prático de como importar e utilizar a estrutura de fila e controle de estoque:

```python
# Instanciando a fila básica
fila = FilaEncadeada()

# Verificando se está vazia (deve retornar True)
print(f"Fila vazia? {fila.esta_vazia()}")

# Adicionando itens (Enfileirar)
fila.enfileirar("Produto A")
fila.enfileirar("Produto B")

# Removendo o primeiro item (Desenfileirar)
removido = fila.desenfileirar()
print(f"Atendendo / Removendo: {removido}") # Retorna "Produto A"
