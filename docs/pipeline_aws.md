Pipeline AWS

1. Los datos crudos (`loans.csv`, `branches.csv`) se almacenan en Amazon S3.
2. AWS Glue ejecuta un trabajo de limpieza: convierte fechas, calcula `total_payable` y elimina registros con `amount <= 0`.
3. Los datos limpios se guardan en S3 (zona curated).
4. Athena o Redshift consultan los datos para análisis.
5. Power BI o QuickSight se conectan para visualizar métricas.
6. La automatización se logra con EventBridge o Step Functions.