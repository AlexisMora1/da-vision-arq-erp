# Workflow: Crear proyecto

## Objetivo

Registrar un proyecto para agrupar la información comercial y operativa de una obra o servicio.

## Actor

Administrador de la empresa.

## Precondiciones

* El tenant está identificado.
* El cliente existe en el catálogo o puede registrarse durante el flujo.

## Flujo principal

1. El usuario selecciona crear proyecto.
2. Captura nombre, cliente, fechas relevantes, descripción y estado inicial.
3. Opcionalmente carga una cotización, contrato u otro documento fuente.
4. El sistema valida que el documento pertenece al tenant y conserva sus metadatos.
5. El sistema crea el proyecto y relaciona los documentos cargados.
6. El sistema muestra el proyecto sin crear órdenes, facturas, movimientos de inventario ni movimientos financieros.

## Reglas

* El nombre no es suficiente como identificador; el proyecto debe tener un identificador único por tenant.
* Un proyecto pertenece a un solo tenant.
* La cotización adjunta no genera saldos ni estados financieros.
* El proyecto puede crearse sin cotización para permitir operaciones históricas o casos en los que aún no existe el archivo.

## Resultado

Proyecto creado y disponible para asociar cotizaciones, órdenes, facturas, pagos, avances y documentos.

## Rechazos

* Cliente inexistente cuando el flujo exige un cliente válido.
* Documento no legible, no soportado o perteneciente a otro tenant.
* Datos obligatorios incompletos.