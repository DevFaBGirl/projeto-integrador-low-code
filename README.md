# PROJETO INTEGRADOR - LOW CODE GRUPO 17

## Tema do Projeto
<h1>Saúde Mental no Trabalho nos Dias Atuais</h1>

## Integrantes
- Estefano Deimis Martins
- Fabiana Balduina Freitas Silva
- Giovanna Alves Galichi
- Leonardo Santos De Oliveira
- Matheus Batista Lopes
- Vinicius Lourenco Martinsa

## Descrição sobre o Projeto
<p>A saúde mental tem se tornado um tema cada vez mais relevante na sociedade contemporânea, especialmente em ambientes de trabalho altamente exigentes, como o setor de tecnologia. Com o avanço da digitalização, a pressão por produtividade, prazos curtos e a constante necessidade de atualização profissional têm contribuído para o aumento do estresse, da ansiedade e de outros problemas psicológicos entre trabalhadores. Nesse contexto, compreender e discutir a saúde mental tornou-se essencial para garantir qualidade de vida, bem-estar e desempenho profissional.</p>

<p>Um ponto importante é que problemas de saúde mental não afetam apenas o indivíduo, mas também impactam diretamente as organizações e a sociedade. Estima-se que transtornos como depressão e ansiedade afetem centenas de milhões de pessoas no mundo, causando perda de produtividade e impactos econômicos significativos. Dessa forma, promover ambientes de trabalho mais saudáveis, incentivar o diálogo sobre saúde mental e oferecer suporte adequado aos colaboradores são medidas fundamentais para reduzir esses impactos.</p>

<p>Com base nessas questões, este projeto utiliza dados da pesquisa Mental Health in Tech Survey, disponibilizada na plataforma Kaggle, que reúne respostas de profissionais da área de tecnologia sobre temas relacionados à saúde mental no ambiente de trabalho. A base de dados contém informações sobre histórico de saúde mental, acesso a tratamento, percepção sobre apoio das empresas e impacto desses fatores na vida profissional.

## Objetivo da Análise
<p>A análise desses dados permite identificar padrões, tendências e possíveis fatores que influenciam o acesso ao tratamento psicológico e a percepção dos trabalhadores em relação à saúde mental no setor de tecnologia. Dessa forma, o projeto busca contribuir para uma melhor compreensão do tema e destacar a importância de iniciativas que promovam ambientes de trabalho mais saudáveis e conscientes em relação à saúde mental.</p>

<p>Portanto, discutir a saúde mental nos dias atuais é essencial para compreender os desafios enfrentados pelos trabalhadores e desenvolver estratégias que promovam o bem-estar. Iniciativas de conscientização, políticas organizacionais de apoio psicológico e ambientes de trabalho mais empáticos são passos importantes para garantir que os profissionais possam desempenhar suas funções de forma saudável e sustentável.</p>

## Base de Dados
<h3>Fonte de dados foi coletada no site <a href="https://www.kaggle.com/code/chaitanya99/mental-health-in-tech-survey-eda" target="_blank" rel="author">Kaggle</a>

## Processamento de Dados (ETL)
<p>Para garantir a qualidade da análise, os dados brutos passaram por um processo de <strong>ETL (Extract, Transform, Load)</strong> utilizando a biblioteca Pandas em Python:</p>

<ul>
    <li><strong>Extração:</strong> Os dados foram carregados diretamente do arquivo original <code>survey.csv</code>.</li>
    <li><strong>Transformação:</strong>
        <ul>
            <li><strong>Tradução:</strong> Colunas e respostas (como "Yes", "No", "Often") foram traduzidas para o português para facilitar a visualização no dashboard.</li>
            <li><strong>Limpeza de Outliers:</strong> Filtramos a coluna de idade para manter apenas registros entre 18 e 120 anos, eliminando dados inconsistentes.</li>
            <li><strong>Tratamento de Nulos:</strong> Valores ausentes foram preenchidos com o termo "Sem Informações" para evitar distorções estatísticas.</li>
            <li><strong>Padronização:</strong> Formatação da coluna de data e ajuste na categoria de quantidade de funcionários para evitar erros de interpretação por ferramentas de BI.</li>
        </ul>
    </li>
    <li><strong>Carga:</strong> O resultado final foi exportado para o arquivo <code>survey_Dados_Tratados.csv</code>, estruturado e pronto para consumo.</li>
</ul>

## Ideia Inicial do Dashboard
<p>O dashboard foi desenvolvido utilizando o Pandas para tratamento e geração de indicadores, Plotly Express para geração gráfica e Streamlit, permitindo a visualização interativa dos dados diretamente no navegador.</p>

