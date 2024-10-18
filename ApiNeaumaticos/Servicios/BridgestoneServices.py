import requests
from bs4 import BeautifulSoup
from ApiNeaumaticos.Servicios.ServiceWebScraping import ServiceWebScraping

class BridgestoneServices(ServiceWebScraping):
    def __init__(self,url,headers) -> None:
        self.urlBase=url
        self.headers=headers
        self.proveedor={"proveedor":"RASA","direccion":"Agraciada 2720","telefono":"2203 4449","pagina":self.urlBase}
        self.resultado = []

    def PeticionGet(self):
        response = requests.get(self.urlBase,self.headers)
        if response.status_code ==200:
            soup = BeautifulSoup(response.text,'html.parser',fromEncoding='utf-8')
            productos = soup.find_all("div",class_="ui-search-result__wrapper")

            for producto in productos:
                nombre = producto.find("h2",class_="poly-box")
                precio = producto.find("div",class_="poly-component__price")
                img = producto.find("img",class_="poly-component__picture")
                self.resultado.append({'nombre':nombre.text,'precio':precio.text,'img':img.get('data-src')})
        else:
          return {'respuesta':"algo fallo"}
        
        return  {"proveedor":self.proveedor,"naumaticos":self.resultado}
        #fin