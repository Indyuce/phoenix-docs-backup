import os

def scan_files_with_uppercase(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        # Si c'est un fichier et qu'il contient au moins une majuscule
        if os.path.isfile(full_path) and any(c.isupper() for c in entry):
            print(f"Fichier avec majuscule: {full_path}")

        # Si c'est un dossier, récursion
        if os.path.isdir(full_path):
            scan_files_with_uppercase(full_path)

# Lancer sur le dossier courant
current_folder = os.getcwd()
scan_files_with_uppercase(current_folder)
