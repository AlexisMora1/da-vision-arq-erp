# ERP — Especificación funcional del MVP

## 1. Propósito

El objetivo del sistema es proporcionar una plataforma sencilla para que una empresa pueda administrar sus operaciones comerciales básicas desde un mismo lugar.

El sistema debe permitir registrar y dar seguimiento a:

* clientes y ventas;
* proveedores y compras;
* productos y movimientos de inventario;
* ingresos y egresos;
* cuentas por cobrar y por pagar;
* flujo de efectivo;
* proyectos, cotizaciones y documentos operativos asociados;
* avances y estimaciones de proyectos.

El ERP será **multi-tenant**: una misma aplicación podrá ser utilizada por diferentes empresas, manteniendo sus datos completamente separados.

El objetivo del MVP no es cubrir toda la operación contable, fiscal o administrativa de una empresa, sino establecer una base funcional que permita registrar las principales operaciones comerciales y sus efectos sobre el inventario, los proyectos y las finanzas.

---

# 2. Alcance del MVP

El MVP estará compuesto por las siguientes áreas principales:

| Área       | Propósito                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------- |
| Proyectos  | Agrupar la cotización, documentos, órdenes, facturas, pagos y avances de una obra o servicio |
| Ventas     | Registrar las operaciones de venta y dar seguimiento a su entrega y cobro                   |
| Compras    | Registrar las operaciones de compra y dar seguimiento a su recepción y pago                 |
| Inventario | Controlar las existencias mediante entradas y salidas                                       |
| Finanzas   | Registrar movimientos de dinero y mostrar cuentas por cobrar, por pagar y flujo de efectivo |
| Catálogo   | Administrar productos, servicios, clientes y proveedores reutilizables en las operaciones   |
| Documentos | Conservar archivos fuente, comprobantes y documentos comerciales relacionados con entidades |

El panel de control y sus gráficas se consideran una capa de consulta posterior. En esta etapa se priorizan los registros y relaciones que harán posible calcular esas métricas, no la construcción del módulo de Analytics.

Estas áreas estarán relacionadas, pero **una operación en un área no implica automáticamente que haya ocurrido una operación en otra**.

Por ejemplo:

> Crear una Orden de Compra no significa que los productos ya estén en el inventario.

De la misma forma:

> Crear una Orden de Compra no significa que el proveedor ya haya recibido el pago.

La orden representa el compromiso u operación comercial. La recepción y el pago son acontecimientos posteriores que deben registrarse cuando realmente ocurren.

Esta separación será un principio fundamental del sistema.

---

# 3. Conceptos principales

## Empresa / Tenant

Representa a una empresa que utiliza el ERP.

Cada empresa tiene sus propios clientes, proveedores, productos, órdenes, movimientos y registros financieros.

Una empresa nunca debe poder consultar o modificar información perteneciente a otra empresa.

---

## Cliente

Persona o empresa a quien se venden productos o servicios.

Un cliente puede tener múltiples órdenes de venta, entregas y pagos asociados.

---

## Proveedor

Persona o empresa a quien se compran productos, servicios o insumos.

Un proveedor puede tener múltiples órdenes de compra, recepciones y pagos asociados.

---

## Producto / Servicio

Elemento que la empresa vende o compra.

Un **producto** representa normalmente un bien físico cuya existencia puede controlarse mediante inventario.

Un **servicio** representa algo que puede venderse o comprarse sin necesidad de controlar existencias físicas.

Ejemplos:

* Laptop → producto
* Materia prima → producto
* Consultoría → servicio
* Mantenimiento → servicio

---

## Orden de Venta

Representa una operación comercial mediante la cual un cliente solicita o acuerda comprar determinados productos o servicios.

Una orden contiene:

* cliente;
* productos o servicios;
* cantidades;
* precios;
* importe total;
* estado de la orden.

La creación de una orden **no implica necesariamente que los productos hayan salido del almacén ni que el cliente haya pagado**.

La orden puede avanzar posteriormente mediante acciones independientes, como una entrega y un cobro.

---

## Orden de Compra

Representa una operación mediante la cual la empresa solicita o acuerda comprar productos o servicios a un proveedor.

Una orden contiene:

