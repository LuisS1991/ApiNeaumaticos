
*Esta herramienta digital forma parte del proyecto de fin de curso de 3er año del bachillerato de Soporte y Desarrollo Informático del **Instituto Técnico Superior Arias Balparda**. Puedes conocer más sobre el proyecto en [its.utu.edu.uy](https://its.utu.edu.uy/wp-content/uploads/sites/33/2024/06/Proyecto-3o-EMT-Enfasis-Soporte-2024-3.pdf)*

<h1 align="center">API Neumaticos</h1>
<p align="center"><img src="https://www.webdevelopersnotes.com/wp-content/uploads/create-a-simple-home-page.png"/></p>

## Tabla de contenidos:
---

- [API](#api)
- [Idea del proyecto](#idea-del-proyecto)
- [Guía de uso](#guía-de-uso)
- [Información adicional](#información-adicional)
- [Licencia](#licencia)
- [Limitación de responsabilidades](#limitación-de-responsabilidades)

## Api
---
API o Application Programming Interface, que en español quiere decir Interfaz de Programación de Aplicaciones, es un conjunto de funciones y procedimientos que permite integrar sistemas, permitiendo que sus funcionalidades puedan ser reutilizadas por otras aplicaciones o software

## Idea del proyecto

La idea surge como una necesidad del proyecto principal el cual estamos desarrollando que trata de un Software de administración para un parking con gomeria. Donde nuestro cliente solicita 
alguna forma que el sistema obtenga los precios de neumaticos de sus 3 principales proveedores. Analizando los datos es como llegamos a crear el siguiente servicio web. Agregando una capa de complejidad al proyecto 
complementario se decidio que la api utilizara un jwt de autentificación. El mismo se obtiene de la web app que fue creada para administrar usuarios y jwt.- 
Dicha pagina web cuenta con un login donde se puede crear, actualizar o eliminar el JWT. Asi mismo este token tiene un tiempo de expiración configurable. A fines educativos se configuro a 1 año.- 
Como funciones extras a futuro se pensaba implementar algun sistema de conteo de peticione diarias a fin de evitar algun sobre costo en el servicio.- 

---
<div align="center">

### **✨ Api craeada con  Python  y deploy in Railway. ✨**
![PyPI version](https://badge.fury.io/py/reflex.svg)
![versions](https://img.shields.io/pypi/pyversions/reflex.svg)
![Documentation](https://img.shields.io/badge/Documentation%20-Introduction%20-%20%23007ec6)
![version](https://img.shields.io/badge/version-0.0.1-blue)
</div>
 

## Guía de uso
---
Se debe autentificar en al aplicación web y obtener un token de autentificación, el cual sera agregado en las cabecera de las peticiones.-

Fomra de utilizarla es mediante el protocolo de comunicación http mediante el verbo GET. accedemos mediante una petición a la ruta original agegando la marca del neumatico que nuestro cliente trabaja
* la ruta principal de nuestra api es la siguiente: https://apineumaticos-production.up.railway.app
* /pirelli
* /bridgestone
* /michelin 
* en las peticiones se debe adjuntar un JWT, el cual proporciona una capa de seguridad al web service.
estas peticiones nos retornara un json con datos del proveedor y una lista de neumatico, a continuacion daremos un ejemplo

```
{
   "proveedor":{

      "proveedor":"RASA",

      "direccion":"Agraciada 2720",

      "telefono":"2203 4449",

      "pagina"":""https"://listado.mercadolibre.com.uy/accesorios-vehiculos/neumaticos/_CustId_227678069?item_id=MLU615508682&category_id=MLU208676&seller_id=227678069&client=recoview-selleritems&recos_listing=true#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D3%26applied_value_id%3DMLU208675%26applied_value_name%3DNeum%C3%A1ticos%26applied_value_order%3D1%26applied_value_results%3D195%26is_custom%3Dfalse"

    },

"naumaticos":
    [
        {""nombre"":"Neumático Bridgestone Ecopia EP150 P 185/55R16 83 V",""precio"":"US$145,

      80",""img"":null},

        {""nombre"":"Neumático Bridgestone Dueler H/P Sport 225/55R18 98 H",""precio"":"US$277,

      20",""img"":null},

        {""nombre"":"Neumático Bridgestone Dueler H/T 684 215/65R16 98 T",""precio"":"US$197,

      10",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_745136-MLA46524062203_062021-V.webp"},{""nombre"":"Neumático Bridgestone B-Series B250 185/65R15 88 H",""precio"":"US$130,

      50",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_693038-MLU75071023744_032024-V.webp"},{""nombre"":"Neumático Firestone Destination A/T LT 235/75R15 104 S",""precio"":"US$239,

      40",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_916917-MLA50056205969_052022-V.webp"},

        {""nombre"":"Neumático Bridgestone Turanza Er300 195/65 R15 91 H",""precio"":"US$154,

      80",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_706450-MLU75108443021_032024-V.webp"},

        {""nombre"":"Neumático Bridgestone Turanza T001 205/55 R16",""precio"":"US$166,

      50",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_630330-MLU74368553026_022024-V.webp"},

        {""nombre"":"Neumático Firestone Cv5000 185 R14 102/100 R",""precio"":"US$153",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_617629-MLU76141981853_052024-V.webp"}
    ]

}
```
### Dependencias

Esta api esta constrida con python y el framework de [Reflex](https://astro.build/) el cual es un potente marco de trabajo para crar aplicaciones web completas. 
Se puede desarrollar el frontend como backend incluyendo construcción de Api.Por debajo utiliza la tecnologia de fast api para la cración de servicios web. 

Despligue de la aplicación en la plataforma [RailWai](https://railway.app) que nos ofrece una capa gratis para poder alojar nuestro pequeño proyecto. 
La capa gratuita es de: 
* $5 dolares
* 512 MB of RAM per Container
* 1 GB of Shared Disk
* 2 vCPU per Container

## Autor/es
---
Idea original intengrantes del grupo Téchene, autor de la herramienta y despliege [Luis](https://github.com/LuisS1991/)


## Información adicional
---
Nuestro proyecto cuenta con la creación de una empresa de desarrollo de software e insfractructura de red.
Este proyecto ocupa todo los aspectos tecnicos necesarios para creación y puesta en marcha de un producto de software, que incluye la parte tan importante como el desarrollo que es la insfrastructura de red y su seguiridad. 
Nuestra Empresa es [Téchene](techne-tau.vercel.app), este sitio web fue creado con la tecnologia de [Astro](https://reflex.dev/), un marco de trabajo para frontend. 


## Licencia 
---
i. La licencia esta herramientas es gratis para usos educativos.
ii. No se puede utilizar con fines comerciales, en ese caso puede contactarse al autor y crear una version de pago

## Limitación de responsabilidades
---

El ITS y los integrantes del grupo no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.

