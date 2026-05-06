import streamlit as st
import os
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "..", "data", "survey_Dados_Tratados.csv")
    return pd.read_csv(path, sep=";")

df = load_data()

# =========================
# NORMALIZAÇÃO FORTE
# =========================
def normalize_text(col):
    return col.astype(str).str.strip().str.lower()

df["Tratamento"] = normalize_text(df["Tratamento"])

map_bin = {
    "sim": 1, "yes": 1,
    "não": 0, "nao": 0, "no": 0
}

df["tratamento_bin"] = df["Tratamento"].map(map_bin)

df["Impacto_Trabalho"] = normalize_text(df["Impacto_Trabalho"])

impacto_map = {
    "nunca": 0,
    "raramente": 1,
    "às vezes": 1,
    "as vezes": 1,
    "muitas vezes": 1,
    "sem informações": np.nan
}

df["impacto_bin"] = df["Impacto_Trabalho"].map(impacto_map)

# =========================
# LABELS
# =========================
col_map = {
    "Tratamento": "Buscou tratamento para saúde mental?",
    "Impacto_Trabalho": "Saúde mental impacta o trabalho?",
    "Historico_Familiar": "Possui histórico familiar de doença mental?",
    "Beneficios": "Empresa oferece benefícios de saúde mental?",
    "Opcoes_Cuidado": "Conhece opções de cuidado oferecidas?",
    "Programa_Bem_Estar": "Empresa discute saúde mental em programas?",
    "Busca_Ajuda": "Empresa oferece recursos para buscar ajuda?",
    "Anonimato": "Anonimato é protegido ao buscar tratamento?",
    "Facilidade_Licenca": "Facilidade para tirar licença por saúde mental?",
    "Consequencia_Saude_Mental": "Há consequências negativas ao falar sobre saúde mental?",
    "Consequencia_Saude_Fisica": "Há consequências negativas ao falar sobre saúde física?",
    "Colegas": "Disposição para falar com colegas sobre saúde mental?",
    "Supervisor": "Disposição para falar com supervisor sobre saúde mental?",
    "Entrevista_Saude_Mental": "Falaria sobre saúde mental em entrevista?",
    "Entrevista_Saude_Fisica": "Falaria sobre saúde física em entrevista?"
}

def label(col):
    return col_map.get(col, col)

# =========================
# SCORES
# =========================
cols_empresa = [
    "Beneficios", "Opcoes_Cuidado", "Programa_Bem_Estar",
    "Busca_Ajuda", "Anonimato", "Facilidade_Licenca"
]

valid_cols_empresa = [c for c in cols_empresa if c in df.columns]

def map_sim_nao(x):
    return map_bin.get(str(x).strip().lower(), np.nan)

df["score_empresa"] = df[valid_cols_empresa].apply(
    lambda col: col.map(map_sim_nao)
).mean(axis=1)

cols_psico = [
    "Consequencia_Saude_Mental", "Consequencia_Saude_Fisica",
    "Colegas", "Supervisor",
    "Entrevista_Saude_Mental", "Entrevista_Saude_Fisica"
]

valid_cols_psico = [c for c in cols_psico if c in df.columns]

df["score_psicologico"] = df[valid_cols_psico].apply(
    lambda col: col.map(map_sim_nao)
).mean(axis=1)

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Filtros")

modo = st.sidebar.radio(
    "Modo de análise",
    ["Indicadores relacionais", "Indicadores absolutos"],
    horizontal=True
)

modo_relacional = modo == "Indicadores relacionais"

generos = st.sidebar.multiselect(
    "Gênero",
    options=df['Genero'].dropna().unique(),
    default=df['Genero'].dropna().unique()
)

df = df[df['Genero'].isin(generos)]

# =========================
# FUNÇÃO HEATMAP (PADRÃO)
# =========================
def heatmap_relacao(df, col_x, col_y, titulo=None):

    df_plot = pd.crosstab(
        df[col_x],
        df[col_y],
        normalize='index'
    )

    fig = px.imshow(
        df_plot,
        text_auto=".1%",
        labels=dict(
            x=label(col_y),
            y=label(col_x),
            color="% dentro do grupo"
        ),
        title=titulo
    )

    fig.update_coloraxes(colorbar_tickformat=".0%")

    return fig

# =========================
# HEADER
# =========================
st.title("Dashboard de Saúde Mental no Trabalho")

