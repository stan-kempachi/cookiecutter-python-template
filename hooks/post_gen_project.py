import io
import os
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Permettre l'affichage des caractères Unicode dans la console
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")

# Variables contextuelles à partir de Cookiecutter
project_slug = r"{{ cookiecutter.project_slug }}"  # Fix chemin
package_name = r"{{ cookiecutter.package_name }}"  # Fix chemin
framework = r"{{ cookiecutter.framework }}"  # Fix alternative

# Répertoires du projet généré (avec gestion des chemins Windows)
project_path = Path(r"{{ cookiecutter._output_dir }}") / project_slug
package_path = project_path / package_name


def clean_unused_files():
    """
    🧹 Supprime les fichiers inutiles selon le framework sélectionné.
    """
    print("\n🔍 Suppression des fichiers inutiles selon le framework...")
    if framework != "django":
        django_file = package_path / "manage.py"
        if django_file.exists():
            os.remove(django_file)
            print(f"  🗑️ Supprimé : {django_file}")

    if framework != "flask":
        flask_file = package_path / "flask_app.py"
        if flask_file.exists():
            os.remove(flask_file)
            print(f"  🗑️ Supprimé : {flask_file}")


def safe_remove(filepath):
    """
    🚨 Tente de supprimer le fichier donné, avec vérification après suppression.
    """
    try:
        os.remove(filepath)
        # Vérification si le fichier existe encore
        if not os.path.exists(filepath):
            print(f"    🗑️ Supprimé correctement : {filepath}")
        else:
            print(f"    ❌ Problème lors de la suppression : {filepath}")
    except Exception as e:
        print(f"    ❌ Impossible de supprimer {filepath} : {e}")


def render_jinja_templates(base_dir):
    """
    Rendu des fichiers `.j2` en utilisant Jinja2, avec suppression forcée de l'original.
    """
    print("\n🔧 Rendu des templates Jinja2...")
    env = Environment(loader=FileSystemLoader(base_dir))

    # Parcours des fichiers `.j2`
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Filtrer uniquement les fichiers `.j2`
            if file.endswith(".j2"):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file[:-3])  # Supprime `.j2`

                print(f"  📄 Traitement du fichier : {old_file_path}")

                try:
                    # Lecture du contenu du modèle `.j2`
                    with open(old_file_path, "r", encoding="utf-8") as old_file:
                        template_content = old_file.read()

                    # Chargement du contexte Cookiecutter
                    context = {
                        "project_name": "{{ cookiecutter.project_name }}",
                        "project_slug": "{{ cookiecutter.project_slug }}",
                        "package_name": "{{ cookiecutter.package_name }}",
                        "framework": "{{ cookiecutter.framework }}",
                        "use_app_folder": "{{ cookiecutter.use_app_folder }}",
                        "use_black": "{{ cookiecutter.use_black }}",
                        "use_ruff": "{{ cookiecutter.use_ruff }}",
                        "use_pytest": "{{ cookiecutter.use_pytest }}",
                        "use_pre_commit": "{{ cookiecutter.use_pre_commit }}",
                        "python_version": "{{ cookiecutter.python_version }}",
                        "author": "{{ cookiecutter.author }}",
                        "_template": r"{{ cookiecutter._template }}",  # FIX
                        "_output_dir": r"{{ cookiecutter._output_dir }}",  # FIX
                        "_repo_dir": r"{{ cookiecutter._repo_dir }}",  # FIX
                        "_checkout": "{{ cookiecutter._checkout }}",
                    }

                    # Transformation avec Jinja2
                    rendered_content = env.from_string(template_content).render(context)

                    # Écriture du contenu rendu dans le fichier sans `.j2`
                    with open(new_file_path, "w", encoding="utf-8") as new_file:
                        new_file.write(rendered_content)
                    print(f"    ✅ Créé : {new_file_path}")

                    # Suppression explicite de l'original `.j2`
                    safe_remove(old_file_path)

                except Exception as e:
                    print(f"    ❌ Erreur : {str(e)}")


def print_final_instructions():
    """
    📝 Instructions pour l'utilisateur.
    """
    print("=" * 40)
    print(f"✅ Projet '{project_slug}' généré avec succès !")
    print("➡️ Étapes suivantes :")
    print(f"cd {project_slug}")
    print("poetry install")
    print(f"poetry run python -m {package_name}")
    print("=" * 40)


# Script principal
if __name__ == "__main__":
    try:
        print("\n🚀 Initialisation du post_gen_project.py...\n")
        # Vérifier que le répertoire de projet existe bien
        if not project_path.exists():
            print(f"❌ Répertoire introuvable : {project_path}")
            sys.exit(1)

        # Supprimer les fichiers inutiles
        clean_unused_files()

        # Rendu des fichiers `.j2`
        render_jinja_templates(project_path)

        # Afficher les instructions finales
        print_final_instructions()
        sys.exit(0)

    except Exception as e:
        print(f"❌ Erreur critique : {e}")
        sys.exit(1)
