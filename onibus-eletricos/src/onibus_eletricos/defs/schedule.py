import dagster as dg

from .jobs import (
    job_posicao_onibus_por_minuto,

)

schedule_posicao_onibus_por_minuto = dg.ScheduleDefinition(
    job=job_posicao_onibus_por_minuto,
    cron_schedule="* * * * *",  # a cada minuto
)
