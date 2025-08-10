import json
from collections import OrderedDict
from pathlib import Path


def main():
    """Exemple de hook pré-génération."""
    # Définir le chemin racine (répertoire actuel du fichier)
    project_root = Path(
        __file__
    ).parent  # Pas d'utilisation de resolve() pour garder les chemins relatifs

    # Chemins relatifs
    template_dir = project_root / "template"
    output_dir = template_dir / "test_generated_template"
    repo_dir = project_root

    # Créer le contexte avec chemins relatifs
    context = OrderedDict(
        {
            "project_name": "Mon super projet",
            "project_slug": "mon_super_projet",
            "package_name": "core",
            "framework": "script",
            "use_app_folder": "yes",
            "use_black": "yes",
            "use_ruff": "yes",
            "use_pytest": "yes",
            "use_pre_commit": "yes",
            "python_version": "3.12",
            "author": "Anonyme <anonyme@example.com>",
            "_template": str(template_dir).replace(str(project_root), "<project_root>"),
            "_output_dir": str(output_dir).replace(str(project_root), "<project_root>"),
            "_repo_dir": str(repo_dir).replace(str(project_root), "<project_root>"),
            "_checkout": None,
        }
    )

    # Éventuelles opérations supplémentaires sur le contexte
    print(f"Contexte validé : {json.dumps(context, indent=4)}")


if __name__ == "__main__":
    main()
