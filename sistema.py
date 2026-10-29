from .estruturas import FilaEncadeada
from .modelos import OrdemServico


class OficinaMecanica:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.fila_normal = FilaEncadeada()
        self.fila_guincho = FilaEncadeada()  # Fila prioritária
        self.ordens_abertas = []             # Só OS em andamento ficam na memória
        self.historico = []                  # Resumos leves das OS já fechadas
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

    # ------------------------------------------------------------------ atendimento
    def registrar_chegada(self, placa, queixa, via_guincho=False):
        cliente, veiculo = self.buscar_veiculo_por_placa(placa)
        if not veiculo:
            print(f"Erro: Veículo placa {placa} não encontrado.")
            return

        atendimento = {"cliente": cliente, "veiculo": veiculo, "queixa": queixa}
        if via_guincho:
            self.fila_guincho.enfileirar(atendimento)
            print(f"Veículo {placa} ({cliente.nome}) entrou na Fila PRIORITÁRIA (Guincho).")
        else:
            self.fila_normal.enfileirar(atendimento)
            print(f"Veículo {placa} ({cliente.nome}) entrou na Fila Normal.")

    def chamar_proximo(self):
        """Guincho tem prioridade sobre a fila normal."""
        if not self.fila_guincho.esta_vazia():
            return self.fila_guincho.desenfileirar()
        if not self.fila_normal.esta_vazia():
            return self.fila_normal.desenfileirar()
        return None

    def abrir_ordem_servico(self, atendimento, mecanico):
        os = OrdemServico(
            self._proximo_numero_os,
            atendimento["cliente"],
            atendimento["veiculo"],
            mecanico,
        )
        self._proximo_numero_os += 1
        self.ordens_abertas.append(os)
        return os

    # ------------------------------------------------------------------ fechamento
    def fechar_ordem_servico(self, os, forma_pagamento, parcelas=1):
        """Fecha a OS e libera memória: remove o carro, e o cliente se não restar nenhum carro."""
        total_pecas, total_servicos, total_geral = os.calcular_total()
        cliente, veiculo = os.cliente, os.veiculo

        print(f"\n--- FECHAMENTO DA OS #{os.numero_os} ---")
        print(f"Cliente: {cliente.nome} | Veículo: {veiculo.modelo} ({veiculo.placa})")
        print(f"Total Peças: R$ {total_pecas:.2f} | Total Mão de Obra: R$ {total_servicos:.2f}")
        print(f"Valor Total a Pagar: R$ {total_geral:.2f} via {forma_pagamento} (Parcelas: {parcelas})")

        os.status = "Fechada"

        # 1) guarda só um resumo leve e tira a OS completa da memória
        self.historico.append({
            "numero_os": os.numero_os,
            "cliente": cliente.nome,
            "placa": veiculo.placa,
            "total": total_geral,
            "pagamento": forma_pagamento,
        })
        self.ordens_abertas = [o for o in self.ordens_abertas if o is not os]

        # 2) remove o carro consertado do cliente
        cliente.remover_veiculo(veiculo.placa)
        print(f"Veículo {veiculo.placa} removido do cadastro do cliente.")

        # 3) sem mais carros, remove o cliente do sistema
        if not cliente.tem_veiculos():
            self.remover_cliente(cliente.cpf)
            print(f"Cliente {cliente.nome} sem veículos pendentes: removido do sistema.")
        else:
            restantes = ", ".join(v.placa for v in cliente.veiculos)
            print(f"Cliente {cliente.nome} continua cadastrado (veículos pendentes: {restantes}).")

    # ------------------------------------------------------------------ ordenação (sort)
    def clientes_ordenados(self):
        """Clientes em ordem alfabética (cópia; a lista original não muda)."""
        copia = self.clientes[:]
        copia.sort(key=lambda c: c.nome.lower())
        return copia

    def produtos_por_estoque(self):
        """Produtos do menor para o maior estoque (os mais críticos primeiro)."""
        copia = self.produtos[:]
        copia.sort(key=lambda p: p.quantidade_total())
        return copia

    def historico_ordenado(self, campo="total", decrescente=True):
        """Histórico de OS ordenado por um campo (ex.: 'total', 'cliente', 'numero_os')."""
        copia = self.historico[:]
        copia.sort(key=lambda h: h[campo], reverse=decrescente)
        return copia

    # ------------------------------------------------------------------ relatórios
    def alertas_estoque(self):
        return [p for p in self.produtos if p.abaixo_do_minimo()]

    def resumo(self):
        print(f"\n[Memória] Clientes ativos: {len(self.clientes)} | "
              f"OS abertas: {len(self.ordens_abertas)} | "
              f"OS no histórico: {len(self.historico)}")
