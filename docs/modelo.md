Modelo de Datos

Objetivo
Organizar la información de préstamos en un **modelo tipo estrella** que permita analizar montos, zonas y estados de los préstamos de manera rápida y sencilla.

--------------------------------------------------------------------------------

Tablas

1. fact_loans
Registra los datos principales de cada préstamo.

| Columna | Descripción |
|----------|-------------|
| loan_id | Identificador del préstamo |
| client_id | Cliente asociado |
| branch_id | Sucursal del préstamo |
| date_id | Fecha del préstamo |
| amount | Monto otorgado |
| interest_rate | Tasa de interés |
| total_payable | Total a pagar (monto + interés) |
| status | Estado del préstamo (activo, cerrado, en mora) |

--------------------------------------------------------------------------------

2. dim_branch
Información de las sucursales.

| Columna | Descripción |
|----------|-------------|
| branch_id | Identificador de la sucursal |
| branch_name | Nombre de la sucursal |
| zone | Zona geográfica (Norte, Sur, Este, Oeste) |

--------------------------------------------------------------------------------

3. dim_date
Permite analizar los préstamos por periodo de tiempo.

| Columna | Descripción |
|----------|-------------|
| date_id | Identificador único (YYYYMMDD) |
| date | Fecha completa |
| year | Año |
| month | Mes |

--------------------------------------------------------------------------------

Relaciones
- `fact_loans.branch_id` → `dim_branch.branch_id`
- `fact_loans.date_id` → `dim_date.date_id`

--------------------------------------------------------------------------------

## Justificación
El modelo estrella facilita consultas por zona, sucursal o fecha.
Es simple, eficiente y permite usar herramientas de BI como Power BI o QuickSight.

