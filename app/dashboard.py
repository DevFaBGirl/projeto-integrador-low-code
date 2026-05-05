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
# NORMALIZAÇÃO FORTE (CRÍTICO)
# =========================
def normalize_text(col):
    return col.astype(str).str.strip().str.lower()

df["Tratamento"] = normalize_text(df["Tratamento"])

map_bin = {
    "sim": 1, "yes": 1,
    "não": 0, "nao": 0, "no": 0
}

df["tratamento_bin"] = df["Tratamento"].map(map_bin)

df["Impacto_Trabalho"] = (
    df["Impacto_Trabalho"]
    .astype(str)
    .str.strip()
    .str.lower()
)

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
# CAMADA SEMÂNTICA
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
    x = str(x).strip().lower()
    return map_bin.get(x, np.nan)

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

generos = st.sidebar.multiselect(
    "Gênero",
    options=df['Genero'].dropna().unique(),
    default=df['Genero'].dropna().unique()
)

df = df[df['Genero'].isin(generos)]

# =========================
# HEADER
# =========================
st.title("Dashboard de Saúde Mental no Trabalho")

pagina = st.radio(
    "Selecione a página",
    ["Visão Geral", "Empresa & Suporte", "Ambiente & Cultura", "Medo & Carreira"],
    horizontal=True
)

# =========================
# VISÃO GERAL
# =========================
if pagina == "Visão Geral":

    st.subheader("Panorama geral da saúde mental")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Buscou tratamento (%)", f"{df['tratamento_bin'].mean()*100:.1f}%")
    col2.metric("Impacto no trabalho (%)", f"{df['impacto_bin'].mean()*100:.1f}%")
    col3.metric("Score de suporte organizacional", f"{df['score_empresa'].mean():.2f}")
    col4.metric("Score de segurança psicológica", f"{df['score_psicologico'].mean():.2f}")

    st.markdown("### Distribuição de tratamento")

    st.caption(label("Tratamento"))

    dados = df['Tratamento'].value_counts(normalize=True).reset_index()
    dados.columns = ['Resposta', 'Percentual']

    dados["Percentual"] = dados["Percentual"] * 100

    fig = px.bar(
        dados,
        x='Resposta',
        y='Percentual',
        text_auto=".1f",
        labels={
            "Resposta": label("Tratamento"),
            "Percentual": "Percentual (%)"
        }
    )

    fig.update_yaxes(ticksuffix="%")

    st.plotly_chart(fig, use_container_width=True)

# =========================
# EMPRESA & SUPORTE
# =========================
elif pagina == "Empresa & Suporte":

    st.subheader("O suporte da empresa influencia a busca por tratamento?")

    variavel = st.selectbox(
        "Fator de suporte",
        valid_cols_empresa,
        format_func=label
    )

    st.caption(label(variavel))

    df_plot = (df.groupby(variavel)["tratamento_bin"].mean().reset_index())

    fig = px.bar(
        df_plot,
        x=variavel,
        y="tratamento_bin",
        labels={
            variavel: label(variavel),
            "tratamento_bin": "% que buscou tratamento"
        },
        text_auto=".1%"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribuição do suporte organizacional")

    fig = px.box(
        df,
        x="Tratamento",
        y="score_empresa",
        labels={
            "Tratamento": label("Tratamento"),
            "score_empresa": "Score de suporte organizacional"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Suporte vs Impacto no trabalho")

    variavel_impacto = st.selectbox(
        "Fator de suporte (impacto)",
        valid_cols_empresa,
        key="impacto",
        format_func=label
    )

    df_plot = (
        df.groupby(variavel_impacto)["impacto_bin"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        df_plot,
        x=variavel_impacto,
        y="impacto_bin",
        labels={
            variavel_impacto: label(variavel_impacto),
            "impacto_bin": "% com impacto no trabalho"
        },
        text_auto=".1%"
    )

    st.plotly_chart(fig, use_container_width=True)
# =========================
# AMBIENTE & CULTURA
# =========================
elif pagina == "Ambiente & Cultura":

    st.subheader("O ambiente favorece a abertura para discussão?")

    col1, col2 = st.columns(2)

    col1.metric(
        "Abertura com colegas",
        f"{df['Colegas'].apply(map_sim_nao).mean():.2f}"
    )

    col2.metric(
        "Abertura com supervisores",
        f"{df['Supervisor'].apply(map_sim_nao).mean():.2f}"
    )

    col1, col2 = st.columns(2)

    with col1:
        variavel_empresa = st.selectbox(
            "Fator da empresa",
            valid_cols_empresa,
            format_func=label
        )

    with col2:
        variavel_ambiente = st.selectbox(
            "Tipo de abertura",
            ["Colegas", "Supervisor"],
            format_func=label
        )

    df_plot = (
        df.groupby(variavel_empresa)[variavel_ambiente]
        .apply(lambda x: x.map(map_sim_nao).mean()*100)
        .reset_index()
    )

    fig = px.bar(
        df_plot,
        x=variavel_empresa,
        y=variavel_ambiente,
        labels={
            variavel_empresa: label(variavel_empresa),
            variavel_ambiente: "Nível médio de abertura"
        },
        text_auto=".2f"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================
# MEDO & CARREIRA
# =========================
elif pagina == "Medo & Carreira":

    st.subheader("O medo influencia o comportamento profissional?")

    if "Consequencia_Saude_Mental" in df.columns:
        df["medo_score"] = df["Consequencia_Saude_Mental"].apply(map_sim_nao)*100


    dados = df["Consequencia_Saude_Mental"].value_counts(normalize=True).reset_index()
    dados.columns = ["Resposta", "Percentual"]

    dados = df.groupby("Consequencia_Saude_Mental")["tratamento_bin"].mean().reset_index()

    fig = px.bar(
        dados,
        x="Consequencia_Saude_Mental",
        y="tratamento_bin",
        text_auto=".1%",
        labels={
            "Consequencia_Saude_Mental": label("Consequencia_Saude_Mental"),
            "tratamento_bin": "% que buscou tratamento"
        },
        title="Medo vs busca por tratamento"
    )

    st.plotly_chart(fig, use_container_width=True)
    

    variavel_empresa = st.selectbox(
        "Fator da empresa",
        valid_cols_empresa,
        format_func=label
    )

    heatmap = pd.crosstab(
        df[variavel_empresa],
        df["Entrevista_Saude_Mental"],
        normalize='index'
    ) * 100

    fig = px.imshow(
        heatmap,
        text_auto=".1f",
        labels=dict(
            x=label("Entrevista_Saude_Mental"),
            y=label(variavel_empresa),
            color="Percentual (%)"
        )
    )

    st.plotly_chart(fig, use_container_width=True)