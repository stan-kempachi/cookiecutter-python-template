import os

from jinja2 import Environment, FileSystemLoader

# Attributs globaux (exemple pour le contexte global)
stdout = None
project_slug = None
package_name = None
framework = None
project_path = None
package_path = None


def clean_unused_files():
    """
    Supprime les fichiers inutiles qui ne correspondent pas au framework ou au contexte défini.
    """
    try:
        # Logique existante pour la suppression
        print("🔍 Suppression des fichiers inutiles...")
    except Exception as e:
        print(f"❌ Erreur dans clean_unused_files : {e}")


def safe_remove(filepath):
    """
    Supprime un fichier de façon sécurisée s'il existe.
    """
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"✔️ Fichier supprimé : {filepath}")
    except PermissionError as e:
        print(
            f"❌ Permission refusée lors de la suppression du fichier {filepath} : {e}"
        )
    except Exception as e:
        print(f"❌ Erreur lors de la suppression du fichier {filepath} : {e}")


def render_jinja_templates():
    """
    Rendu des templates Jinja2 et suppression de l'extension `.j2` une fois le rendu effectué.
    """
    try:
        templates_dir = os.getcwd()  # Répertoire contenant les fichiers .j2
        env = Environment(loader=FileSystemLoader(templates_dir))

        for root, dirs, files in os.walk(templates_dir):
            for file in files:
                if file.endswith(".j2"):
                    file_path = os.path.join(root, file)
                    rendered_file_path = os.path.splitext(file_path)[
                        0
                    ]  # Chemin sans l'extension .j2

                    try:
                        # Lecture du contenu du template
                        with open(file_path, "r", encoding="utf-8") as template_file:
                            template = env.from_string(template_file.read())

                        # Rendu avec les variables existantes
                        rendered_content = template.render(
                            project_slug=project_slug,
                            package_name=package_name,
                            framework=framework,
                            project_path=project_path,
                            package_path=package_path,
                        )

                        # Écriture dans un fichier sans extension .j2
                        with open(
                            rendered_file_path, "w", encoding="utf-8"
                        ) as rendered_file:
                            rendered_file.write(rendered_content)
                            print(f"✔️ Rendu du fichier : {rendered_file_path}")

                        # Suppression du template source
                        safe_remove(file_path)

                    except Exception as e:
                        print(f"❌ Erreur lors du rendu de {file_path} : {e}")

    except Exception as e:
        print(f"❌ Erreur générale dans render_jinja_templates : {e}")


def print_final_instructions():
    """
    Affiche les instructions finales pour l'utilisateur une fois le projet généré.
    """
    try:
        # Logique actuelle
        print(f"✅ Projet '{project_slug}' généré avec succès !")
        print("➡️ Étapes suivantes :")
        print(f"cd {project_slug}")
        print("poetry install")
        print(f"poetry run python -m {package_name}")
        print("=" * 40)
    except Exception as e:
        print(f"❌ Erreur dans print_final_instructions : {e}")


def main():
    """
    Fonction principale exécutée après la génération du projet via Cookiecutter.
    """
    global stdout, project_slug, package_name, framework, project_path, package_path

    # Initialisation des variables globales
    stdout = os.sys.stdout
    project_slug = "{{ cookiecutter.project_slug }}"
    package_name = "{{ cookiecutter.package_name }}"
    framework = "{{ cookiecutter.framework }}"
    project_path = os.getcwd()
    package_path = os.path.join(project_path, package_name)

    print("🚀 Initialisation du script post_gen_project.py...")

    # Appeler les différentes fonctions
    try:
        clean_unused_files()  # Suppression des fichiers inutiles en fonction du contexte
        render_jinja_templates()  # Rendu des templates Jinja2
        print_final_instructions()  # Messages finaux pour l'utilisateur
    except Exception as e:
        print(f"❌ Erreur critique dans le script principal : {e}")


if __name__ == "__main__":
    main()
