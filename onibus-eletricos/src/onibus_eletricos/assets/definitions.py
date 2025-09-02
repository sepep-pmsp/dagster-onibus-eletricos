from dagster import Definitions

#Raw - APIOlhoVivo
from .raw.api_olho_vivo.ainda_n_sei_nome import ainda_n_sei_nome

defs= Definitions(
    sensors=[],
    assets=[
        #Raw
        ainda_n_sei_nome
    ]
)