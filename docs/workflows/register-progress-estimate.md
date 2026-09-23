# Workflow: Registrar avance y generar estimación

## Objetivo

Separar el avance real de un proyecto de la preparación y aprobación del documento de estimación.

## Actor

Administrador de la empresa o responsable autorizado del proyecto.

## Precondiciones

* El proyecto existe y pertenece al tenant.
* Las partidas o sets que reciben avance pueden identificarse.

## Flujo principal

1. El usuario registra un avance para una partida o set, con fecha, cantidad o porcentaje y evidencia opcional.
2. El sistema conserva el avance como histórico y actualiza el acumulado ejecutado.
3. Cuando corresponde, el usuario selecciona avances para preparar una estimación.
4. El sistema genera un borrador con partidas, periodo, cantidades e importe.
5. El usuario revisa y adjunta el documento de estimación.
6. El usuario aprueba o rechaza el borrador.
7. Solo una estimación aprobada puede actualizar el monto estimado o el saldo por cobrar según la regla comercial configurada.

## Reglas

* Registrar avance no genera automáticamente factura, cobro ni ingreso.
* Un avance puede acumularse en varias capturas.
* Una estimación rechazada no afecta saldos.
* La aprobación debe ser explícita y auditable.
* “Terminado” e “instalado” son estados distintos hasta que el cliente confirme lo contrario.

## Resultado

Historial de avance y, cuando aplique, una estimación aprobada vinculada al proyecto, sus partidas y su documento fuente.

## Pendientes de negocio

* Definir si el importe aprobado incrementa por cobrar, genera una factura o solo representa avance.
* Confirmar el significado de OT/Subcontrato y su relación con este workflow.
* Definir si una partida puede estimarse más de una vez y cómo se evitan duplicidades.