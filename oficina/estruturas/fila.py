from .no import No


class FilaEncadeada:
    """Fila FIFO implementada com nós encadeados (sem usar list/deque)."""

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def enfileirar(self, dado):
        novo = No(dado)
        if self._fim is None:
            self._inicio = novo
        else:
            self._fim.proximo = novo
        self._fim = novo
        self._tamanho += 1

    def desenfileirar(self):
        """Remove e devolve o primeiro da fila (None se estiver vazia)."""
        if self._inicio is None:
            return None
        dado = self._inicio.dado
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return dado

    def primeiro(self):
        """Devolve o primeiro da fila sem removê-lo (None se estiver vazia)."""
        return None if self._inicio is None else self._inicio.dado

    def esta_vazia(self):
        return self._inicio is None

    def __len__(self):
        return self._tamanho

    def __iter__(self):
        """Percorre a fila do mais antigo ao mais novo sem destruí-la."""
        atual = self._inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo
