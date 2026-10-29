from oficina import OficinaMecanica
from oficina.modelos import Cliente, Veiculo, LoteEstoque, ProdutoEstoque

oficina = OficinaMecanica()

# ---------------------------------------------------------------- funções auxiliares
def ler_numero(texto):
    """Lê um número decimal; pede de novo se o usuário digitar errado."""
    while True:
        try:
            return float(input(texto).replace(",", "."))
        except ValueError:
            print("Valor inválido, digite um número.")


def ler_inteiro(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Valor inválido, digite um número inteiro.")


def buscar_cliente(cpf):
    for c in oficina.clientes:
        if c.cpf == cpf:
            return c
    return None


def buscar_os(numero):
    for os in oficina.ordens_abertas:
        if os.numero_os == numero:
            return os
    return None


def buscar_produto(codigo):
    for p in oficina.produtos:
        if p.codigo.upper() == codigo.upper():
            return p
    return None


# ---------------------------------------------------------------- opções do menu
def cadastrar_cliente():
    print("\n--- Cadastrar cliente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    if buscar_cliente(cpf) is not None:
        print("Já existe um cliente com esse CPF.")
        return
    telefone = input("Telefone: ")
    oficina.cadastrar_cliente(Cliente(nome, cpf, telefone))
    print("Cliente cadastrado!")


def adicionar_veiculo():
    print("\n--- Adicionar veículo a um cliente ---")
    cliente = buscar_cliente(input("CPF do cliente: "))
    if cliente is None:
        print("Cliente não encontrado.")
        return
    placa = input("Placa: ")
    dono, _ = oficina.buscar_veiculo_por_placa(placa)
    if dono is not None:
        print("Essa placa já está cadastrada.")
        return
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    ano = ler_inteiro("Ano: ")
    cliente.adicionar_veiculo(Veiculo(placa, modelo, marca, ano))
    print(f"Veículo adicionado. {cliente.nome} agora tem {len(cliente.veiculos)} veículo(s).")


def listar_clientes():
    print("\n--- Clientes (ordem alfabética) ---")
    if len(oficina.clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return
    for c in oficina.clientes_ordenados():
        print(f"{c.nome} | CPF {c.cpf} | Tel {c.telefone}")
        for v in c.veiculos:
            print(f"    - {v.placa}: {v.marca} {v.modelo} ({v.ano})")


def cadastrar_produto():
    print("\n--- Cadastrar produto / lote ---")
    codigo = input("Código do produto: ")
    produto = buscar_produto(codigo)
    if produto is None:
        nome = input("Nome do produto: ")
        minimo = ler_inteiro("Estoque mínimo: ")
        produto = ProdutoEstoque(codigo, nome, minimo)
        oficina.cadastrar_produto(produto)
        print("Produto criado.")
    quantidade = ler_inteiro("Quantidade do lote: ")
    preco = ler_numero("Preço de compra (unidade): R$ ")
    produto.adicionar_lote(LoteEstoque(quantidade, preco))
    print(f"Lote adicionado. Estoque de {produto.nome}: {produto.quantidade_total()} un.")


def ver_estoque():
    print("\n--- Estoque (menor para maior) ---")
    if len(oficina.produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    for p in oficina.produtos_por_estoque():
        aviso = "  <-- ABAIXO DO MÍNIMO" if p.abaixo_do_minimo() else ""
        print(f"{p.codigo} | {p.nome} | {p.quantidade_total()} un. (mín. {p.minimo}){aviso}")


def registrar_chegada():
    print("\n--- Registrar chegada de veículo ---")
    placa = input("Placa: ")
    queixa = input("Queixa do cliente: ")
    guincho = input("Chegou de guincho? (s/n): ").lower() == "s"
    oficina.registrar_chegada(placa, queixa, via_guincho=guincho)


def chamar_proximo():
    print("\n--- Chamar próximo da fila ---")
    atendimento = oficina.chamar_proximo()
    if atendimento is None:
        print("Nenhum veículo na fila.")
        return
    mecanico = input("Nome do mecânico responsável: ")
    os = oficina.abrir_ordem_servico(atendimento, mecanico)
    print(f"OS #{os.numero_os} aberta para {atendimento['veiculo'].modelo} "
          f"({atendimento['veiculo'].placa}) de {atendimento['cliente'].nome}.")


def listar_os_abertas():
    print("\n--- Ordens de serviço abertas ---")
    if len(oficina.ordens_abertas) == 0:
        print("Nenhuma OS aberta.")
        return
    for os in oficina.ordens_abertas:
        _, _, total = os.calcular_total()
        print(f"OS #{os.numero_os} | {os.cliente.nome} | {os.veiculo.placa} | "
              f"Mecânico: {os.mecanico} | Total até agora: R$ {total:.2f}")


def adicionar_peca_ou_servico():
    print("\n--- Lançar peça ou serviço na OS ---")
    os = buscar_os(ler_inteiro("Número da OS: "))
    if os is None:
        print("OS não encontrada.")
        return
    tipo = input("Digite P para peça ou S para serviço: ").upper()
    if tipo == "P":
        nome = input("Nome da peça: ")
        valor = ler_numero("Valor: R$ ")
        codigo = input("Código no estoque para dar baixa (Enter para pular): ")
        if codigo != "":
            produto = buscar_produto(codigo)
            if produto is None:
                print("Produto não encontrado no estoque; peça lançada sem baixa.")
            elif produto.retirar(1):
                print(f"Baixa de 1 un. de {produto.nome} (FIFO).")
            else:
                print("Estoque insuficiente; peça lançada sem baixa.")
        os.adicionar_peca(nome, valor)
        print("Peça lançada.")
    elif tipo == "S":
        descricao = input("Descrição do serviço: ")
        valor = ler_numero("Valor: R$ ")
        os.adicionar_servico(descricao, valor)
        print("Serviço lançado.")
    else:
        print("Opção inválida.")


def fechar_os():
    print("\n--- Fechar ordem de serviço ---")
    os = buscar_os(ler_inteiro("Número da OS: "))
    if os is None:
        print("OS não encontrada.")
        return
    forma = input("Forma de pagamento: ")
    parcelas = ler_inteiro("Parcelas: ")
    oficina.fechar_ordem_servico(os, forma, parcelas)


def ver_historico():
    print("\n--- Histórico de OS fechadas (maior valor primeiro) ---")
    if len(oficina.historico) == 0:
        print("Nenhuma OS fechada ainda.")
        return
    for h in oficina.historico_ordenado("total"):
        print(f"OS #{h['numero_os']} | {h['cliente']} | {h['placa']} | "
              f"R$ {h['total']:.2f} | {h['pagamento']}")


# ---------------------------------------------------------------- menu principal
def mostrar_menu():
    print("\n==============================")
    print("      OFICINA MECÂNICA")
    print("==============================")
    print(" 1 - Cadastrar cliente")
    print(" 2 - Adicionar veículo a um cliente")
    print(" 3 - Listar clientes e veículos")
    print(" 4 - Cadastrar produto / lote no estoque")
    print(" 5 - Ver estoque")
    print(" 6 - Registrar chegada de veículo")
    print(" 7 - Chamar próximo da fila (abre OS)")
    print(" 8 - Listar OS abertas")
    print(" 9 - Lançar peça ou serviço na OS")
    print("10 - Fechar OS")
    print("11 - Ver histórico de OS fechadas")
    print(" 0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            adicionar_veiculo()
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            cadastrar_produto()
        elif opcao == "5":
            ver_estoque()
        elif opcao == "6":
            registrar_chegada()
        elif opcao == "7":
            chamar_proximo()
        elif opcao == "8":
            listar_os_abertas()
        elif opcao == "9":
            adicionar_peca_ou_servico()
        elif opcao == "10":
            fechar_os()
        elif opcao == "11":
            ver_historico()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
