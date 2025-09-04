from dagster import Definitions

#Resources
from .resources.env_variables import OLHO_VIVO_TOKEN
from .resources.api_olho_vivo import APIOlhoVivoClient
from .resources.localhost_data import LocalhostDataSaver

#Jobs
from .defs.jobs import job_posicao_onibus_por_minuto

#Schedules
from .defs.schedule import schedule_posicao_onibus_por_minuto

#Assets
## Raw - APIOlhoVivo
from .assets.raw.api_olho_vivo.json_posicoes_onibus_raw import dici_posicoes_onibus_raw


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
        "localhost_raw_data_saver": LocalhostDataSaver(tier='raw'),
        "localhost_bronze_data_saver": LocalhostDataSaver(tier='bronze'),
        "localhost_silver_data_saver": LocalhostDataSaver(tier='silver'),
        "localhost_gold_data_saver": LocalhostDataSaver(tier='gold'),
    },
    assets=[
        #Raw
        dici_posicoes_onibus_raw
    ]
)


####
# from pathlib import Path

#from dagster import definitions, load_from_defs_folder


#@definitions
#def defs():
#    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
