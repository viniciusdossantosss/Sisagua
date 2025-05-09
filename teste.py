import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('dados_sisagua.db')
cursor = conn.cursor()

# Buscar todos os dados da tabela
cursor.execute('SELECT * FROM dados')
dados = cursor.fetchall()

# Obter os nomes das colunas
colunas = [descricao[0] for descricao in cursor.description]

# Nome do arquivo CSV de saída
nome_arquivo_csv = 'dados_exportados.csv'

# Escrever os dados no CSV
with open(nome_arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(colunas)  # Cabeçalho
    writer.writerows(dados)   # Linhas de dados

# Fechar conexão
conn.close()

print(f"✅ Exportação concluída! Arquivo salvo como: {nome_arquivo_csv}")
