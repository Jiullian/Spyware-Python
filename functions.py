# Fonction création simple du fichier
def creation_fichier(nom_fichier):
    try :
        open(nom_fichier, "w")
    except Exception as e:
        print(f"Erreur lors de la création de %s : {e}" %(nom_fichier))
