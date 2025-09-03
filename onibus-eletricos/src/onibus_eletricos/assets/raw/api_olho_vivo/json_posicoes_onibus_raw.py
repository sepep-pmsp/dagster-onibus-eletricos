from dagster import(
    asset,
#    AssetCheckExecutionContext,
    Output,
#    AssetCheckResult,
#    AssetCheckSpec,
    AutomationCondition
)
import time

@asset(
    required_resource_keys= {
        "api_olho_vivo"
    },
    group_name = "raw",
#    check_specs=[
#        AssetCheckSpec(name="features_not_empty", asset="geojson_tis_poligonais_portarias"),
#        AssetCheckSpec( name="total_features_downloaded_features", blocking=True, asset="geojson_tis_poligonais_portarias"),
#    ],
#    automation_condition=AutomationCondition.eager(),
    tags={
        "tier" : "raw", #?
        "fonte": "api_olho_vivo", #?
        "tipo": "json"#?
    }
)

def json_posicoes_onibus_raw(context):
    api = context.resources.api_olho_vivo
    return api