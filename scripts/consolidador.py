import pandas as pd
import glob
import os

# Define os caminhos das pastas usando caminhos relativos
pasta_origem = r'../data/input'
arquivo_destino = r'../data/output/base_consolidada.csv'

# Localiza todos os arquivos Excel na pasta de origem
arquivos = glob.glob(os.path.join(pasta_origem, "*.xlsx"))
lista_dataframes = []

print(f"Encontrados {len(arquivos)} arquivos. Iniciando consolidação...")

# Lê cada arquivo e guarda na lista
for arquivo in arquivos:
    # Lê a planilha
    df = pd.read_excel(arquivo)
    
    # Cria uma coluna rastreando de qual arquivo aquele dado veio
    df['arquivo_origem'] = os.path.basename(arquivo)
    
    lista_dataframes.append(df)

# Verifica se a lista tem algum dado antes de tentar juntar
if not lista_dataframes:
    print("Aviso: Nenhum arquivo .xlsx foi encontrado na pasta de origem. Nenhuma ação realizada.")
else:
    # Se a lista não estiver vazia, faz a consolidação normalmente
    df_consolidado = pd.concat(lista_dataframes, ignore_index=True)
    
    # Verifica se o arquivo final já existe.
    if not os.path.isfile(arquivo_destino):
        # Se NÃO existir, cria o arquivo pela primeira vez (com o cabeçalho)
        df_consolidado.to_csv(arquivo_destino, index=False, sep=';', encoding='utf-8')
        print("Novo arquivo criado e consolidação concluída! Salvo em:", arquivo_destino)
    else:
        # Se JÁ existir, adiciona as novas linhas no final sem repetir o cabeçalho
        df_consolidado.to_csv(arquivo_destino, index=False, sep=';', encoding='utf-8', mode='a', header=False)
        print("Novos dados adicionados ao arquivo existente com sucesso! Salvo em:", arquivo_destino)