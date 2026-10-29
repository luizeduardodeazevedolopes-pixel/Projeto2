class Cliente:
    """Cliente da oficina. Pode ter vários veículos ao mesmo tempo."""

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, placa):
        """Remove o veículo da lista do cliente após a finalização do conserto."""
        self.veiculos = [v for v in self.veiculos if v.placa.upper() != placa.upper()]

    def tem_veiculos(self):
        return len(self.veiculos) > 0
