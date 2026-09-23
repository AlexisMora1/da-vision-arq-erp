# Workflow: Cargar factura

## Objetivo

Conservar una factura existente y relacionarla con el contexto comercial y financiero correcto.

## Actor

Administrador de la empresa.

## Precondiciones

* El tenant está identificado.
* La contraparte existe: cliente para una factura de venta o proveedor para una factura de compra.
* El proyecto u orden relacionados existen cuando se informa esa relación.

## Flujo principal

1. El usuario elige factura de venta o factura de compra.
2. Selecciona proyecto, cliente/proveedor y, si existe, la orden relacionada.
3. Captura número, fecha, moneda, total y demás metadatos disponibles.
4. Adjunta el PDF u otro archivo soportado.
5. El sistema valida el archivo, guarda su referencia y crea la factura estructurada.
6. El sistema calcula el saldo inicial como total de la factura.

## Reglas

* Cargar una factura no registra por sí mismo un cobro o pago.
* La generación automática de facturas está fuera del MVP.
* La factura puede existir sin orden cuando se trata de un documento histórico o no ordenado.
* La relación con una orden debe ser opcional, explícita y trazable.
* El estado se deriva del total pagado: sin pago, parcialidad o pagada.

## Resultado

Factura consultable desde el proyecto, la contraparte y la orden asociada, con archivo original y saldo pendiente.

## Rechazos

* Archivo inválido o perteneciente a otro tenant.
* Total negativo o datos obligatorios incompletos.
* Relación con una orden de otro tenant o de una contraparte incompatible.