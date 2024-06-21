import sqlite3
from database import criar_tabelas


criar_tabelas()


def nova_entrada():
    nome_cliente = input("Digite o nome do cliente: ")
    valor_recebido = input("Digite o valor recebido: ")
    data_faturamento = input("Informe a data de recebimento (AAAA-MM-DD): ")

    conn = sqlite3.connect("controle_financeiro.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO entrada (nome_cliente, valor_recebido, data_faturamento)
        VALUES (?, ?, ?)
''', (nome_cliente, valor_recebido, data_faturamento))
    
    conn.commit()
    conn.close()

    print("EVENTO REGISTRADO COM SUCESSO!!!")


def nova_saida():
    nome_fornecedor = input("Digite o nome do fornecedor: ")
    valor_pago = input("Digite o valor pago: ")
    data_saida = input("Informe a data de pagamento (AAAA-MM-DD): ")

    conn = sqlite3.connect("controle_financeiro.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO saida (nome_fornecedor, valor_pago, data_saida)
        VALUES (?, ?, ?)
''', (nome_fornecedor, valor_pago, data_saida))
    
    conn.commit()
    conn.close()

    print("EVENTO REGISTRADO COM SUCESSO!!!")


if __name__ == "__main__":
    while True:
        print(">>> Bem Vindo(a)!!! <<<")
        print("1. Inserir entrada")
        print("2. Inserir saída")
        print("3. Encerrar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nova_entrada()
        elif escolha == "2":
            nova_saida()
        elif escolha == "3":
            break
        else:
            print("Opção inválida, tente novamente.")