<p>O conjunto de gráficos visa proporcionar entendimento e criar relações entre os fatores apontados no banco de dados. Através da análise cruzada das informações, é possível identificar associações entre a adoção de programas de bem-estar, a busca por tratamento, o impacto no trabalho, a criação de um ambiente confortável para discussão de problemas e os receios que os profissionais têm em comentar sobre sua saúde mental.</p>

<h2>📈 Indicadores e Visualizações</h2>

<p>O dashboard está organizado em páginas temáticas, permitindo a análise estruturada das relações entre suporte organizacional, comportamento dos profissionais, cultura no ambiente de trabalho e bem-estar.</p>

<h3>📊 1. Visão Geral</h3>

<p><b>Objetivo:</b> Apresentar o panorama geral da saúde mental dos profissionais.</p>

<p><b>Indicadores:</b></p>
<ul>
    <li>Percentual de profissionais que buscaram tratamento;</li>
    <li>Percentual de profissionais que relatam impacto no trabalho;</li>
    <li>Score médio de suporte organizacional;</li>
    <li>Score médio de segurança psicológica.</li>
</ul>

<p><b>Visualizações:</b></p>
<ul>
    <li>Gráfico de barras com a distribuição de profissionais que buscaram tratamento.</li>
</ul>

<p>Permite compreender a dimensão do problema e o comportamento geral dos profissionais em relação à saúde mental.</p>

<h3>🏢 2. Empresa & Suporte</h3>

<p><b>Objetivo:</b> Avaliar como o suporte organizacional influencia o comportamento e o bem-estar dos profissionais.</p>

<p><b>Indicadores:</b></p>
<ul>
    <li>Score médio de suporte organizacional;</li>
    <li>Distribuição do suporte em relação à busca por tratamento.</li>
</ul>

<p><b>Visualizações:</b></p>
<ul>
    <li>Mapa de calor (heatmap) relacionando fatores de suporte da empresa com a busca por tratamento;</li>
    <li>Boxplot com a distribuição do score de suporte entre profissionais que buscaram ou não tratamento;</li>
    <li>Mapa de calor (heatmap) relacionando suporte organizacional e impacto no trabalho.</li>
</ul>

<p>Permite identificar se empresas com maior suporte organizacional estão associadas a uma maior busca por tratamento e a um menor impacto da saúde mental no desempenho.</p>

<h3>🧠 3. Ambiente & Cultura</h3>

<p><b>Objetivo:</b> Compreender como o suporte organizacional influencia a criação de um ambiente seguro para discussão de saúde mental.</p>

<p><b>Indicadores:</b></p>
<ul>
    <li>Nível de abertura para discussão com colegas;</li>
    <li>Nível de abertura para discussão com supervisores.</li>
</ul>

<p><b>Visualizações:</b></p>
<ul>
    <li>Mapa de calor (heatmap) relacionando fatores de suporte da empresa com a disposição em discutir problemas de saúde mental.</li>
</ul>

<p>Permite avaliar se o suporte organizacional contribui para um ambiente mais seguro e aberto ao diálogo.</p>

<h3>⚠️ 4. Medo & Carreira</h3>

<p><b>Objetivo:</b> Analisar como o medo e a percepção de consequências negativas impactam o comportamento dos profissionais.</p>

<p><b>Indicadores:</b></p>
<ul>
    <li>Percepção de consequências negativas ao discutir saúde mental;</li>
    <li>Disposição em abordar saúde mental em entrevistas.</li>
</ul>

<p><b>Visualizações:</b></p>
<ul>
    <li>Mapa de calor (heatmap) relacionando medo de consequências e busca por tratamento;</li>
    <li>Mapa de calor (heatmap) relacionando suporte organizacional e disposição em abordar saúde mental em entrevistas.</li>
</ul>

<p>Permite identificar barreiras culturais e sociais que impactam a busca por ajuda e a comunicação no ambiente profissional.</p>

<h2>📊 Indicadores Sintéticos</h2>

<ul>
    <li>Percentual de profissionais que buscaram tratamento;</li>
    <li>Percentual de profissionais que relatam impacto no trabalho;</li>
    <li>Percentual com histórico familiar de doenças mentais.</li>
</ul>

<p>Esses indicadores fornecem uma visão consolidada da situação da saúde mental no ambiente de trabalho, permitindo análises comparativas e identificação de padrões.</p>

## Planejamento das Tarefas
| Tarefa | Responsável | Status |
|--------|-------------|--------|
| Criação do repositório | Fabiana | ✅ Concluído |
| Criação do README | Fabiana | ✅ Concluído |
| Definição da base de dados | Giovanna/Vinicius | ✅ Concluído |
| Descrever brevemente o contexto | Estéfano | ✅ Concluído |
| Descrever brevemente o objetivo da análise | Estéfano | ✅ Concluído |
| Ideia inicial do dashboard | Leonardo | ✅ Concluído |