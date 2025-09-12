from dagster import(
    asset,
    Output,
    AssetIn,
)
import pandas as pd
from datetime import date

@asset(
    required_resource_keys={
        "localhost_silver_data"
    },
    group_name="silver",
    tags={
        "tier":"silver",
        "fonte": "",
        "tipo": "csv"
    },
    deps=[
        "df_posicoes_onibus_bronze",
    ] # coloquei como deps e não como ins pq não precisa do asset, mas dos arquivos que o asset retorna.
)

def df_posicoes_onibus_diario_silver(
    context,
    df_posicoes_onibus_bronze:pd.DataFrame
)->None:#pd.DataFrame:
    df_posicoes = df_posicoes_onibus_bronze
    context.log.info(df_posicoes.sample())
    
    # Metadados? colunas? asset separado?
    hora_requisicao = df_posicoes['hora_requisicao'][0]
    context.log.info(hora_requisicao)

    hora_req = str(hora_requisicao).replace(":", "-")
    date_req = date.today().strftime('%Y-%m-%d')

    return print('Teste das lineage de assets')
    


