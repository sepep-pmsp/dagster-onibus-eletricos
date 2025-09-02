from dagster import Definitions

#Raw - APIOlhoVivo
from .raw.api_olho_vivo.json_posicoes_onibus_raw import json_posicoes_onibus_raw

defs= Definitions(
    sensors=[],
    assets=[
        #Raw
        json_posicoes_onibus_raw,
    ]
)