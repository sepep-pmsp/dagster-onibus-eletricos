from dagster import(
    asset,
    Output,
    AssetIn,
)
from pydantic import BaseModel
import pandas as pd
from datetime import (
    datetime,
    time
)

class Onibus(BaseModel):
    hora_requisicao: time
    codigo_linha: int #str
    nome_linha: str
    letreiro: str
    codigo_onibus: int #str
    x: float
    y: float
    hora_gps: datetime


@asset(
    required_resource_keys= {
        "api_olho_vivo",
        "localhost_bronze_data"
    },
    group_name = "bronze",
    tags={
        "tier" : "bronze",
        "fonte": "api_olho_vivo",
        "tipo": "csv"
    },
    ins={
        "dici_posicoes_onibus_raw" : AssetIn(key="dici_posicoes_onibus_raw"),
    },
)

def df_posicoes_onibus_bronze(
        context,
        dici_posicoes_onibus_raw:dict
)->pd.DataFrame:
    
    dici_posicoes=dici_posicoes_onibus_raw
    context.log.info(dici_posicoes)

    hora_requisicao = datetime.strptime(dici_posicoes['hr'], "%H:%M").time()
    context.log.info(hora_requisicao)
    
    linhas = dici_posicoes['l']
    dados_parsed = []
    for linha in linhas:
        codigo_linha = linha['cl']
        nome_linha = linha['c']
        letreiro = ' - '.join([linha['lt0'], linha['lt1']])
        for onibus in linha['vs']:
            codigo_onibus=onibus['p']
            y = onibus['py']
            x = onibus['px']
            hora_gps = datetime.fromisoformat(onibus['ta'])

            parsed = {
                'hora_requisicao' : hora_requisicao,
                'codigo_linha' : codigo_linha,
                'nome_linha' : nome_linha,
                'letreiro' : letreiro,
                'codigo_onibus' : codigo_onibus,
                'x' : x,
                'y' : y,
                'hora_gps' : hora_gps
            }

            teste = Onibus(**parsed)

            dados_parsed.append(teste.model_dump())

    df = pd.DataFrame(dados_parsed)

    #fazer um save_csv no data saver

    return df