* proveedor;
* productos o servicios;
* cantidades;
* precios;
* importe total;
* estado de la orden.

La creación de una orden **no implica que los productos hayan sido recibidos ni que la empresa haya realizado el pago**.

La recepción y el pago se registran posteriormente cuando realmente ocurren.

---

## Recepción de Compra

Representa el momento en que la empresa recibe físicamente los productos de una Orden de Compra.

Una recepción puede generar una o varias entradas de inventario.

Por ejemplo:

> Orden de Compra: 100 unidades
> Primera recepción: 60 unidades
> Segunda recepción: 40 unidades

La orden sigue representando la compra original, mientras que las recepciones representan lo que efectivamente llegó al almacén.

Esto permite manejar compras recibidas parcialmente.

---

## Entrega / Salida de Venta

Representa el momento en que los productos de una Orden de Venta son entregados al cliente o salen físicamente del almacén.

Una entrega puede generar una o varias salidas de inventario.

Por ejemplo:

> Orden de Venta: 10 unidades
> Primera entrega: 6 unidades
> Segunda entrega: 4 unidades

La orden representa lo que se acordó vender; las entregas representan lo que efectivamente salió del inventario.

En el MVP, esta separación permite manejar ventas parcialmente entregadas sin descontar inventario simplemente por crear una orden.

---

## Pago

Representa un movimiento real de dinero relacionado con una operación.

Puede ser:

* dinero recibido de un cliente;
* dinero pagado a un proveedor;
* otro ingreso;
* otro egreso.

El pago es independiente de la creación de una orden.

Por ejemplo:

> Orden de Venta: $10,000
> Pago recibido: $0

significa que existe una operación de venta, pero todavía no se ha recibido el dinero.

Posteriormente:

> Pago recibido: $10,000

genera el movimiento financiero correspondiente.

El mismo principio aplica a las compras.

---

## Inventario

Representa las existencias actuales de los productos físicos que maneja la empresa.

El inventario se obtiene a partir de los movimientos registrados.

Una Orden de Compra por sí sola no aumenta el inventario.

El inventario aumenta cuando los productos son efectivamente recibidos y se registra la entrada correspondiente.

De manera análoga, una Orden de Venta por sí sola no disminuye necesariamente el inventario.

El inventario disminuye cuando los productos efectivamente salen del almacén y se registra la salida correspondiente.

---

## Kardex

El Kardex es el historial de movimientos de inventario de un producto.

Por ejemplo:

| Fecha | Movimiento | Cantidad |
| ----- | ---------- | -------: |
| 01/09 | Entrada    |     +100 |
| 05/09 | Salida     |      -20 |
| 10/09 | Entrada    |      +50 |
| 15/09 | Salida     |      -10 |

El stock actual resulta de estos movimientos:

**100 - 20 + 50 - 10 = 120 unidades**

El Kardex permite saber no solamente cuánto inventario existe actualmente, sino también cómo se llegó a esa cantidad.

Los movimientos del Kardex deben conservarse como historial de las operaciones realizadas.

---

## Ingreso

Representa dinero que efectivamente entra a la empresa.

Normalmente proviene del pago de una venta.

Una Orden de Venta no constituye por sí misma un ingreso.

El ingreso se registra cuando se recibe el dinero.

---

## Egreso

Representa dinero que efectivamente sale de la empresa.

Normalmente proviene del pago de una compra o de un gasto operativo.

Una Orden de Compra no constituye por sí misma un egreso.

El egreso se registra cuando se realiza el pago.

---

## Cuenta por cobrar

Representa dinero que los clientes deben a la empresa.

Por ejemplo:

> Orden de Venta: $20,000
> Pagado: $5,000
> Pendiente de cobrar: $15,000

La cuenta por cobrar permite conocer cuánto dinero se espera recibir de operaciones que ya fueron realizadas pero todavía no han sido pagadas completamente.

---

## Cuenta por pagar

Representa dinero que la empresa debe a sus proveedores.

Por ejemplo:

> Orden de Compra: $12,000
> Pagado: $4,000
> Pendiente de pagar: $8,000

La cuenta por pagar permite conocer cuánto dinero queda pendiente de entregar a los proveedores.

