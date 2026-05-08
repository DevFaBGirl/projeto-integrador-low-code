import streamlit as st
import pandas as pd
import plotly.express as px
import os


st.set_page_config(
    page_title="Dashboard Saúde Mental",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #2e4053;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        color: #5d6d7e;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title"> Dashboard: Saúde Mental na Tecnologia</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Análise baseada nos dados da pesquisa <i>Mental Health in Tech Survey</i></p>', unsafe_allow_html=True)


@st.cache_data
def load_data():
     
    caminhos = [
        '../data/survey_Dados_Tratados.csv',
        'data/survey_Dados_Tratados.csv',
        'survey_Dados_Tratados.csv'
    ]
    
    for caminho in caminhos:
        if os.path.exists(caminho):
            return pd.read_csv(caminho, sep=';')
            
    st.error("Arquivo de dados 'survey_Dados_Tratados.csv' não encontrado!")
    st.stop()

df = load_data()




st.markdown("###  Principais Indicadores")

col1, col2, col3 = st.columns(3)

tratamento_pct = (df['Tratamento'] == 'Sim').mean() * 100
impacto_pct = df['Impacto_Trabalho'].isin(['Muitas vezes', 'Às vezes']).mean() * 100
historico_pct = (df['Historico_Familiar'] == 'Sim').mean() * 100

col1.metric("Buscaram Tratamento Psicológico", f"{tratamento_pct:.1f}%")
col2.metric("Impacto Frequente no Trabalho", f"{impacto_pct:.1f}%")
col3.metric("Têm Histórico Familiar", f"{historico_pct:.1f}%")

st.divider()



tab1, tab2, tab3, tab4 = st.tabs([
    " Visão Geral", 
    " Empresa & Suporte", 
    " Ambiente & Cultura", 
    " Medo & Carreira"
])

with tab1:
    st.header("1. Visão Geral")
    st.markdown("Panorama geral da saúde mental dos profissionais analisados.")
    
    colA, colB = st.columns(2)
    
    with colA:
        fig1 = px.pie(df, names='Tratamento', 
                      title="Profissionais que Buscaram Tratamento",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig1, use_container_width=True)
        
    with colB:
        fig2 = px.histogram(df, x='Impacto_Trabalho', 
                            title="Frequência que a Saúde Mental Impacta no Trabalho",
                            color='Impacto_Trabalho',
                            category_orders={"Impacto_Trabalho": ["Nunca", "Raramente", "Às vezes", "Muitas vezes", "Sem Informações"]})
        st.plotly_chart(fig2, use_container_width=True)


with tab2:
    st.header("2. Empresa & Suporte")
    st.markdown("Avaliação de como o suporte organizacional influencia o bem-estar e o tratamento.")
    
    colC, colD = st.columns(2)
    
    with colC:
        fig3 = px.density_heatmap(df, x='Beneficios', y='Tratamento', 
                                  title="Empresa Oferece Benefícios vs Busca por Tratamento",
                                  text_auto=True, color_continuous_scale="Blues")
        st.plotly_chart(fig3, use_container_width=True)
        
    with colD:
        fig4 = px.density_heatmap(df, x='Programa_Bem_Estar', y='Impacto_Trabalho', 
                                  title="Programa de Bem-Estar vs Impacto no Trabalho",
                                  text_auto=True, color_continuous_scale="Teal")
        st.plotly_chart(fig4, use_container_width=True)


with tab3:
    st.header("3. Ambiente & Cultura")
    st.markdown("Compreensão do suporte organizacional na criação de um ambiente seguro para o diálogo.")
    
    fig5 = px.density_heatmap(df, x='Colegas', y='Supervisor', 
                              title="Disposição em Discutir Saúde Mental: Colegas vs Supervisor",
                              labels={"Colegas": "Abertura com Colegas", "Supervisor": "Abertura com Supervisor"},
                              text_auto=True, color_continuous_scale="Purples")
    st.plotly_chart(fig5, use_container_width=True)


with tab4:
    st.header("4. Medo & Carreira")
    st.markdown("Análise de como o medo de consequências negativas impacta os profissionais.")
    
    colE, colF = st.columns(2)
    
    with colE:
        fig6 = px.density_heatmap(df, x='Consequencia_Saude_Mental', y='Tratamento', 
                                  title="Medo de Consequências vs Busca por Tratamento",
                                  labels={"Consequencia_Saude_Mental": "Temer Consequências Negativas"},
                                  text_auto=True, color_continuous_scale="Reds")
        st.plotly_chart(fig6, use_container_width=True)
        
    with colF:
        fig7 = px.histogram(df, x='Entrevista_Saude_Mental', 
                            title="Você falaria de Saúde Mental numa Entrevista de Emprego?",
                            color='Entrevista_Saude_Mental')
        st.plotly_chart(fig7, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Desenvolvido por Grupo 17 - Projeto Integrador Low Code</p>", unsafe_allow_html=True)
