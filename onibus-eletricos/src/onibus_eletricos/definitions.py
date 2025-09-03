from dagster import Definitions

#Resources
from .resources.api_olho_vivo import APIOlhoVivoClient

#Jobs
from .defs.jobs import job_posicao_onibus_por_minuto

#Schedules
from .defs.schedule import schedule_posicao_onibus_por_minuto

#Assets
## Raw - APIOlhoVivo
from .assets.raw.api_olho_vivo.json_posicoes_onibus_raw import json_posicoes_onibus_raw


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
                    token='7c54257f14ee2043182985954596f0b6c6cda242e6447f817338f45f29a593c0'
        )
    },
    assets=[
        #Raw
        json_posicoes_onibus_raw
    ]
)


####
# from pathlib import Path

#from dagster import definitions, load_from_defs_folder


#@definitions
#def defs():
#    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
