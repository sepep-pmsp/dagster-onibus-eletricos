from dagster import Definitions

#Resources
from .resources.env_variables import OLHO_VIVO_TOKEN
from .resources.api_olho_vivo import APIOlhoVivoClient
from .resources.localhost_data import LocalhostData

#Jobs
from .defs.jobs import job_posicao_onibus_por_minuto

#Schedules
from .defs.schedule import schedule_posicao_onibus_por_minuto

#Assets
## Raw - APIOlhoVivo
from .assets.raw.api_olho_vivo.json_posicoes_onibus_raw import dici_posicoes_onibus_raw
## Bronze - APIOlhoVivo
from .assets.bronze.csv_posicoes_onibus_bronze import df_posicoes_onibus_bronze

defs = Definitions(
    jobs=[
        job_posicao_onibus_por_minuto,
    ],
    sensors=[
        
    ],
    schedules=[
        schedule_posicao_onibus_por_minuto

    ],
    resources={
        # API olho vivo
        "api_olho_vivo": APIOlhoVivoClient(
                    token=OLHO_VIVO_TOKEN
        ),
        "localhost_raw_data": LocalhostData(tier='raw'),
        "localhost_bronze_data": LocalhostData(tier='bronze'),
        "localhost_silver_data": LocalhostData(tier='silver'),
        "localhost_gold_data": LocalhostData(tier='gold'),
    },
    assets=[
        #Raw
        dici_posicoes_onibus_raw,
        df_posicoes_onibus_bronze,
    ]
)


####
# from pathlib import Path

#from dagster import definitions, load_from_defs_folder


#@definitions
#def defs():
#    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