# =========================
# MODO RELACIONAL
# =========================
if modo_relacional:

    pagina = st.radio(
        "Selecione a página",
        ["Visão Geral", "Empresa & Suporte", "Ambiente & Cultura", "Medo & Carreira"],
        horizontal=True
    )

    if pagina == "Visão Geral":

        st.subheader("Panorama geral da saúde mental")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Buscou tratamento (%)", f"{df['tratamento_bin'].mean()*100:.1f}%")
        col2.metric("Impacto no trabalho (%)", f"{df['impacto_bin'].mean()*100:.1f}%")
        col3.metric("Score de suporte organizacional", f"{df['score_empresa'].mean():.2f}")
        col4.metric("Score de segurança psicológica", f"{df['score_psicologico'].mean():.2f}")

        st.caption("Score varia de 0 a 1.")

        dados = df['Tratamento'].value_counts(normalize=True).reset_index()
        dados.columns = ['Resposta', 'Percentual']
        dados["Percentual"] *= 100

        fig = px.bar(
            dados,
            x='Resposta',
            y='Percentual',
            text_auto=".1f",
            labels={"Percentual": "Percentual (%)"}
        )

        fig.update_yaxes(ticksuffix="%")
        st.plotly_chart(fig, use_container_width=True)

    elif pagina == "Empresa & Suporte":

        variavel = st.selectbox("Fator de suporte", valid_cols_empresa, format_func=label)

        st.plotly_chart(
            heatmap_relacao(df, variavel, "Tratamento"),
            use_container_width=True
        )

        st.plotly_chart(
            px.box(df, x="Tratamento", y="score_empresa"),
            use_container_width=True
        )

        variavel_impacto = st.selectbox(
            "Fator de suporte (impacto)",
            valid_cols_empresa,
            key="impacto",
            format_func=label
        )

        st.plotly_chart(
            heatmap_relacao(df, variavel_impacto, "Impacto_Trabalho"),
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("Modelo de trabalho")

        for (x, y, t) in [
            ("autônomo", "Impacto_Trabalho", "Autônomo vs Impacto"),
            ("Trabalho_Remoto", "Impacto_Trabalho", "Remoto vs Impacto"),
            ("autônomo", "Tratamento", "Autônomo vs Tratamento"),
            ("Trabalho_Remoto", "Tratamento", "Remoto vs Tratamento"),
            ("Trabalho_Remoto", "Supervisor", "Remoto vs Supervisor"),
        ]:
            if x in df.columns:
                st.plotly_chart(
                    heatmap_relacao(df, x, y, t),
                    use_container_width=True
                )

    elif pagina == "Ambiente & Cultura":

        col1, col2 = st.columns(2)

        col1.metric("Abertura colegas", f"{df['Colegas'].map(map_sim_nao).mean()*100:.1f}%")
        col2.metric("Abertura supervisor", f"{df['Supervisor'].map(map_sim_nao).mean()*100:.1f}%")

        col1, col2 = st.columns(2)

        with col1:
            var_emp = st.selectbox("Empresa", valid_cols_empresa, format_func=label)
            
        with col2:
            var_amb = st.selectbox("Abertura", ["Colegas", "Supervisor"], format_func=label)

        st.plotly_chart(
            heatmap_relacao(df, var_emp, var_amb),
            use_container_width=True
        )

    elif pagina == "Medo & Carreira":

        st.plotly_chart(
            heatmap_relacao(df, "Consequencia_Saude_Mental", "Tratamento"),
            use_container_width=True
        )

        var = st.selectbox("Empresa", valid_cols_empresa, format_func=label)

        st.plotly_chart(
            heatmap_relacao(df, var, "Entrevista_Saude_Mental"),
            use_container_width=True
        )

# =========================
# MODO ABSOLUTO
# =========================
else:

    st.subheader("Distribuição Geral (%)")

    colunas = [
        "Tratamento","Beneficios","Impacto_Trabalho","Historico_Familiar",
        "Opcoes_Cuidado","Programa_Bem_Estar","Busca_Ajuda","Anonimato",
        "Facilidade_Licenca","Consequencia_Saude_Mental","Consequencia_Saude_Fisica",
        "Colegas","Supervisor","Entrevista_Saude_Mental","Entrevista_Saude_Fisica"
    ]

    for col in colunas:

        if col not in df.columns:
            continue

        dados = df[col].value_counts(normalize=True).reset_index()
        dados.columns = [col, "percentual"]

        fig = px.bar(
            dados,
            x=col,
            y="percentual",
            text_auto=".1%",
            labels={"percentual": "% do total"}
        )

        fig.update_yaxes(tickformat=".0%")

        st.markdown("---")
        st.subheader(label(col))
        st.plotly_chart(fig, use_container_width=True)