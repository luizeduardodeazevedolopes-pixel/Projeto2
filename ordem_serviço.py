class OrdemServico:
    def __init__(self, numero_os, cliente, veiculo, mecanico):
        self.numero_os = numero_os
        self.cliente = cliente
        self.veiculo = veiculo
        self.mecanico = mecanico
        self.pecas_utilizadas = []
        self.servicos_realizados = []
        self.status = "Aberta"  # "Aberta" ou "Fechada"

    def adicionar_peca(self, nome_peca, valor):
        self.pecas_utilizadas.append({"nome": nome_peca, "valor": valor})

    def adicionar_servico(self, descricao, valor):
        self.servicos_realizados.append({"descricao": descricao, "valor": valor})

    def calcular_total(self):
        total_pecas = sum(p["valor"] for p in self.pecas_utilizadas)
        total_servicos = sum(s["valor"] for s in self.servicos_realizados)
        return total_pecas, total_servicos, total_pecas + total_servicos
