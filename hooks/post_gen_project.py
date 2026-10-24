"""Après génération : retirer ce qui n'a pas été demandé, puis afficher la marche à suivre."""

import os
import shutil

FRAMEWORK = "{{ cookiecutter.framework }}"
PACKAGE_DIR = "{{ cookiecutter.package_dir }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
USE_PYTEST = "{{ cookiecutter.use_pytest }}" == "yes"
USE_PRE_COMMIT = "{{ cookiecutter.use_pre_commit }}" == "yes"
USE_GITHUB_ACTIONS = "{{ cookiecutter.use_github_actions }}" == "yes"


def supprimer(chemin: str) -> None:
    if os.path.isdir(chemin):
        shutil.rmtree(chemin)
    elif os.path.exists(chemin):
        os.remove(chemin)


def main() -> None:
    if not USE_PYTEST:
        supprimer("tests")
    if not USE_PRE_COMMIT:
        supprimer(".pre-commit-config.yaml")
    if not USE_GITHUB_ACTIONS:
        supprimer(".github")

    print(f"✅ Projet « {PROJECT_SLUG} » généré.")
    print("➡️  Étapes suivantes :")
    print(f"   cd {PROJECT_SLUG}")
    print("   git init && poetry install")
    if USE_PRE_COMMIT:
        print("   poetry run pre-commit install")
    if FRAMEWORK == "django":
        print("   poetry run django-admin startproject config .")
        print("   poetry run python manage.py runserver")
    elif FRAMEWORK == "flask":
        print(f"   poetry run flask --app {PACKAGE_DIR}.main run")
    else:
        print(f"   poetry run python -m {PACKAGE_DIR}.main")


if __name__ == "__main__":
    main()
