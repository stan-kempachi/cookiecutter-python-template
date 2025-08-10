from pathlib import Path


project_slug = "{{ cookiecutter.project_slug }}"
package_name = "{{ cookiecutter.package_name }}"
framework = "{{ cookiecutter.framework }}"

# 📁 Point de départ : le dossier du projet généré
project_path = Path.cwd() / project_slug
package_path = project_path / package_name

# 🧹 Supprimer les fichiers inutiles
if framework != "django":
    django_file = package_path / "manage.py"
    if django_file.exists():
        django_file.unlink()

if framework != "flask":
    flask_file = package_path / "flask_app.py"
    if flask_file.exists():
        flask_file.unlink()

# 💬 Message de fin
print("=" * 40)
print(f"✅ Projet '{project_slug}' généré avec succès !")
print("➡️ Étapes suivantes :")
print("1. cd", project_slug)
print("2. poetry install")
print("3. poetry run python -m", package_name)
print("=" * 40)
