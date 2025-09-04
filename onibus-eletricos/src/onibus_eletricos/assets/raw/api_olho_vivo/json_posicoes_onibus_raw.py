from dagster import(
    asset,
#    AssetCheckExecutionContext,
    Output,
#    AssetCheckResult,
#    AssetCheckSpec,
    AutomationCondition
)
import time
import pandas as pd

@asset(
    required_resource_keys= {
        "api_olho_vivo",
        "localhost_raw_data_saver"
    },
    group_name = "raw",
#    check_specs=[
#        AssetCheckSpec(name="features_not_empty", asset="geojson_tis_poligonais_portarias"),
#        AssetCheckSpec( name="total_features_downloaded_features", blocking=True, asset="geojson_tis_poligonais_portarias"),
#    ],
#    automation_condition=AutomationCondition.eager(),
    tags={
        "tier" : "raw",
        "fonte": "api_olho_vivo",
        "tipo": "pickle"
    }
)
def dici_posicoes_onibus_raw(context)->dict:
    api = context.resources.api_olho_vivo
    posicao_atual = api.posicao_atual_onibus

    hora_req = posicao_atual['hr'].replace(":", "-")
    context.resources.localhost_raw_data_saver.save_json(posicao_atual, f"posicoes_onibus_{hora_req}_raw.json")
    context.log.info(f"Saved raw bus position data at hour: {hora_req}.")
    return posicao_atual


from pydantic import BaseModel
import pandas as pd
from datetime import datetime

class Onibus(BaseModel):
    hora_requisicao: datetime
    codigo_linha: str
    nome_linha: str
    letreiro: str
    codigo_onibus: str
    x: float
    y: float
    hora_gps: datetime


def df_posicoes_onibus(dici_posicoes:dict)->pd.DataFrame:

    hora_requisicao = datetime.fromisoformat(dici_posicoes['hr'])
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