---

## Flujo de efectivo

Representa el dinero que efectivamente entra y sale de la empresa durante un período.

Ejemplo:

> Ingresos: $100,000
> Egresos: $60,000
> Flujo neto: $40,000

Las consultas financieras del MVP utilizarán esta información para proporcionar una visión sencilla del movimiento de efectivo. La visualización en un dashboard queda para una iteración posterior.

---

# 4. Principio fundamental: operación, inventario y dinero son cosas diferentes

El sistema debe distinguir entre tres acontecimientos relacionados pero independientes:

### 1. La operación comercial

Algo que la empresa acuerda comprar o vender.

Ejemplos:

> Orden de Venta
> Orden de Compra

### 2. El movimiento físico

Algo que efectivamente entra o sale del almacén.

Ejemplos:

> Recepción de compra → Entrada de inventario
> Entrega de venta → Salida de inventario

### 3. El movimiento financiero

Dinero que efectivamente entra o sale de la empresa.

Ejemplos:

> Cobro de cliente → Ingreso
> Pago a proveedor → Egreso

Una misma operación comercial puede generar los tres tipos de acontecimientos, pero **no necesariamente al mismo tiempo**.

### Ejemplo completo

Una empresa compra 100 unidades:

```text
Día 1
Orden de Compra
100 unidades
$10,000
```

Todavía:

```text
Inventario: +0
Dinero:     -$0
```

El proveedor entrega 60 unidades:

```text
Recepción
60 unidades
```

Ahora:

```text
Inventario: +60
Dinero:     -$0
```

Posteriormente se pagan los $10,000:

```text
Pago
$10,000
```

Ahora:

```text
Inventario: +60
Dinero:     -$10,000
```

Las 40 unidades restantes podrán recibirse posteriormente.

Este comportamiento es importante porque representa mejor la operación real de una empresa y evita asumir que todos los pasos ocurren automáticamente.

---

# 5. Flujo de ventas — Order-to-Cash

El flujo de ventas representa el proceso desde que se registra una operación de venta hasta que los productos son entregados y el dinero es recibido.

Conceptualmente:

**Cliente → Orden de Venta → Entrega → Cobro**

Estos pasos pueden ocurrir en momentos diferentes.

### Orden de Venta

Registra lo que se acordó vender.

### Entrega

Registra lo que efectivamente salió del almacén.

La entrega genera las salidas de inventario correspondientes.

### Cobro

Registra el dinero que efectivamente recibió la empresa.

El cobro genera el ingreso financiero correspondiente.

### Ejemplo

Se venden 10 unidades por $20,000.

Primero:

> Orden de Venta: 10 unidades
> Total: $20,000

Todavía no se modifica el inventario ni se registra un ingreso.

Después se entregan 6 unidades:

> Salida de inventario: -6
> Pendiente de entregar: 4

Finalmente se entregan las otras 4:

> Salida de inventario: -4
> Pendiente de entregar: 0

El cliente paga:

> Ingreso: +$20,000
> Cuenta por cobrar: $0

La operación comercial, el movimiento físico y el movimiento financiero quedan relacionados, pero cada uno conserva su propio registro.

---

# 6. Flujo de compras — Procure-to-Pay

El flujo de compras representa el proceso mediante el cual la empresa solicita productos o servicios, los recibe y posteriormente paga al proveedor.

Conceptualmente:

**Proveedor → Orden de Compra → Recepción → Pago**

### Orden de Compra

Registra lo que la empresa acordó comprar.

### Recepción

Registra lo que efectivamente llegó al almacén.

La recepción genera las entradas de inventario correspondientes.

### Pago

Registra el dinero que efectivamente salió de la empresa.

El pago genera el egreso financiero correspondiente.

### Ejemplo

Se compran 100 unidades por $10,000.

Primero:

> Orden de Compra: 100 unidades
> Total: $10,000

Después llegan 60:

> Entrada de inventario: +60
> Pendiente de recibir: 40

Posteriormente llegan las otras 40:

> Entrada de inventario: +40
> Pendiente de recibir: 0

Finalmente se realiza el pago:

> Egreso: -$10,000
> Cuenta por pagar: $0

