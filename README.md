# Pipeline ETL e Dashboard de Vendas

## Sobre o Projeto
Este projeto demonstra a construção de uma arquitetura de dados, desde a extração até a visualização analítica. O objetivo principal é automatizar o processo de consolidação de relatórios mensais de vendas (arquivos Excel) e transformar esses dados brutos em inteligência de negócio através de um dashboard interativo, substituindo rotinas manuais demoradas por um fluxo escalável.

## Tecnologias Utilizadas
* Linguagem: Python (bibliotecas: Pandas, OS, Glob)
* Ferramenta de BI: Power BI
* Tratamento e Modelagem: Power Query, DAX e Star Schema

## Arquitetura e Fluxo de Dados
1. Extração (Extract): O script Python varre a pasta de input em busca de relatórios mensais em formato .xlsx.
2. Transformação (Transform): Os dados são limpos, padronizados e uma coluna de rastreabilidade de origem é adicionada utilizando a biblioteca Pandas.
3. Carga (Load): O script consolida os dados de forma incremental e salva um arquivo único no formato .csv.
4. Visualização: O Power BI consome o arquivo consolidado, relaciona as tabelas (Fato e Dimensões) e exibe os KPIs de performance corporativa.

## Estrutura do Repositório
* /assets: Capturas de tela das páginas do dashboard.
* /dashboards: Arquivo .pbix contendo o painel interativo.
* /data/input: Pasta destinada aos relatórios brutos mensais (arquivos Excel).
* /data/output: Pasta onde o script salva a base consolidada (arquivo CSV).
* /scripts: Código fonte em Python (consolidador.py) responsável pelo pipeline ETL.

## Como Executar
1. Clone esse repositório em sua máquina local.
2. Tenha o Python e a biblioteca Pandas instalados.
3. Pelo terminal, navegue até a pasta scripts e execute o comando: python consolidador.py
4. Após a mensagem de sucesso no terminal, abra o arquivo .pbix contido na pasta dashboards usando o Power BI Desktop.
5. Caso necessário, atualize as credenciais de fonte de dados no Power BI apontando para a pasta local /data/output/base_consolidada.csv.
