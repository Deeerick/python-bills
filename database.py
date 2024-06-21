import sqlite3

def criar_tabelas():
    conn = sqlite3.connect("controle_financeiro.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entrada (
            id_entrada INTEGER PRIMARY KEY,
            nome_cliente TEXT NOT NULL,
            valor_recebido INTEGER NOT NULL,
            data_faturamento DATE
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saida (
            id_saida INTEGER PRIMARY KEY,
            nome_fornecedor TEXT NOT NULL,
            valor_pago INTEGER NOT NULL,
            data_saida DATE
    )
    ''')

    conn.commit()
    conn.close()
