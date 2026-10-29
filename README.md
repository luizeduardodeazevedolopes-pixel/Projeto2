# 🔧 Oficina Mecânica

Sistema de gerenciamento de oficina em Python, com estruturas de dados implementadas do zero.

## Funcionalidades

- **Clientes com vários veículos**: um cliente pode ter vários carros cadastrados ao mesmo tempo.
- **Economia de memória**: ao fechar a OS, o carro consertado é removido do cliente; quando o cliente fica sem carros, ele também é removido do sistema. A OS completa sai da memória e fica só um resumo leve no histórico.
- **Filas encadeadas (FIFO)**: fila normal e fila prioritária para veículos chegados de guincho.
- **Estoque por lotes (FIFO)**: o lote mais antigo é consumido primeiro, com alerta de estoque mínimo.
- **Árvore N-ária de diagnóstico**: componentes do veículo, com busca de peças defeituosas.
- **Ordem de Serviço**: peças, mão de obra, total e forma de pagamento.

## Estrutura do projeto

```
oficina-mecanica/
├── menu.py                    # menu interativo no terminal
├── main.py                    # simulação automática de demonstração
└── oficina/
    ├── sistema.py             # OficinaMecanica (regras de negócio)
    ├── estruturas/
    │   ├── no.py              # nó encadeado
    │   ├── fila.py            # FilaEncadeada (FIFO)
    │   └── arvore.py          # NoArvore (árvore N-ária)
    └── modelos/
        ├── veiculo.py
        ├── cliente.py
        ├── estoque.py         # LoteEstoque e ProdutoEstoque
        └── ordem_servico.py
```

## Como executar

```bash
python menu.py   # menu interativo
python main.py   # simulação automática
```

Requer apenas Python 3.8+ (nenhuma dependência externa).

