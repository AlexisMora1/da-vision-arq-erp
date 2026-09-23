# Workflow: Registrar orden de venta

## Objetivo

Registrar lo que la empresa acordó vender a un cliente dentro de un proyecto.

## Actor

Administrador de la empresa.

## Precondiciones

* El cliente existe.
* El proyecto existe cuando la operación pertenece a un proyecto.
* Cada línea referencia un producto o servicio válido.

## Flujo principal

1. El usuario selecciona el proyecto y al cliente.
2. Captura fecha, moneda, condiciones comerciales y líneas de productos o servicios.
3. El sistema calcula subtotales, impuestos o cargos configurados y total.
4. El usuario confirma la orden.
5. El sistema crea la orden con estado comercial pendiente.
6. Opcionalmente se asocia una factura existente, sin confundirla con la orden.

## Reglas

* Crear la orden no descuenta inventario.
* Crear la orden no registra un ingreso ni un cobro.
* Las cantidades entregadas y cobradas se acumulan por separado.
* Los estados de entrega y cobro se derivan de sus propios acontecimientos.
* Una orden cancelada no puede recibir nuevas entregas, salvo una operación explícita de reactivación permitida por el negocio.

## Resultado

Orden de venta trazable al cliente y, cuando corresponda, al proyecto y a la cotización de origen.

## Rechazos

* Cliente o proyecto perteneciente a otro tenant.
* Línea sin producto/servicio, cantidad no positiva o precio inválido.
* Orden sin líneas.