---

# 7. Flujo de inventario

El inventario se modifica únicamente mediante movimientos registrados.

Los principales movimientos del MVP serán:

**Entrada**

Aumenta las existencias.

Ejemplos:

* recepción de una compra;
* entrada manual de mercancía.

**Salida**

Disminuye las existencias.

Ejemplos:

* entrega de una venta;
* salida manual de mercancía.

Cada movimiento queda registrado en el Kardex y puede relacionarse con la operación que lo originó.

Por ejemplo:

```text
Orden de Compra
      ↓
Recepción
      ↓
Entrada de Inventario
```

o:

```text
Orden de Venta
      ↓
Entrega
      ↓
Salida de Inventario
```

El sistema debe permitir consultar el historial de movimientos y obtener el stock actual a partir de ellos.

---

# 8. Flujo financiero

Las finanzas del MVP tienen como objetivo proporcionar una visión sencilla del dinero de la empresa, no llevar una contabilidad completa.

Los movimientos financieros principales serán:

```text
Cobro de venta
      ↓
Ingreso

Pago de compra
      ↓
Egreso
```

También podrán registrarse ingresos y egresos que no provengan directamente de una orden.

El sistema debe mostrar:

* ingresos;
* egresos;
* cuentas por cobrar;
* cuentas por pagar;
* flujo neto de efectivo.

### Ejemplo

Durante un mes:

> Ventas cobradas: $150,000
> Compras pagadas: $70,000
> Otros gastos: $20,000

Una vista financiera posterior puede mostrar:

> Ingresos: $150,000
> Egresos: $90,000
> Flujo neto: $60,000

Además:

> Por cobrar: $30,000
> Por pagar: $15,000

---

# 9. Relación entre los módulos

Los módulos no funcionan de forma aislada.

Una operación comercial puede producir diferentes acontecimientos en momentos distintos.

### Venta

```text
Cliente
   ↓
Orden de Venta
   │
   ├── Entrega
   │      ↓
   │   Salida de Inventario
   │
   └── Cobro
          ↓
       Ingreso
```

### Compra

```text
Proveedor
   ↓
Orden de Compra
   │
   ├── Recepción
   │      ↓
   │   Entrada de Inventario
   │
   └── Pago
          ↓
        Egreso
```

La aplicación debe permitir que estos acontecimientos ocurran independientemente y mantener la relación entre ellos.

Esto permite representar situaciones reales como:

* compras recibidas parcialmente;
* ventas entregadas parcialmente;
* órdenes todavía pendientes de pago;
* pagos parciales;
* órdenes canceladas antes de ser entregadas;
* productos recibidos antes de que una compra sea pagada.

---

# 10. Estados de las operaciones

Las operaciones deben tener estados que permitan conocer en qué punto del proceso se encuentran.

Por ejemplo, una Orden de Venta podría estar:

**Pendiente → Parcialmente entregada → Entregada**

y de manera independiente:

**Pendiente de cobro → Parcialmente pagada → Pagada**

Una Orden de Compra podría estar:

**Pendiente → Parcialmente recibida → Recibida**

y de manera independiente:

**Pendiente de pago → Parcialmente pagada → Pagada**

La cancelación debe ser un estado posible cuando corresponda.

Es importante que el estado comercial, el estado de inventario y el estado financiero no se confundan entre sí.

Una orden puede estar completamente recibida pero todavía pendiente de pago.

De igual forma, una orden de venta puede estar completamente pagada pero todavía tener productos pendientes de entregar, dependiendo de las condiciones de la operación.

---

# 11. Reglas generales del sistema

### Separación por empresa

Los datos de una empresa deben estar completamente separados de los datos de otras empresas.

### Las órdenes no generan automáticamente movimientos físicos

Crear una Orden de Compra no aumenta el inventario.

Crear una Orden de Venta no disminuye automáticamente el inventario.

Los movimientos de inventario se registran cuando ocurre la recepción o entrega correspondiente.

### Las órdenes no generan automáticamente movimientos de dinero

Crear una Orden de Compra no registra un egreso.

Crear una Orden de Venta no registra un ingreso.

Los movimientos financieros se registran cuando ocurre el pago o cobro.

