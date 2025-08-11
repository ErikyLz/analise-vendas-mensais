import pandas as pd

def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df

def corrigir_dados(df):
    print(df.columns)
    df.columns = df.columns.str.strip()

    if 'data_venda' in df.columns:
        df['data_venda'] = pd.to_datetime(df['data_venda'])
    else:
        print("Coluna 'data_venda' não encontrada no DataFrame.")
    return df
