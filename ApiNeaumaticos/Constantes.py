SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
pirelli_url="https://listado.mercadolibre.com.uy/accesorios-vehiculos/_Tienda_pirelli"
michelin_url="https://tienda.mercadolibre.com.uy/bartl"
bridgestone_url="https://listado.mercadolibre.com.uy/accesorios-vehiculos/neumaticos/_CustId_227678069?item_id=MLU615508682&category_id=MLU208676&seller_id=227678069&client=recoview-selleritems&recos_listing=true#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D3%26applied_value_id%3DMLU208675%26applied_value_name%3DNeum%C3%A1ticos%26applied_value_order%3D1%26applied_value_results%3D195%26is_custom%3Dfalse"


respuesta_json="""
{
   
"proveedor":{

      "proveedor":"RASA",

      "direccion":"Agraciada 2720",

      "telefono":"2203 4449",

      "pagina"":"https://listado.mercadolibre.com.uy/accesorios-vehiculos/neumaticos/_CustId_227678069?item_id=MLU615508682&category_id=MLU208676&seller_id=227678069&client=recoview-selleritems&recos_listing=true#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D3%26applied_value_id%3DMLU208675%26applied_value_name%3DNeum%C3%A1ticos%26applied_value_order%3D1%26applied_value_results%3D195%26is_custom%3Dfalse"

    },

"naumaticos":
    [
    
       {""nombre"":"Neumático Bridgestone Ecopia EP150 P 185/55R16 83 V",""precio"":"US$145,80",""img"":null},

       {""nombre"":"Neumático Bridgestone Dueler H/P Sport 225/55R18 98 H",""precio"":"US$277,20",""img"":null},

       {""nombre"":"Neumático Bridgestone Dueler H/T 684 215/65R16 98 T",""precio"":"US$197,10",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_745136-MLA46524062203_062021-V.webp"},
       
       {""nombre"":"Neumático Bridgestone B-Series B250 185/65R15 88 H",""precio"":"US$130,50",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_693038-MLU75071023744_032024-V.webp"},
       
       {""nombre"":"Neumático Firestone Destination A/T LT 235/75R15 104 S",""precio"":"US$239,40",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_916917-MLA50056205969_052022-V.webp"},

       {""nombre"":"Neumático Bridgestone Turanza Er300 195/65 R15 91 H",""precio"":"US$154,80",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_706450-MLU75108443021_032024-V.webp"},

       {""nombre"":"Neumático Bridgestone Turanza T001 205/55 R16",""precio"":"US$166,50",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_630330-MLU74368553026_022024-V.webp"},

       {""nombre"":"Neumático Firestone Cv5000 185 R14 102/100 R",""precio"":"US$153",""img"":""https"://http2.mlstatic.com/D_Q_NP_2X_617629-MLU76141981853_052024-V.webp"}
    ]

}
"""