### Los procesos pueden ocurrir parcialmente

Una orden puede ser recibida o entregada en varias partes.

Un pago puede realizarse parcialmente.

### Historial de inventario

Los movimientos del Kardex representan el historial del inventario y deben conservarse como registro de las operaciones realizadas.

### Trazabilidad

Siempre que sea posible, debe poder identificarse qué operación originó un movimiento.

Por ejemplo:

> Orden de Compra → Recepción → Entrada de Inventario

o:

> Orden de Venta → Entrega → Salida de Inventario

Esto permite entender posteriormente por qué cambió el inventario o por qué se generó un movimiento financiero.

---

# 12. Fuera del alcance del MVP

El MVP no pretende implementar:

* contabilidad financiera completa;
* declaraciones fiscales;
* facturación electrónica;
* integración con autoridades fiscales;
* nómina;
* recursos humanos;
* contabilidad de doble partida;
* múltiples almacenes;
* manufactura;
* logística avanzada;
* promociones o descuentos complejos;
* reportes empresariales avanzados;
* inteligencia artificial;
* automatizaciones complejas.

También quedan fuera inicialmente las etapas de:

* generación avanzada de cotizaciones, incluyendo plantillas complejas de costos, márgenes y precios;
* requisición interna de compra.

El MVP sí debe permitir registrar o adjuntar una cotización existente y consultar su información estructurada cuando sea necesaria para el proyecto. La generación avanzada puede incorporarse posteriormente sin modificar la idea fundamental del sistema.

---

# 13. Visión general

El ERP puede entenderse como un sistema que registra tres tipos de acontecimientos relacionados:

```text
                 OPERACIÓN COMERCIAL
                         │
              ┌──────────┴──────────┐
              │                     │
           VENTA                  COMPRA
              │                     │
        ┌─────┴─────┐         ┌─────┴─────┐
        ▼           ▼         ▼           ▼
     ENTREGA       COBRO   RECEPCIÓN      PAGO
        │           │         │           │
        ▼           ▼         ▼           ▼
     SALIDA       INGRESO   ENTRADA      EGRESO
   INVENTARIO                INVENTARIO
```

La idea central del sistema es que **una orden representa una operación comercial, mientras que las entregas, recepciones, cobros y pagos representan cosas que realmente ocurrieron después**.

Esto permite que el ERP represente operaciones reales sin asumir que todos sus pasos ocurren automáticamente o al mismo tiempo.

---

# 14. Proyecto como eje operativo

Un **Proyecto** representa una obra, servicio o encargo comercial que agrupa la información operativa relacionada con un cliente. El proyecto es una dimensión de organización y seguimiento; no reemplaza a las órdenes, facturas, pagos ni movimientos de inventario.

Un proyecto puede relacionarse con:

* un cliente;
* una o más cotizaciones;
* órdenes de venta y sus facturas;
* órdenes de compra y sus facturas de proveedor;
* pagos y cobros;
* documentos adjuntos;
* avances de ejecución y estimaciones.

El proyecto debe tener, como mínimo, identificador, nombre, cliente, fecha relevante, estado y referencias a los documentos asociados. El estado inicial del MVP será independiente de los estados financieros y físicos: por ejemplo, un proyecto puede estar en progreso aunque tenga facturas pagadas o pendientes.

## 14.1 Cotización

La cotización representa una propuesta comercial y puede existir antes de una orden. En el MVP podrá:

* registrarse con sus datos principales;
* asociarse a un proyecto y a un cliente;
* conservarse como archivo fuente, normalmente PDF o Excel;
* contener líneas consultables de productos, servicios o sets cuando esa información esté disponible;
* servir como referencia para crear órdenes o consultar el alcance contratado.

La cotización no genera inventario, ingreso, egreso ni cuenta por cobrar por sí misma.

## 14.2 Sets

Un **set** es una unidad de trabajo o conjunto comercial definido en una cotización. Para el MVP se tratará como un producto o servicio del catálogo con metadatos específicos del proyecto cuando sea necesario. El sistema deberá evitar confundir:

* **terminado**: el trabajo o fabricación del set fue concluido;
* **instalado**: el set fue colocado o entregado en el sitio.

