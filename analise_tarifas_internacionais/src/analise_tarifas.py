"""
Análise estatística de tarifas internacionais fictícias.
Uso:
    python src/analise_tarifas.py
Dependências: pandas, numpy, matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados" / "tarifas_ficticias.csv"
OUT = ROOT / "outputs"
IMG = ROOT / "images"
OUT.mkdir(exist_ok=True)
IMG.mkdir(exist_ok=True)

def detectar_outliers_iqr(grupo):
    """Detecta valores fora de Q1 - 1,5*IQR e Q3 + 1,5*IQR."""
    q1 = grupo["custo_usd"].quantile(0.25)
    q3 = grupo["custo_usd"].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return grupo[
        (grupo["custo_usd"] < limite_inferior) |
        (grupo["custo_usd"] > limite_superior)
    ].assign(
        limite_inferior=limite_inferior,
        limite_superior=limite_superior
    )

def main():
    df = pd.read_csv(DATA)
    df["custo_usd"] = pd.to_numeric(df["custo_usd"], errors="coerce")
    df = df.dropna(subset=["rota", "trimestre", "custo_usd"])

    resumo = df.groupby("rota").agg(
        observacoes=("custo_usd", "count"),
        media_usd=("custo_usd", "mean"),
        mediana_usd=("custo_usd", "median"),
        desvio_padrao_usd=("custo_usd", "std"),
        minimo_usd=("custo_usd", "min"),
        maximo_usd=("custo_usd", "max"),
    ).reset_index()
    resumo["coeficiente_variacao_pct"] = (
        resumo["desvio_padrao_usd"] / resumo["media_usd"] * 100
    )
    resumo["amplitude_usd"] = resumo["maximo_usd"] - resumo["minimo_usd"]
    resumo = resumo.sort_values("coeficiente_variacao_pct", ascending=False)
    resumo.to_csv(OUT / "resumo_estatistico.csv", index=False, float_format="%.2f")

    outliers = pd.concat(
        [detectar_outliers_iqr(g) for _, g in df.groupby("rota")],
        ignore_index=True
    )
    outliers.to_csv(OUT / "outliers_iqr.csv", index=False, float_format="%.2f")

    # Gráfico de evolução por trimestre
    plt.figure(figsize=(11, 6))
    for rota, grupo in df.groupby("rota"):
        grupo = grupo.sort_values("trimestre")
        plt.plot(grupo["trimestre"], grupo["custo_usd"], marker="o", label=rota)
    plt.xticks(rotation=35, ha="right")
    plt.xlabel("Trimestre")
    plt.ylabel("Custo por embarque (USD)")
    plt.title("Tarifas internacionais fictícias por rota")
    plt.legend(fontsize=8, ncol=2)
    plt.tight_layout()
    plt.savefig(IMG / "tarifas_por_rota.png", dpi=160)
    plt.close()

    # Boxplot para comparar dispersão e valores extremos
    rotas = resumo.sort_values("media_usd")["rota"].tolist()
    valores = [df.loc[df["rota"] == rota, "custo_usd"].values for rota in rotas]
    plt.figure(figsize=(11, 6))
    plt.boxplot(valores, labels=rotas, showmeans=True)
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Custo por embarque (USD)")
    plt.title("Distribuição dos custos por rota — boxplot")
    plt.tight_layout()
    plt.savefig(IMG / "boxplot_tarifas.png", dpi=160)
    plt.close()

    print("\\nResumo estatístico (rotas mais instáveis primeiro):")
    print(resumo.round(2).to_string(index=False))
    print("\\nOutliers detectados pelo método IQR:")
    if outliers.empty:
        print("Nenhum outlier detectado.")
    else:
        print(outliers.round(2).to_string(index=False))
    print("\\nArquivos gerados em outputs/ e images/.")

if __name__ == "__main__":
    main()
