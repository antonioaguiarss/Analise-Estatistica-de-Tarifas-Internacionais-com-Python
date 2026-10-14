# Análise Estatística de Tarifas Internacionais (Python)

Projeto de portfólio com uma base **100% fictícia** de custos por embarque em rotas internacionais envolvendo EUA, Canadá e México, ao longo de oito trimestres (2024–2025).

## Objetivo
Demonstrar como Python pode transformar dados de frete em indicadores que ajudam a identificar rotas com custos mais instáveis e valores atípicos que merecem investigação.

## O que o projeto faz
- Calcula média e mediana por rota.
- Calcula desvio padrão amostral e amplitude (máximo - mínimo).
- Calcula coeficiente de variação (CV) para comparar instabilidade relativa entre rotas com níveis de custo diferentes.
- Detecta outliers pelo método do intervalo interquartil (IQR): abaixo de Q1 - 1,5 × IQR ou acima de Q3 + 1,5 × IQR.
- Gera CSVs com o resumo estatístico e os outliers.
- Gera gráficos de evolução trimestral e boxplot.

## Estrutura
```text
analise_tarifas_internacionais/
├── dados/
│   └── tarifas_ficticias.csv
├── images/
│   ├── boxplot_tarifas.png
│   └── tarifas_por_rota.png
├── outputs/
│   ├── outliers_iqr.csv
│   └── resumo_estatistico.csv
├── src/
│   └── analise_tarifas.py
├── requirements.txt
└── README.md
```

## Como executar
Requer Python 3.10+.

```bash
pip install -r requirements.txt
python src/analise_tarifas.py
```

O script lê `dados/tarifas_ficticias.csv` e recria os arquivos em `outputs/` e `images/`.

## Métricas principais
- **Média:** custo médio por embarque.
- **Desvio padrão:** dispersão absoluta dos custos; maior valor indica maior variação em USD.
- **Coeficiente de variação (CV):** desvio padrão dividido pela média, em percentual. É útil para comparar instabilidade relativa entre rotas de escalas diferentes.
- **IQR:** intervalo entre o terceiro e o primeiro quartil, usado para marcar valores atípicos.

## Como interpretar
A rota com maior desvio padrão tem maior variação absoluta em USD; a rota com maior CV tem maior instabilidade proporcional ao seu custo médio. Um outlier é um sinal para investigar, não prova de erro: pode refletir sazonalidade, combustível, congestionamento, alteração de serviço, sobretaxas ou erro de registro.

## Limitações
- Os dados são fictícios e servem apenas para demonstração.
- Há oito observações trimestrais por rota; conclusões são exploratórias e não devem ser tratadas como previsão.
- O custo está expresso em USD por embarque e não controla diferenças de peso, volume, Incoterm, tipo de contêiner, transportadora ou nível de serviço.

## Tecnologias
Python, pandas, NumPy e Matplotlib.

## Ideia para apresentar em entrevista
“Criei uma análise em Python para comparar a estabilidade dos custos de frete por rota. Além da média e do desvio padrão, usei o coeficiente de variação para comparar rotas com custos-base diferentes e o método IQR para destacar observações atípicas. O resultado é um relatório reproduzível que direciona a investigação para as rotas e períodos com maior volatilidade.”

---
**Aviso:** todos os valores desta base são inventados para fins educacionais e não representam cotações reais de mercado.
