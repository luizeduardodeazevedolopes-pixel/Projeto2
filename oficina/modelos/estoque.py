from ..estruturas import FilaEncadeada


class LoteEstoque:
    def __init__(self, quantidade, preco_compra, data_validade=None):
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.data_validade = data_validade  # Ex: "2026-12-31" ou None


class ProdutoEstoque:
    """Produto com lotes organizados em fila (FIFO: o lote mais antigo sai primeiro)."""

    def __init__(self, codigo, nome, minimo=5):
        self.codigo = codigo
        self.nome = nome
        self.minimo = minimo
        self.lotes = FilaEncadeada()

    def adicionar_lote(self, lote):
        self.lotes.enfileirar(lote)

    def quantidade_total(self):
        """Soma o estoque total percorrendo a fila sem destruí-la."""
        return sum(lote.quantidade for lote in self.lotes)

    def abaixo_do_minimo(self):
        return self.quantidade_total() < self.minimo

    def retirar(self, quantidade):
        """Retira unidades seguindo FIFO. Retorna False se não houver estoque suficiente."""
        if quantidade > self.quantidade_total():
            return False
        restante = quantidade
        while restante > 0:
            lote = self.lotes.primeiro()
            if lote.quantidade <= restante:
                restante -= lote.quantidade
                self.lotes.desenfileirar()  # lote esgotado
            else:
                lote.quantidade -= restante
                restante = 0
        return True
