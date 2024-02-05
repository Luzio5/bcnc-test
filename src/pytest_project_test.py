import requests

# Define el URL base del API
API_URL = "https://jsonplaceholder.typicode.com/albums"

# URL del servidor de autorización OAuth 2.0 inventado
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

# Define una función para realizar una solicitud GET al API
def make_api_request(url):
    response = requests.get(url)
    return response

# Define una función para realizar un flujo de autenticación OAuth 2.0 con client credentials
def get_access_token_client_credentials():
    try:
        # Parámetros de solicitud de token
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }

        # Realiza la solicitud de token de acceso con timeout
        response = requests.post(AUTH_SERVER_URL, data=data, timeout=10)

        # Extrae el token de acceso del cuerpo de la respuesta JSON
        token_data = response.json()
        access_token = token_data.get("access_token")
        return access_token
    except requests.Timeout:
        print("Error: Timeout al obtener el token de acceso con client credentials.")
        return None
    except Exception as e:
        print("Error obteniendo token de acceso con client credentials:", e)
        return None

# Define una función para realizar un flujo de autenticación OAuth 2.0 con authorization code
def get_access_token_authorization_code():
    try:
        # Parámetros de solicitud de token
        data = {
            "grant_type": "password",
            "username": USERNAME,
            "password": PASSWORD,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }

        # Realiza la solicitud de token de acceso con timeout
        response = requests.post(AUTH_SERVER_URL, data=data, timeout=10)

        # Extrae el token de acceso del cuerpo de la respuesta JSON
        token_data = response.json()
        access_token = token_data.get("access_token")
        return access_token
    except requests.Timeout:
        print("Error: Timeout al obtener el token de acceso con authorization code.")
        return None
    except Exception as e:
        print("Error obteniendo token de acceso con authorization code:", e)
        return None

# Define la función para realizar la llamada al API protegido con OAuth 2.0
def call_protected_api(access_token):
    try:
        # Cabecera de autorización con el token de acceso
        headers = {"Authorization": f"Bearer {access_token}"}

        # Realiza la llamada al API protegido
        response = requests.get(API_URL, headers=headers, timeout=10)
        return response
    except requests.Timeout:
        print("Error: Timeout al llamar al API protegido.")
        return None
    except Exception as e:
        print("Error al llamar al API protegido:", e)
        return None

#Comentado por no tener authorization code . Estos test pasan porque a la api no le importa que se envie en un get method
# Define una función de prueba para probar el API con autenticación de client credentials
#def test_api_response_client_credentials():
    # Obtiene el token de acceso utilizando client credentials grant
    access_token = get_access_token_client_credentials()

    if access_token:
        # Realiza la llamada al API protegido
        response = call_protected_api(access_token)

        # Verifica si la respuesta es exitosa (código de estado 200)
        if response and response.status_code == 200:
            # Extrae los datos JSON de la respuesta
            data = response.json()

            # Verifica los datos recibidos del API
            for i in range(5):
                expected_item = EXPECTED_DATA[i]
                actual_item = data[i]
                for key, value in expected_item.items():
                    assert key in actual_item
                    assert actual_item[key] == value
        else:
            print("Error: No se pudo obtener una respuesta del API protegido.")
    else:
        print("Error: No se pudo obtener el token de acceso con client credentials.")

#Comentado por no tener credenciales. Estos test pasan porque a la api no le importa que se envie en un get method
# Define una función de prueba para probar el API con autenticación de authorization code
#def test_api_response_authorization_code():
    # Obtiene el token de acceso utilizando authorization code grant
    access_token = get_access_token_authorization_code()

    if access_token:
        # Realiza la llamada al API protegido
        response = call_protected_api(access_token)

        # Verifica si la respuesta es exitosa (código de estado 200)
        if response and response.status_code == 200:
            # Extrae los datos JSON de la respuesta
            data = response.json()

            # Verifica los datos recibidos del API
            for i in range(5):
                expected_item = EXPECTED_DATA[i]
                actual_item = data[i]
                for key, value in expected_item.items():
                    assert key in actual_item
                    assert actual_item[key] == value
        else:
            print("Error: No se pudo obtener una respuesta del API protegido.")
    else:
        print("Error: No se pudo obtener el token de acceso con authorization code.")

# Define una función de prueba para probar el API sin autenticación
def test_api_response_no_authentication():
    # Realiza la llamada al API sin autenticación
    response = requests.get(API_URL, timeout=10)

    # Verifica si la respuesta es exitosa (código de estado 200)
    if response and response.status_code == 200:
        # Extrae los datos JSON de la respuesta
        data = response.json()

        # Verifica los datos recibidos del API
        for i in range(5):
            expected_item = EXPECTED_DATA[i]
            actual_item = data[i]
            for key, value in expected_item.items():
                assert key in actual_item
                assert actual_item[key] == value
    else:
        print("Error: No se pudo obtener una respuesta del API sin autenticación.")
