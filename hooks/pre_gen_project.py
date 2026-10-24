"""Validation des réponses avant génération."""

import re
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

IDENTIFIANT = re.compile(r"^[a-z][a-z0-9_]*$")

erreurs = []
if not IDENTIFIANT.match(PROJECT_SLUG):
    erreurs.append(f"project_slug « {PROJECT_SLUG} » doit être un identifiant Python (minuscules, chiffres, _).")
if not IDENTIFIANT.match(PACKAGE_NAME):
    erreurs.append(f"package_name « {PACKAGE_NAME} » doit être un identifiant Python (minuscules, chiffres, _).")
if not re.match(r"^3\.(1[0-9]|[2-9][0-9])$", PYTHON_VERSION):
    erreurs.append(f"python_version « {PYTHON_VERSION} » : attendu 3.10 ou plus (ex. 3.12).")

if erreurs:
    print("❌ Génération annulée :")
    for e in erreurs:
        print(f"   - {e}")
    sys.exit(1)
