import shutil
from pathlib import Path

from cookiecutter.main import cookiecutter


def test_generate_template():
    """Test verifying that the template generation works with default parameters."""
    # Cible pour la génération de templates
    output_dir = Path("test_generated_template").resolve()

    # Nettoyage si le répertoire existe déjà
    if output_dir.exists():
        shutil.rmtree(output_dir)

    try:
        # Génération du projet avec Cookiecutter
        cookiecutter(
            str(Path(".").resolve()), no_input=True, output_dir=str(output_dir)
        )
    except Exception as e:
        print(f"Erreur lors de la génération du template : {e}")
        raise
