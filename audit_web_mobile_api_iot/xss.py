import requests

# Pide al usuario que ingrese la URL
url = input("Ingrese la URL: ")

# Abre el diccionario de payloads
with open('xss.txt') as f:
    payloads = f.readlines()
payloads = [payload.strip() for payload in payloads]

# Realiza la prueba de vulnerabilidad XSS con cada payload
for payload in payloads:
    full_url = url + payload
    response = requests.get(full_url)
    if payload in response.text:
        print(f"XSS detectado con payload: {payload}")
    else:
        print(f"No se detectó XSS con payload: {payload}")
