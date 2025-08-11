from scripts.limpeza import carregar_dados, corrigir_dados
from scripts.analise import analise_vendas

def main():
    df = carregar_dados('./data/raw/vendas.csv')
    df_corrigido = corrigir_dados(df)
    vendas_mes = analise_vendas(df_corrigido)
    print(vendas_mes)

if __name__ == "__main__":
    main()