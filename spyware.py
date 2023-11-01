import keyboard, socket
import functions
from time import strftime

ip_host = socket.gethostbyname(socket.gethostname())
time = strftime("%Y-%m-%d_%H-%M-%S")
name_file = ip_host + "_" + time + ".txt"

functions.creation_fichier(name_file)

