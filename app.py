from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

# Função para carregar os dados do banco, com suporte para filtro por mês
def carregar_dados(mes=None):
    conn = sqlite3.connect('dados_sisagua.db')
    query = "SELECT * FROM dados"
    if mes:
        query += f" WHERE mes = {int(mes)}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Rota principal para exibir os dados filtrados por mês
@app.route('/', methods=['GET'])
def index():
    mes = request.args.get('mes')  # Pegando o mês selecionado na URL (ex: ?mes=3)
    df = carregar_dados(mes)

    # Geração da tabela HTML
    if df.empty:
        tabela_html = "<p>Sem dados disponíveis para o mês selecionado.</p>"
    else:
        tabela_html = df.to_html(classes='table table-striped', index=False)

    # Lista de meses para o filtro
    meses = [
        {'numero': i, 'nome': nome} for i, nome in enumerate(
            ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], start=1
        )
    ]

    return render_template('index.html', tabela=tabela_html, meses=meses, mes_selecionado=mes)

# Rota para exibir o ranking de amostras por bairro, com suporte para filtro por mês
@app.route('/ranking', methods=['GET'])
def ranking():
    mes = request.args.get('mes')  # Pegando o mês selecionado na URL (ex: ?mes=3)
    df = carregar_dados(mes)

    if 'area' not in df.columns or 'mes' not in df.columns:
        return "Colunas necessárias não encontradas."

    # Agrupar por mês e bairro, contando as amostras
    ranking_mensal = df.groupby(['mes', 'area']).size().reset_index(name='quantidade_amostras')
    ranking_mensal = ranking_mensal.sort_values(by=['mes', 'quantidade_amostras'], ascending=[True, False])

    # Separar os dados por mês para exibir em blocos
    dados_por_mes = {}
    for mes_unico in sorted(ranking_mensal['mes'].unique()):
        dados_por_mes[mes_unico] = ranking_mensal[ranking_mensal['mes'] == mes_unico][['area', 'quantidade_amostras']].to_dict(orient='records')

    # Lista de meses para o filtro
    meses = [
        {'numero': i, 'nome': nome} for i, nome in enumerate(
            ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], start=1
        )
    ]

    return render_template('ranking.html', dados_por_mes=dados_por_mes, meses=meses, mes_selecionado=mes)

if __name__ == '__main__':
    app.run(debug=True)