Si el negocio confirma que ambos conceptos son equivalentes, podrán compartir estado; hasta entonces se conservarán como conceptos distintos para no perder información.

## 14.3 Avance y estimación

El **avance** registra trabajo ejecutado o cantidad completada en un proyecto, independientemente de que todavía se haya generado un documento de estimación.

La **estimación** es un documento preparado a partir de uno o varios avances; puede revisarse, aprobarse y quedar asociado a las partidas del proyecto. Una estimación aprobada puede actualizar el monto estimado o por cobrar según la regla comercial definida, pero no debe registrar automáticamente un cobro.

El MVP debe conservar el historial de avances y permitir que una estimación indique sus partidas, periodo, importe, estado, documento adjunto y proyecto relacionado. La aprobación debe ser explícita para que una estimación no afecte saldos por accidente.

---

# 15. Facturas y documentos operativos

Una factura es un documento comercial y una referencia para cuentas por cobrar o por pagar. No debe confundirse con una orden:

* una orden representa lo acordado;
* una factura representa el documento emitido o recibido;
* un pago representa dinero efectivamente recibido o entregado.

En el MVP una factura podrá cargarse como archivo y asociarse a un proyecto, cliente o proveedor y, cuando exista, a una orden. La generación automática de facturas queda fuera del alcance.

El sistema debe permitir consultar el archivo original y sus metadatos principales, como número, fecha, importe, moneda, tipo, contraparte y relaciones. La relación factura-orden debe ser flexible: una factura puede asociarse a una orden existente, pero el flujo no debe obligar a crear una orden ficticia cuando el documento proviene de una operación histórica o no tiene orden.

Los documentos de cotización, estimación, factura, comprobante de pago, Orden de Compra y OT deben conservar su tipo, nombre, ubicación, fecha de carga y entidad relacionada. El archivo adjunto no sustituye los datos estructurados necesarios para calcular saldos.

---

# 16. Orden de Compra, OT y alcance documental

La **Orden de Compra (OC)** sigue el flujo de compras descrito en este documento: registra el compromiso con un proveedor y no genera inventario ni egreso hasta que se registren recepción y pago.

La **OT** aparece en los documentos de ejemplo con el nombre de “Subcontrato”. Su significado operativo todavía debe confirmarse con el cliente. Mientras no exista esa confirmación, el MVP la tratará como un tipo de documento adjunto asociado a un proyecto, sin inventar reglas de negocio ni convertirla automáticamente en una orden de compra, venta o trabajo.

Cuando se confirme que la OT representa una orden de trabajo o un subcontrato, se definirá su entidad, estados, partidas, relación con avances y efecto sobre compras, ventas o cuentas por pagar. Esta decisión queda registrada como pendiente de descubrimiento.

---

# 17. Consultas del proyecto

La página de un proyecto deberá poder consultar, como mínimo:

* datos generales y estado del proyecto;
* cotizaciones y sets;
* órdenes de venta y facturas por cobrar;
* órdenes de compra y facturas por pagar;
* pagos y cobros, incluyendo su estado derivado;
* avances, estimaciones y documentos adjuntos.

Los filtros de facturas deben calcularse a partir del saldo acumulado, no de un estado escrito manualmente:

* **sin pago** cuando el total pagado es cero;
* **parcialidad** cuando el total pagado es mayor que cero y menor que el total;
* **pagada** cuando el saldo es cero.

Estas consultas pueden alimentar el panel de control posteriormente. El panel no será una fuente adicional de verdad.

---

# 18. Workflows del MVP

Los flujos principales se documentan por separado en `docs/workflows/`:

* [Crear un proyecto](workflows/create-project.md);
* [Registrar una orden de venta](workflows/create-sales-order.md);
* [Registrar una orden de compra](workflows/create-purchase-order.md);
* [Cargar una factura](workflows/upload-invoice.md);
* [Registrar un cobro o pago](workflows/register-payment.md);
* [Registrar avance y generar estimación](workflows/register-progress-estimate.md).

Cada workflow define actor, precondiciones, pasos, reglas, resultado y casos de rechazo. Estos documentos son especificaciones funcionales, no una decisión sobre endpoints o tablas.
