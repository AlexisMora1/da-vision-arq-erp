# Workflow: Registrar cobro o pago

## Objetivo

Registrar un movimiento real de dinero y aplicarlo a una factura, una orden o una operación independiente.

## Actor

Administrador de la empresa.

## Precondiciones

* La factura o contraparte relacionada existe, si se está aplicando el movimiento a una operación.
* El medio de pago y la fecha están disponibles.
* El importe es positivo.

## Flujo principal

1. El usuario elige cobro de cliente o pago a proveedor.
2. Busca el proyecto, factura u orden relacionada.
3. Captura importe, fecha, medio, referencia y notas.
4. Opcionalmente adjunta el comprobante.
5. El sistema crea el movimiento financiero.
6. El sistema aplica el importe a la factura y recalcula el saldo.
7. El sistema deriva el estado: sin pago, parcialidad o pagada.

## Reglas

* El importe aplicado no puede exceder el saldo pendiente, salvo que el negocio defina explícitamente anticipos o sobrantes.
* Los pagos parciales son válidos.
* El movimiento financiero se conserva aunque posteriormente se corrija mediante una operación de reversa; no se borra el historial.
* Registrar un cobro o pago no modifica inventario.
* Un movimiento sin factura puede registrarse como ingreso o egreso independiente cuando el negocio lo permita.

## Resultado

Movimiento financiero trazable, saldo actualizado y estado de la factura derivado del saldo.

## Rechazos

* Importe cero, negativo o mayor al saldo permitido.
* Factura ya cancelada o perteneciente a otro tenant.
* Tipo de movimiento incompatible con la factura.