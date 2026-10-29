from oficina import OficinaMecanica
from oficina.estruturas import NoArvore
from oficina.modelos import Cliente, Veiculo, LoteEstoque, ProdutoEstoque


def main():
    oficina = OficinaMecanica()

    # 1. Clientes e veículos (um cliente pode ter vários carros)
    c1 = Cliente("Carlos Eduardo", "123.456.789-00", "(19) 99111-2233")
    c1.adicionar_veiculo(Veiculo("ABC-1234", "Civic", "Honda", 2019))
    c1.adicionar_veiculo(Veiculo("DEF-5678", "Corolla", "Toyota", 2021))

    c2 = Cliente("Marina Souza", "987.654.321-00", "(19) 98888-7766")
    c2.adicionar_veiculo(Veiculo("GHI-9012", "Gol", "Volkswagen", 2015))

    oficina.cadastrar_cliente(c2)
    oficina.cadastrar_cliente(c1)
    oficina.resumo()

    print("\nClientes em ordem alfabética:")
    for c in oficina.clientes_ordenados():
        print(f"  - {c.nome} ({len(c.veiculos)} veículo(s))")

    # 2. Estoque com lotes (FIFO)
    pastilha = ProdutoEstoque("P001", "Pastilha de freio", minimo=5)
    pastilha.adicionar_lote(LoteEstoque(4, 35.00))
    pastilha.adicionar_lote(LoteEstoque(6, 38.50))
    oficina.cadastrar_produto(pastilha)
    print(f"\nEstoque de {pastilha.nome}: {pastilha.quantidade_total()} un.")
    pastilha.retirar(5)  # consome o lote mais antigo primeiro
    print(f"Após retirar 5: {pastilha.quantidade_total()} un.")
    for produto in oficina.alertas_estoque():
        print(f"ALERTA: {produto.nome} abaixo do mínimo ({produto.minimo}).")

    # 3. Chegadas: o guincho passa na frente
    print()
    oficina.registrar_chegada("ABC-1234", "Barulho no freio")
    oficina.registrar_chegada("GHI-9012", "Não liga", via_guincho=True)
    oficina.registrar_chegada("DEF-5678", "Revisão dos 40 mil km")

    # 4. Diagnóstico em árvore N-ária
    motor = NoArvore("Carro")
    freios = motor.adicionar_filho(NoArvore("Sistema de freios"))
    freios.adicionar_filho(NoArvore("Pastilhas", codigo_peca="P001", estado="Com defeito"))
    freios.adicionar_filho(NoArvore("Discos"))
    motor.adicionar_filho(NoArvore("Bateria", codigo_peca="B010", estado="Com defeito"))
    print("\nDiagnóstico:")
    motor.exibir_pre_ordem()
    print("Defeitos encontrados:", ", ".join(n.nome for n in motor.buscar_defeitos()))

    # 5. Atendimento: atende todos os carros e fecha as OS
    pagamentos = {"GHI-9012": ("Pix", 1), "ABC-1234": ("Cartão", 3), "DEF-5678": ("Dinheiro", 1)}
    mao_de_obra = {"GHI-9012": 300.00, "ABC-1234": 200.00, "DEF-5678": 450.00}
    while True:
        atendimento = oficina.chamar_proximo()
        if atendimento is None:
            break
        veiculo = atendimento["veiculo"]
        print(f"\nAtendendo {veiculo.modelo} ({veiculo.placa}) - queixa: {atendimento['queixa']}")
        os = oficina.abrir_ordem_servico(atendimento, mecanico="João")
        os.adicionar_peca("Peça de reposição", 150.00)
        os.adicionar_servico(atendimento["queixa"], mao_de_obra[veiculo.placa])
        forma, parcelas = pagamentos[veiculo.placa]
        oficina.fechar_ordem_servico(os, forma, parcelas)
        oficina.resumo()

    # 6. Relatório com sort: OS fechadas da mais cara para a mais barata
    print("\nHistórico ordenado por valor (maior -> menor):")
    for h in oficina.historico_ordenado("total"):
        print(f"  OS #{h['numero_os']} | {h['cliente']} | {h['placa']} | R$ {h['total']:.2f}")


if __name__ == "__main__":
    main()
