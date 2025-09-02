from dagster import Definitions

#Resources
from .resources.api_olho_vivo import APIOlhoVivoClient

defs = Definitions(
    jobs=[
    ],
    sensors=[
        
    ],
    resources={
        # API olho vivo
        "api_olho_vivo": APIOlhoVivoClient(
                    token='7c54257f14ee2043182985954596f0b6c6cda242e6447f817338f45f29a593c0'
        )
    }
)


####
# from pathlib import Path

#from dagster import definitions, load_from_defs_folder


#@definitions
#def defs():
#    return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)
