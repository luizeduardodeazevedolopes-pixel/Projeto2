class OficinaMecanica:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.fila_normal = FilaEncadeada()
        self.fila_guincho = FilaEncadeada()  # Fila prioritária
        self.ordens_abertas = []             # Só OS em andamento ficam na memória
        self.historico = []                  # Resumos das OS já fechadas
        self._proximo_numero_os = 1

    # ------------------------------------------------------------------ cadastros
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def remover_cliente(self, cpf):
        self.clientes = [c for c in self.clientes if c.cpf != cpf]

    def buscar_veiculo_por_placa(self, placa):
        for cliente in self.clientes:
            for veiculo in cliente.veiculos:
                if veiculo.placa.upper() == placa.upper():
                    return cliente, veiculo
        return None, None
