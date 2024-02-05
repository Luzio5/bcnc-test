""" import requests

# Define the API URL
API_URL = "https://jsonplaceholder.typicode.com/albums"

# Datos esperados para los primeros 5 elementos
EXPECTED_DATA = [
    {"userId": 1, "id": 1, "title": "quidem molestiae enim"},
    {"userId": 1, "id": 2, "title": "sunt qui excepturi placeat culpa"},
    {"userId": 1, "id": 3, "title": "omnis laborum odio"},
    {"userId": 1, "id": 4, "title": "non esse culpa molestiae omnis sed optio"},
    {"userId": 1, "id": 5, "title": "eaque aut omnis a"}
]

# Define a test function using pytest
def test_api_response():
    # Make a GET request to the API
    response = requests.get(API_URL)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Extract the JSON data from the response
    data = response.json()

    # Check the length of the received data (limit to the first 5 elements)
    assert len(data) >= 5

    # Check each element in the received data (only for the first 5 elements)
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]

        # Check if all keys and values match the expected data
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value """




""" import requests

# Define el URL base del API
API_URL = "https://jsonplaceholder.typicode.com/albums"

# URL del servidor de autorización OAuth 2.0
AUTH_SERVER_URL = "https://example.com/oauth/token"

# Credenciales de cliente (client credentials grant)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

# Credenciales de usuario (authorization code grant)
USERNAME = "your_username"
PASSWORD = "your_password"

# Datos esperados para los primeros 5 elementos
EXPECTED_DATA = [
    {"userId": 1, "id": 1, "title": "quidem molestiae enim"},
    {"userId": 1, "id": 2, "title": "sunt qui excepturi placeat culpa"},
    {"userId": 1, "id": 3, "title": "omnis laborum odio"},
    {"userId": 1, "id": 4, "title": "non esse culpa molestiae omnis sed optio"},
    {"userId": 1, "id": 5, "title": "eaque aut omnis a"}
]

# Define una función para realizar una solicitud HTTP GET al API
def make_api_request(url):
    # Realiza una solicitud GET al API
    response = requests.get(url)

    # Retorna la respuesta
    return response

# Define una función para realizar un flujo de autenticación OAuth 2.0 con client credentials
# Define la función para obtener el token de acceso (client credentials grant)
def get_access_token_client_credentials():
    # Parámetros de solicitud de token
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Realiza la solicitud de token de acceso
    response = requests.post(AUTH_SERVER_URL, data=data)

    # Extrae el token de acceso del cuerpo de la respuesta JSON
    token_data = response.json()
    access_token = token_data.get("access_token")

    return access_token

# Define una función para realizar un flujo de autenticación OAuth 2.0 con authorization code
def get_access_token_authorization_code():
    # Parámetros de solicitud de token
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Realiza la solicitud de token de acceso
    response = requests.post(AUTH_SERVER_URL, data=data)

    # Extrae el token de acceso del cuerpo de la respuesta JSON
    token_data = response.json()
    access_token = token_data.get("access_token")

    return access_token

# Define la función para realizar la llamada al API protegido con OAuth 2.0
def call_protected_api(access_token):
    # Cabecera de autorización con el token de acceso
    headers = {"Authorization": f"Bearer {access_token}"}

    # Realiza la llamada al API protegido
    response = requests.get(API_URL, headers=headers)
    
    return response

# Define una función de prueba para probar el API con autenticación de client credentials
def test_api_response_client_credentials():
    # Obtiene el token de acceso utilizando client credentials grant
    access_token = get_access_token_client_credentials()

    # Realiza la llamada al API protegido
    response = call_protected_api(access_token)

    # Verifica si la respuesta es exitosa (código de estado 200)
    assert response.status_code == 200

    # Extrae los datos JSON de la respuesta
    data = response.json()

    # Verifica los datos recibidos del API
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value

# Define una función de prueba para probar el API con autenticación de authorization code
def test_api_response_authorization_code():
    # Obtiene el token de acceso utilizando authorization code grant
    access_token = get_access_token_authorization_code()

    # Realiza la llamada al API protegido
    response = call_protected_api(access_token)

    # Verifica si la respuesta es exitosa (código de estado 200)
    assert response.status_code == 200

    # Extrae los datos JSON de la respuesta
    data = response.json()

    # Verifica los datos recibidos del API
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value
 """


