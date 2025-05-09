from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/fora-do-padrao')
def mostrar_fora_do_padrao():
    conn = sqlite3.connect('dados_sisagua.db')
    cursor = conn.cursor()

    query = '''
        SELECT * FROM dados WHERE
            (parametro = 'Escherichia coli' AND resultado != 'AUSENTE') OR
            (parametro = 'Cloro residual livre (mg/L)' AND (CAST(resultado AS REAL) < 0.2 OR CAST(resultado AS REAL) > 5.0)) OR
            (parametro = 'Fluoreto (mg/L)' AND (CAST(resultado AS REAL) < 0.6 OR CAST(resultado AS REAL) > 0.8)) OR
            (parametro = 'Coliformes totais' AND resultado != 'AUSENTE') OR
            (parametro = 'Turbidez (uT)' AND CAST(resultado AS REAL) > 5.0)
    '''

    cursor.execute(query)
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    conn.close()

    return render_template('fora_do_padrao.html', dados=dados, colunas=colunas)

if __name__ == '__main__':
    app.run(debug=True)
