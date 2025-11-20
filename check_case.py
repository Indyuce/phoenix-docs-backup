import os

def rename_recursive(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        # Vérifier si le nom commence par une majuscule
        if entry[0].isupper():
            new_name = entry[0].lower() + entry[1:]
            new_full_path = os.path.join(path, new_name)

            # Renommer le fichier ou dossier
            os.rename(full_path, new_full_path)
            print(f"Renommé: {full_path} -> {new_full_path}")

            # Mettre à jour le chemin pour continuer la récursion si c'est un dossier
            full_path = new_full_path

        # Si c'est un dossier, récursion
        if os.path.isdir(full_path):
            rename_recursive(full_path)

# Lancer sur le dossier courant
current_folder = os.getcwd()
rename_recursive(current_folder)
