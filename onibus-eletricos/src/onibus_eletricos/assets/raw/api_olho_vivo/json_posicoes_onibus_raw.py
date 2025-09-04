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
        "api_olho_vivo",
        "localhost_data_saver"
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
    context.resources.localhost_data_saver.save_json(posicao_atual, f"posicoes_onibus_{hora_req}_raw.json")
    context.log.info(f"Saved raw bus position data at hour: {hora_req}.")
    return posicao_atual