import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Criando dados fictícios
data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Receita": [1000, 1500, 1300, 1700, 1600, 2000],
    "Despesas": [800, 1100, 900, 1200, 1150, 1400]
}
df = pd.DataFrame(data)

# Sidebar para filtros
with st.sidebar:
    st.header("Filtros")
    mes_selecionado = st.selectbox("Escolha um mês:", df["Mês"])

# Título do Dashboard
st.title("📊 Dashboard de Finanças Pessoais")

# Exibindo métricas
receita_total = df["Receita"].sum()
despesa_total = df["Despesas"].sum()
saldo = receita_total - despesa_total

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Receita Total", f"R$ {receita_total}")
with col2:
    st.metric("Despesa Total", f"R$ {despesa_total}")
with col3:
    st.metric("Saldo", f"R$ {saldo}")

# Gráfico de linhas
fig_line = px.line(df, x="Mês", y=["Receita", "Despesas"], markers=True, title="Receita vs. Despesas",
                   color_discrete_map={"Receita": "#1f77b4", "Despesas": "#ff7f0e"})
st.plotly_chart(fig_line, use_container_width=True)

# Gráfico de barras
fig_bar = px.bar(df, x="Mês", y=["Receita", "Despesas"], barmode="group", title="Receita e Despesas por Mês")
st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de pizza
fig_pie = px.pie(df, values="Despesas", names="Mês", title="Proporção de Despesas por Mês")
st.plotly_chart(fig_pie, use_container_width=True)

# Estilização
st.markdown("""
    <style>
    h1 {color: #4CAF50;}
    .stButton button {background-color: #4CAF50; color: white;}
    th {background-color: #4CAF50; color: white; text-align: center;}
    td {text-align: center;}
    table {width: 100% !important;}
    </style>
""", unsafe_allow_html=True)