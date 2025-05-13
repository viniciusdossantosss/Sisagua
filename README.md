# 📊 Projeto SISAGUA - Vigilância da Qualidade da Água

Este projeto tem como objetivo coletar, armazenar e exibir dados da qualidade da água de abastecimento humano da cidade de **Barreiras - BA**, utilizando a API do **SISAGUA** (Sistema de Informação de Vigilância da Qualidade da Água para Consumo Humano).

A aplicação foi desenvolvida com **Python**, **SQLite** e **Flask**, permitindo a visualização interativa dos parâmetros analisados diretamente em uma interface web.

---

## 🛠️ Funcionalidades

- ✅ Coleta automatizada de dados do SISAGUA via API.
- ✅ Armazenamento local em banco de dados SQLite.
- ✅ Visualização de dados em tabelas e gráficos interativos.
- ✅ Página exclusiva para exibir dados **fora dos padrões recomendados**.
- ✅ Ranking de parâmetros coletados.

---

## 📈 Parâmetros Monitorados

- Escherichia coli
- Coliformes totais
- Cloro residual livre (mg/L)
- Fluoreto (mg/L)
- Turbidez (uT)

---

## 📊 Padrões Utilizados

| Parâmetro                      | Padrão Aceitável                         |
| ------------------------------ | ---------------------------------------- |
| **Escherichia coli**            | Ausente                                  |
| **Coliformes totais**           | Ausente                                  |
| **Cloro residual livre (mg/L)** | Entre 0,2 mg/L e 5,0 mg/L                |
| **Fluoreto (mg/L)**             | Entre 0,6 mg/L e 0,8 mg/L                |
| **Turbidez (uT)**               | Até 5,0 uT                               |

---

## 🚀 Como executar o projeto localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/sisagua.git
cd sisagua
````

### 2. Instalar as dependências
```bash
pip install flask requests plotly pandas
````

### 3. Coletar os dados da API e salvar no banco SQLite
````bash
python main.py
````

### 4. Iniciar a aplicação Flask
````bash
python app.py
````
### 5. Acessar no navegador
   
Página principal: http://localhost:5000

Ranking: http://localhost:5000/ranking

Parâmetros fora do padrão: http://localhost:5000/fora-do-padrao

### 6. Exportar dados para CSV (opcional)
````bash
Copy
Edit
python exportar_csv.py
📂 Estrutura do Projeto
graphql
Copy
Edit
sisagua/
├── dados_sisagua.db         # Banco de dados SQLite com as amostras coletadas
├── main.py                  # Script de coleta e armazenamento dos dados
├── app.py                   # Aplicação Flask principal (rotas e visualização)
├── fora_do_padrao.py        # Rota e visualização de dados fora do padrão
├── exportar_csv.py          # Script para exportar os dados para CSV
├── templates/
│   ├── index.html           # Página inicial com visão geral
│   ├── ranking.html         # Página com ranking de parâmetros
│   └── fora_do_padrao.html  # Página com dados fora do padrão
├── static/                  # Arquivos estáticos (CSS / JS / imagens)
└── README.md                # Este arquivo de documentação
````

## 🌎 Fonte dos Dados
Os dados são obtidos da API oficial de Dados Abertos do Ministério da Saúde - SISAGUA:

https://apidadosabertos.saude.gov.br/sisagua/vigilancia-parametros-basicos

## 🧑‍💻 Autores
Projeto desenvolvido por:
 -

Este projeto tem caráter educacional e visa demonstrar habilidades em:

Coleta de dados abertos (API REST)

Armazenamento em banco de dados

Desenvolvimento de aplicações web com Flask

Visualização de dados (tabelas, gráficos, rankings)

Transparência e acesso à informação pública

## 📝 Licença
Distribuído sob a licença MIT.
Consulte o arquivo LICENSE para mais informações.


  
