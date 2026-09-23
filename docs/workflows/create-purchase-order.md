# Workflow: Registrar orden de compra

## Objetivo

Registrar lo que la empresa acordó comprar a un proveedor.

## Actor

Administrador de la empresa.

## Precondiciones

* El proveedor existe.
* El proyecto existe cuando la compra se relaciona con un proyecto.
* Cada línea referencia un producto o servicio válido.

## Flujo principal

1. El usuario selecciona proveedor y proyecto, si aplica.
2. Captura fecha, moneda, condiciones de pago y líneas de la orden.
3. El sistema calcula el total de la orden.
4. El usuario confirma la orden.
5. El sistema crea la orden con estado de recepción pendiente y pago pendiente.
6. Opcionalmente se asocia después una factura recibida del proveedor.

## Reglas

* Crear la orden no aumenta inventario.
* Crear la orden no registra un egreso ni un pago.
* Recepción y pago son workflows independientes y pueden ocurrir parcialmente.
* La factura de proveedor puede cargarse a la orden existente; no es obligatorio crear la orden a partir de la factura.
* Una orden cancelada no puede recibir mercancía ni pagos nuevos, salvo una regla explícita del negocio.

## Resultado

Orden de compra trazable al proveedor y, cuando corresponda, al proyecto y documento de origen.

## Rechazos

* Proveedor o proyecto perteneciente a otro tenant.
* Línea inválida, cantidad no positiva o ausencia de líneas.
* Recepción o pago que exceda la cantidad o saldo pendiente.