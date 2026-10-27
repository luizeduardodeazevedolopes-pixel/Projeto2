# ----------------------------------------------------
# NÓ E FILA (Controle de Fila e Estoque FIFO)
# ----------------------------------------------------
# Aqui a gente monta a estrutura do zero, sem usar listas prontas
# do Python para o controle principal.

class NoFila:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self):
        # Retorna True se a fila estiver zerada
        return self.inicio is None

    def enfileirar(self, dado):
        # Bota um novo item no final da fila
        novo_no = NoFila(dado)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self._tamanho += 1

    def desenfileirar(self):
        # Tira o primeiro cara da fila (FIFO)
        if self.esta_vazia():
            return None
        dado_removido = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1
        return dado_removido

    def tamanho(self):
        return self._tamanho
