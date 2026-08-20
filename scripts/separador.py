import pandas as pd
import os

# 1. Caminhos dos arquivos (ajuste o nome do seu arquivo original se for diferente)
arquivo_original = r'C:\Trabalho\Consolidador de Relatórios Administrativos\dataset_vendas_fake.xlsx'
pasta_destino = r'C:\Trabalho\Consolidador de Relatórios Administrativos\input'

print("Lendo a base de dados original. Isso pode levar alguns segundos...")
df = pd.read_excel(arquivo_original)

# 2. Converte a coluna 'Data' para o formato de data (ajustando para o padrão dia/mês/ano)
df['Data'] = pd.to_datetime(df['Data'])

# 3. Cria uma coluna temporária apenas para descobrir o Ano e o Mês de cada linha (ex: 2024_01)
df['Ano_Mes'] = df['Data'].dt.strftime('%Y_%m')

print("Iniciando a separação dos arquivos por mês...")

# 4. Agrupa os dados por mês e salva uma planilha para cada um
for periodo, dados_periodo in df.groupby('Ano_Mes'):
    
    # Remove a coluna temporária para não alterar a estrutura original
    dados_periodo = dados_periodo.drop(columns=['Ano_Mes'])
    
    # Monta o nome do arquivo (ex: vendas_2024_01.xlsx)
    nome_arquivo = f'vendas_{periodo}.xlsx'
    caminho_salvar = os.path.join(pasta_destino, nome_arquivo)
    
    # Salva o recorte lá dentro da sua pasta input
    dados_periodo.to_excel(caminho_salvar, index=False)
    print(f" -> Arquivo criado: {nome_arquivo} ({len(dados_periodo)} linhas)")

print("\nSucesso! Recortes gerados na pasta input.")