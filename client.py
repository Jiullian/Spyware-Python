import socket
import ssl

# Créez un socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Créez une connexion sécurisée avec SSL/TLS
ssl_client_socket = ssl.wrap_socket(client_socket, keyfile=None, certfile=None, cert_reqs=ssl.CERT_NONE)

# Connectez-vous au serveur sécurisé
ssl_client_socket.connect(("192.168.1.66", 8080))