import requests

# Define el URL base del API
API_URL = "https://jsonplaceholder.typicode.com/albums"

# URL del servidor de autorización OAuth 2.0
AUTH_SERVER_URL = "https://example.com/oauth/token"

# Credenciales de cliente (client credentials grant)
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

# Credenciales de usuario (authorization code grant)
USERNAME = "your_username"
PASSWORD = "your_password"

# Datos esperados para los primeros 5 elementos
EXPECTED_DATA = [
    {"userId": 1, "id": 1, "title": "quidem molestiae enim"},
    {"userId": 1, "id": 2, "title": "sunt qui excepturi placeat culpa"},
    {"userId": 1, "id": 3, "title": "omnis laborum odio"},
    {"userId": 1, "id": 4, "title": "non esse culpa molestiae omnis sed optio"},
    {"userId": 1, "id": 5, "title": "eaque aut omnis a"}
]

# Define una función para realizar una solicitud HTTP GET al API
def make_api_request(url):
    # Realiza una solicitud GET al API
    response = requests.get(url)

    # Retorna la respuesta
    return response

# Define una función para realizar un flujo de autenticación OAuth 2.0 con client credentials
# Define la función para obtener el token de acceso (client credentials grant)
def get_access_token_client_credentials():
    # Parámetros de solicitud de token
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Realiza la solicitud de token de acceso
    response = requests.post(AUTH_SERVER_URL, data=data)

    # Extrae el token de acceso del cuerpo de la respuesta JSON
    token_data = response.json()
    access_token = token_data.get("access_token")

    return access_token

# Define una función para realizar un flujo de autenticación OAuth 2.0 con authorization code
def get_access_token_authorization_code():
    # Parámetros de solicitud de token
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    # Realiza la solicitud de token de acceso
    response = requests.post(AUTH_SERVER_URL, data=data)

    # Extrae el token de acceso del cuerpo de la respuesta JSON
    token_data = response.json()
    access_token = token_data.get("access_token")

    return access_token

# Define la función para realizar la llamada al API protegido con OAuth 2.0
def call_protected_api(access_token):
    # Cabecera de autorización con el token de acceso
    headers = {"Authorization": f"Bearer {access_token}"}

    # Realiza la llamada al API protegido
    response = requests.get(API_URL, headers=headers)
    
    return response

# Define una función para realizar la llamada al API sin autenticación
def call_unauthenticated_api():
    # Realiza la llamada al API sin ningún token de acceso
    response = requests.get(API_URL)
    
    return response

# Define una función de prueba para probar el API con autenticación de client credentials
def test_api_response_client_credentials():
    # Obtiene el token de acceso utilizando client credentials grant
    access_token = get_access_token_client_credentials()

    # Realiza la llamada al API protegido
    response = call_protected_api(access_token)

    # Verifica si la respuesta es exitosa (código de estado 200)
    assert response.status_code == 200

    # Extrae los datos JSON de la respuesta
    data = response.json()

    # Verifica los datos recibidos del API
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value

# Define una función de prueba para probar el API con autenticación de authorization code
def test_api_response_authorization_code():
    # Obtiene el token de acceso utilizando authorization code grant
    access_token = get_access_token_authorization_code()

    # Realiza la llamada al API protegido
    response = call_protected_api(access_token)

    # Verifica si la respuesta es exitosa (código de estado 200)
    assert response.status_code == 200

    # Extrae los datos JSON de la respuesta
    data = response.json()

    # Verifica los datos recibidos del API
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value

# Define una función de prueba para probar el API sin autenticación
def test_api_response_no_authentication():
    # Realiza la llamada al API sin autenticación
    response = call_unauthenticated_api()

    # Verifica si la respuesta es exitosa (código de estado 200)
    assert response.status_code == 200

    # Extrae los datos JSON de la respuesta
    data = response.json()

    # Verifica los datos recibidos del API
    for i in range(5):
        expected_item = EXPECTED_DATA[i]
        actual_item = data[i]
        for key, value in expected_item.items():
            assert key in actual_item
            assert actual_item[key] == value
