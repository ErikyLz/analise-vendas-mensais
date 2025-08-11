# Análise de Vendas (vendas mensais)

Projeto simples para gerar um gráfico de vendas mensais a partir de um arquivo CSV usando Python, Pandas e Matplotlib.

## O que faz
- Carrega um CSV com dados de venda.
- Faz limpeza básica (ajusta nomes de colunas, converte datas).
- Agrupa vendas por mês e gera um gráfico de vendas mensais.

## Estrutura do projeto
- limpeza.py — carrega o CSV e faz limpeza/normalização das colunas (ex.: converter strings de data para datetime).
- analise.py — agrupa por mês, calcula soma/total e gera o gráfico.
- app.py — orquestra a execução (chama limpeza e análise) e imprime/mostra o resultado.

## Requisitos
- Python
- Bibliotecas: pandas, matplotlib

Você pode criar um requirements.txt com:
pandas
matplotlib

## Como rodar (exemplo)
1. Criar ambiente (opcional):
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt

2. Coloque seu CSV na pasta do projeto (ex.: dados/vendas.csv).

3. Rodar:
python app.py

(O app.py deve aceitar o caminho do arquivo ou ter uma variável com o nome do CSV.)

## Formato esperado do CSV (mínimo)
O script espera colunas com data e valor. Exemplos de nomes comuns:
- date, data
- amount, valor, sales

Se as colunas tiverem nomes diferentes, limpeza.py ajusta/renomeia antes da análise.

## Exemplo de saída
- Um DataFrame agrupado por mês (soma das vendas) impresso no console.
- Um gráfico (matplotlib) exibindo vendas por mês.

## Observações

Este projeto foi desenvolvido com o auxílio de ferramentas automatizadas para agilizar a codificação.
O importante é que o código funciona e que você compreenda seu funcionamento.
O uso dessas ferramentas é comum na indústria e não diminui o valor do projeto.
