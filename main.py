import requests
import bs4

plantilla_hotel = {
    "nombre" : "",
    "puntuacion" : "",
    "precio" : "",
    "comentario" : "",
    "imagen" : ""
}

def cargar_pagina():
    html = requests.get("https://www.expedia.es/Hotel-Search?adults=1&d1=2022-11-22&d2=2022-11-30&destination=Sevilla%2C%20Andaluc%C3%ADa%2C%20Espa%C3%B1a&directFlights=false&endDate=2023-01-13&l10n=%5Bobject%20Object%5D&latLong=37.38619%2C-5.99198&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=3312&semdtl=&sort=RECOMMENDED&startDate=2023-01-12&theme=&useRewards=false&userIntent=").content
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup

def cargar_hoteles():
    soup = cargar_pagina()
    lista_hoteles = list()
    lista_elementos = soup.find_all("li", {"class" : "uitk-spacing uitk-spacing-margin-blockstart-three"})

    for elemento in lista_elementos:
        nombre = elemento.find("div", {"class": "uitk-spacing uitk-spacing-padding-blockend-three uitk-layout-flex-item"}).find("h2").text
        if elemento.find("span", {"uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme"}) is not None :
            puntuacion = elemento.find("span", {"uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme"}).text
        precio = elemento.find("div", {"class" : "uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme"}).text
        if elemento.find("span", {"class" : "uitk-text uitk-type-300 uitk-text-default-theme"}) is not None:
            comentario = elemento.find("span", {"class" : "uitk-text uitk-type-300 uitk-text-default-theme"}).text
        if elemento.find("div", {"class" : 'uitk-image-placeholder'}) is not None:
            img = soup.find_all("img", class_ = "uitk-image-media")
        for i in img :

            if ".jpg" in str(i["src"]):
                imagen = str(i["src"])



        hotel_datos = plantilla_hotel.copy()
        hotel_datos["nombre"] = nombre
        hotel_datos["puntuacion"] = puntuacion
        hotel_datos["precio"] = precio
        hotel_datos["comentario"] = comentario
        hotel_datos["imagen"] = imagen
        lista_hoteles.append(hotel_datos)


    return print(lista_hoteles)





cargar_hoteles()