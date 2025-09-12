import dagster as dg

posicao_onibus_por_minuto = dg.AssetSelection.assets(
    "dici_posicoes_onibus_raw",
    "df_posicoes_onibus_bronze"
)


job_posicao_onibus_por_minuto = dg.define_asset_job(
    name="job_posicao_onibus_por_minuto",
    selection=posicao_onibus_por_minuto
)
