import subprocess

# Solicitar el host y el puerto al usuario
host = input("Ingrese el nombre del host a analizar: ")
port = input("Ingrese el puerto: ")

# Validar la versión TLS 1.0
command = f"openssl s_client -connect {host}:{port} -tls1"
tls1_process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
tls1_output = tls1_process.stdout.decode()
if "Secure Renegotiation IS NOT supported" in tls1_output:
    print("Advertencia: El host es vulnerable a ataques de renegociación insegura")

# Validar la versión TLS actual
command = f"openssl s_client -connect {host}:{port}"
tls_process = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
tls_output = tls_process.stdout.decode()

# Verificar si se estableció una conexión SSL
if "Secure connection established" not in tls_output:
    print("Error: No se pudo establecer una conexión segura con el host")
    exit()

# Verificar la versión de TLS
if "TLS 1.0" in tls_output:
    print("Advertencia: El host admite la versión TLS 1.0")

# Reportar el resultado final del análisis
print("Análisis completo")

# Forzar la finalización del proceso OpenSSL
tls_process.kill()
