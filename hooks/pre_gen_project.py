from collections import OrderedDict
from pathlib import Path


def main():
    """Exemple de hook pré-génération."""
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
            "_template": str(
                Path(
                    "C:/Users/pc/Dropbox/Stan/PycharmProjects/cookiecutter-python-template"
                ).resolve()
            ),
            "_output_dir": str(
                Path(
                    "C:/Users/pc/Dropbox/Stan/PycharmProjects/cookiecutter-python-template/test_generated_template"
                ).resolve()
            ),
            "_repo_dir": str(
                Path(
                    "C:/Users/pc/Dropbox/Stan/PycharmProjects/cookiecutter-python-template"
                ).resolve()
            ),
            "_checkout": None,
        }
    )

    # Éventuelles opérations supplémentaires sur le contexte
    print(f"Contexte validé : {context}")


if __name__ == "__main__":
    main()
