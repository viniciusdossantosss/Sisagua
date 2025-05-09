# ranking_amostras_bairros.py
import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect("dados_sisagua.db")
df = pd.read_sql_query("SELECT * FROM dados", conn)
conn.close()

# Verifica se as colunas necessárias existem
if 'area' not in df.columns or 'mes' not in df.columns:
    print("Colunas necessárias ('area' ou 'mes') não encontradas na base de dados.")
else:
    # Agrupar por mês e por bairro (area), contando amostras
    ranking_mensal = df.groupby(['mes', 'area']).size().reset_index(name='quantidade_amostras')

    # Ordenar os resultados por mês e por quantidade (desc)
    ranking_mensal = ranking_mensal.sort_values(by=['mes', 'quantidade_amostras'], ascending=[True, False])

    # Exibir ranking por mês
    for mes in sorted(ranking_mensal['mes'].unique()):
        print(f"\n📅 Ranking de Amostras por Bairro - Mês: {mes:02}")
        ranking_mes = ranking_mensal[ranking_mensal['mes'] == mes].reset_index(drop=True)
        ranking_mes.index += 1
        print(ranking_mes[['area', 'quantidade_amostras']])
