import matplotlib.pyplot as plt
import os

def analise_vendas(df):
    df['ano'] = df['data_venda'].dt.year
    df['mes'] = df['data_venda'].dt.month

    nome_coluna_valor = None
    for col in df.columns:
        if 'preco_unitario' in col.lower():
            nome_coluna_valor = col
            break
    
    if not nome_coluna_valor:
        raise ValueError("Nenhuma coluna de valor encontrada. Verifique o nome no CSV.")

    vendas_mensais = df.groupby(['ano', 'mes'])[nome_coluna_valor].sum().reset_index()
    vendas_mensais['data'] = vendas_mensais.apply(lambda x: f"{int(x['ano'])}-{int(x['mes']):02d}", axis=1)

    plt.figure(figsize=(10,5))
    plt.plot(vendas_mensais['data'], vendas_mensais[nome_coluna_valor], marker='o')
    plt.title('Vendas por mês')
    plt.xlabel('Ano-Mês')
    plt.ylabel('Total de vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    os.makedirs('reports/figures', exist_ok=True)
    plt.savefig('reports/figures/vendas_por_mes.png')
    plt.show()
    return vendas_mensais


