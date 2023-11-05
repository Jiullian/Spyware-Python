import socket, ssl

def transfert(server_socket, kill):
    # Accepter une connexion entrante
    client_socket, client_address = server_socket.accept()
    print(f"Connexion de {client_address} établie !")

    # Création du socket SSL
    server_ssl = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_ssl.load_cert_chain(certfile="certificat.pem", keyfile="cle.pem")

    client_ssl = server_ssl.wrap_socket(client_socket,server_side=True,)

    if kill == 0:
        client_ssl.send(b"nokill")
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

    else:
        # Envoyer la commande kill au client
        client_ssl.send(b"kill")
        print("La commande kill a été envoyée au client.")

    # Fermer ssl
    client_ssl.close()