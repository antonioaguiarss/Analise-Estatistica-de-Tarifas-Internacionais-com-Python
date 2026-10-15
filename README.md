🌎 Análise Estatística de Tarifas Internacionais

Análise em Python de custos de frete por embarque em rotas internacionais entre EUA, Canadá e México, ao longo de oito trimestres (2024–2025). O objetivo é descobrir quais rotas têm custos mais instáveis e quais valores fogem do padrão e merecem ser investigados.

⚠️ Projeto educacional. Todos os valores são fictícios e não representam cotações reais de mercado.

Por que este projeto existe

Olhar só a média de custo de uma rota esconde uma informação importante: o quanto esse custo oscila. Uma rota com média baixa, mas que varia muito de um trimestre para outro, é mais difícil de orçar e negociar do que uma rota um pouco mais cara e estável. Este projeto mede essa instabilidade e aponta os valores atípicos de forma automática.

O que o projeto faz
Calcula média e mediana do custo por rota.
Mede a variação de cada rota: desvio padrão, amplitude e coeficiente de variação.
Detecta valores atípicos (outliers) pelo método do intervalo interquartil (IQR).
Exporta o resumo estatístico e a lista de outliers em CSV.
Gera um gráfico da evolução trimestral por rota e um boxplot comparando as rotas.

Métricas
Métrica	O que mostra	Como ler
Média	Custo médio por embarque, em USD	Nível de preço da rota
Mediana	Valor do meio quando os custos são ordenados	Parecida com a média, mas não é distorcida por poucos valores extremos
Desvio padrão	Quanto os custos se afastam da média, em USD	Quanto maior, mais o custo oscila em valor absoluto
Amplitude	Diferença entre o maior e o menor custo	Mostra o "pior cenário" de variação no período
Coeficiente de variação (CV)	Desvio padrão ÷ média, em %	Permite comparar a instabilidade de rotas caras e baratas na mesma régua

Por que usar o CV além do desvio padrão

Uma variação de USD 300 é muito para uma rota que custa USD 1.000, mas pouco para uma que custa USD 10.000. O desvio padrão trataria as duas igualmente; o CV não:

Exemplo: rota A com média de USD 1.000 e desvio de USD 300 → CV = 30%. Rota B com média de USD 10.000 e desvio de USD 300 → CV = 3%. A rota A é proporcionalmente dez vezes mais instável.

Como os outliers são identificados

O método IQR olha para a faixa onde fica a metade "central" dos custos de cada rota:

Ordena os custos e encontra o Q1 (valor abaixo do qual estão 25% dos dados) e o Q3 (abaixo do qual estão 75%).
Calcula o IQR = Q3 − Q1, o tamanho dessa faixa central.
Marca como outlier qualquer valor abaixo de Q1 − 1,5 × IQR ou acima de Q3 + 1,5 × IQR.

Em outras palavras: um valor é atípico quando fica muito longe da faixa onde os custos normalmente estão.

Como interpretar os resultados
Maior desvio padrão: a rota que mais oscila em dólares.
Maior CV: a rota que mais oscila em relação ao próprio custo médio, normalmente a mais difícil de prever.
Outlier: um sinal para investigar, não uma prova de erro. Pode ser explicado por sazonalidade, preço do combustível, congestionamento em portos ou fronteiras, mudança de serviço, sobretaxas ou erro de registro.
Resultados

Show Image

Show Image

<!-- Sugestão: resuma aqui as principais conclusões, por exemplo: - A rota X teve o maior CV (...%), ou seja, foi a mais instável. - Foram encontrados N outliers, concentrados na rota Y no trimestre Z. -->
Como executar

Pré-requisito: Python 3.10 ou superior.

bash
pip install -r requirements.txt
python src/analise_tarifas.py

O script lê dados/tarifas_ficticias.csv e recria os arquivos das pastas outputs/ e images/.

Estrutura do projeto
analise_tarifas_internacionais/
├── dados/
│   └── tarifas_ficticias.csv      # custo por embarque, por rota e trimestre
├── images/
│   ├── boxplot_tarifas.png        # comparação da distribuição entre rotas
│   └── tarifas_por_rota.png       # evolução trimestral por rota
├── outputs/
│   ├── outliers_iqr.csv           # valores atípicos encontrados
│   └── resumo_estatistico.csv     # métricas por rota
├── src/
│   └── analise_tarifas.py         # script principal
├── requirements.txt
└── README.md
Limitações
Os dados são fictícios e servem apenas para demonstração.
Cada rota tem só oito observações (uma por trimestre). Com tão poucos dados, as conclusões são exploratórias e não servem como previsão.
O custo está em USD por embarque e não leva em conta diferenças de peso, volume, Incoterm (regra que define quem paga e quem assume o risco em cada etapa do transporte), tipo de contêiner, transportadora ou nível de serviço. Duas rotas podem parecer diferentes apenas porque transportam cargas diferentes.
Tecnologias

Antonio Aguiar · GitHub · LinkedIn
