import requests
import sqlite3
from datetime import datetime

# Obter o ano atual
ano_atual = datetime.now().year

# Lista de meses do ano formatados como '01', '02', ..., '12'
meses = [str(m).zfill(2) for m in range(1, 13)]

# Parâmetros para cada mês e tipo de análise
parametros_lista = [
    {'uf': 'BA', 'codigo_ibge': '292740', 'ano': str(ano_atual), 'mes': mes, 'parametro': parametro}
    for mes in meses
    for parametro in [
        'Escherichia coli',
        'Turbidez (uT)',
        'Cloro residual livre (mg/L)',
        'Coliformes totais',
        'Fluoreto (mg/L)'
    ]
]

# Função para coletar os dados da API
def coletar_dados(parametros):
    print(f"🔄 Coletando dados: {parametros['parametro']} - {parametros['mes']}/{parametros['ano']}")
    response = requests.get("https://apidadosabertos.saude.gov.br/sisagua/vigilancia-parametros-basicos", params=parametros)
    if response.status_code == 200:
        dados = response.json()
        return dados.get('parametros', [])
    else:
        print(f"⚠️ Erro {response.status_code} na requisição.")
        return []

# Função para salvar dados no SQLite
def salvar_dados_no_banco(dados):
    conn = sqlite3.connect('dados_sisagua.db')
    cursor = conn.cursor()

    # Criar a tabela com id autoincrementável
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_da_amostra TEXT,
            tipo_da_forma_de_abastecimento TEXT,
            ano INTEGER,
            mes INTEGER,
            data_da_coleta TEXT,
            area TEXT,
            zona TEXT,
            latitude REAL,
            longitude REAL,
            parametro TEXT,
            resultado TEXT,
            procedencia_da_coleta TEXT,
            ponto_de_coleta TEXT
        )
    ''')

    # Limpar todos os dados anteriores
    cursor.execute('DELETE FROM dados')
    print("🗑️ Todos os dados anteriores foram removidos do banco.")

    # Inserir os dados
    for item in dados:
        cursor.execute('''
            INSERT INTO dados (
                numero_da_amostra, tipo_da_forma_de_abastecimento, ano, mes, data_da_coleta,
                area, zona, latitude, longitude, parametro, resultado, procedencia_da_coleta, ponto_de_coleta
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item.get('numero_da_amostra'),
            item.get('tipo_da_forma_de_abastecimento'),
            item.get('ano'),
            item.get('mes'),
            item.get('data_da_coleta'),
            item.get('area'),
            item.get('zona'),
            item.get('latitude'),
            item.get('longitude'),
            item.get('parametro'),
            item.get('resultado'),
            item.get('procedencia_da_coleta'),
            item.get('ponto_de_coleta')
        ))

    conn.commit()
    conn.close()

# Função principal
def main():
    todos_dados = []
    for parametros in parametros_lista:
        dados = coletar_dados(parametros)
        if dados:
            todos_dados.extend(dados)

    if todos_dados:
        salvar_dados_no_banco(todos_dados)
        print(f"✅ {len(todos_dados)} registros salvos no banco após limpeza.")
    else:
        print("⚠️ Nenhum dado coletado.")

if __name__ == '__main__':
    main()
