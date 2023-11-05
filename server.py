import socket, ssl

# Paramètres du serveur
server_address = ("192.168.1.66", 8080)

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse IP et au port
server_socket.bind(server_address)

# Ecouter les connexions entrantes
server_socket.listen(1)

print("En attente de connexion...")

# Accepter une connexion entrante
client_socket, client_address = server_socket.accept()
print(f"Connexion de {client_address} établie !")

# Création du socket SSL
server_ssl = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_ssl.load_cert_chain(certfile="certificat.pem", keyfile="cle.pem")

client_ssl = server_ssl.wrap_socket(
    client_socket,
    server_side=True,
)

# Nom du fichier à recevoir
file_name = "reçu.txt"

# Ouvrir le fichier en mode écriture binaire
with open(file_name, "wb") as f:
    # Lire les données reçues du client
    data = client_ssl.recv(1024)
    while data:
        # Ecrire les données dans le fichier
        f.write(data)
        # Lire les données reçues du client
        data = client_ssl.recv(1024)

print("Fichier reçu !")

# Fermer ssl
client_ssl.close()

# Fermer le serveur
server_socket.close()