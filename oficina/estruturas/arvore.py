class NoArvore:
    """Nó de uma árvore N-ária de diagnóstico (componentes do veículo)."""

    def __init__(self, nome, codigo_peca=None, estado="OK"):
        self.nome = nome
        self.codigo_peca = codigo_peca
        self.estado = estado  # "OK" ou "Com defeito"
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)
        return filho

    def exibir_pre_ordem(self, nivel=0):
        """Imprime a árvore em pré-ordem, com recuo por nível."""
        marcador = "" if self.estado == "OK" else f" [{self.estado}]"
        peca = f" (peça {self.codigo_peca})" if self.codigo_peca else ""
        print("  " * nivel + f"- {self.nome}{peca}{marcador}")
        for filho in self.filhos:
            filho.exibir_pre_ordem(nivel + 1)

    def buscar_defeitos(self):
        """Devolve a lista de nós com defeito (percorre a árvore toda)."""
        defeitos = []
        if self.estado == "Com defeito":
            defeitos.append(self)
        for filho in self.filhos:
            defeitos.extend(filho.buscar_defeitos())
        return defeitos
