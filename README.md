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

## Planejamento das Tarefas
| Tarefa | Responsável | Status |
|--------|-------------|--------|
| Criação do repositório | Fabiana | ✅ Concluído |
| Criação do README | Fabiana | ✅ Concluído |
| Definição da base de dados | Giovanna/Vinicius | ✅ Concluído |
| Descrever brevemente o contexto | Estéfano | ✅ Concluído |
| Descrever brevemente o objetivo da análise | Estéfano | ✅ Concluído |
| Ideia inicial do dashboard | Leonardo | ✅ Concluído |

## Ideia Inicial do Dashboard
<p>O dashboard foi desenvolvido utilizando Streamlit, permitindo a visualização interativa dos dados diretamente no navegador.</p>

<h2>📈 Indicadores e Visualizações</h2>

<h3>1. Proporção de profissionais que buscaram tratamento</h3>
<p>Gráfico de barras que apresenta a distribuição entre profissionais que buscaram e não buscaram tratamento psicológico.</p>

<h3>2. Impacto da saúde mental no desempenho profissional</h3>
<p>Visualização que demonstra como os entrevistados percebem o impacto de problemas de saúde mental no trabalho.</p>

<h3>3. Distribuição por gênero dos profissionais que buscaram tratamento</h3>
<p>Comparativo entre gêneros para identificar padrões de busca por apoio psicológico.</p>

<h2>4. Relação entre benefícios e impacto no trabalho</h2>
<p>Mapa de calor (heatmap) que cruza:</p>

<ul>
    <li>Benefícios oferecidos pelas empresas;</li>
    <li>Impacto percebido no desempenho.</li>
</ul>

<p>Permitindo identificar possíveis correlações entre suporte organizacional e bem-estar.</p>

<h2>📊 Indicadores Sintéticos</h2>
<ul>
    <li>Percentual de profissionais que buscaram tratamento;</li>
    <li>Percentual de profissionais que relatam impacto no trabalho;</li>
    <li>Percentual com histórico familiar de doenças mentais.</li>
</ul>


