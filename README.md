# cookiecutter-python-template

[![CI](https://github.com/stan-kempachi/cookiecutter-python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/stan-kempachi/cookiecutter-python-template/actions/workflows/ci.yml)
![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)
![Licence MIT](https://img.shields.io/badge/licence-MIT-green)

Template [Cookiecutter](https://cookiecutter.readthedocs.io/) pour démarrer un projet Python propre en une commande : Poetry, pre-commit, black/isort/ruff, pytest et un workflow GitHub Actions déjà en place. Trois variantes : script ou bibliothèque, application Flask, application Django.

## Utilisation

```bash
pip install cookiecutter
cookiecutter https://github.com/stan-kempachi/cookiecutter-python-template.git
```

Puis, dans le projet généré :

```bash
git init && poetry install
poetry run pre-commit install
poetry run python -m <package>.main        # script
poetry run flask --app <package>.main run  # flask
poetry run django-admin startproject config . && poetry run python manage.py runserver  # django
```

Génération non interactive :

```bash
cookiecutter gh:stan-kempachi/cookiecutter-python-template --no-input project_name="Mon API" framework=flask
```

## Options

| Variable | Valeurs | Effet |
|---|---|---|
| `project_name` | texte | Nom affiché ; `project_slug` et `package_name` en sont dérivés |
| `framework` | `script` (défaut), `flask`, `django` | Dépendance ajoutée, `main.py` et README adaptés |
| `use_app_folder` | `no` (défaut), `yes` | Code dans `app/` plutôt que dans `<package_name>/` |
| `use_black` | `yes` / `no` | black + isort (dépendances, config, hooks, CI) |
| `use_ruff` | `yes` / `no` | ruff (dépendance, config, hook, CI) |
| `use_pytest` | `yes` / `no` | pytest + dossier `tests/` avec un test d'exemple |
| `use_pre_commit` | `yes` / `no` | `.pre-commit-config.yaml` |
| `use_github_actions` | `yes` / `no` | `.github/workflows/ci.yml` (lint + tests) |
| `python_version` | `3.12` | Version minimale (`^3.12` dans Poetry, cibles black/ruff) |
| `author` | `Nom <email>` | Champ `authors` du `pyproject.toml` |

Les hooks valident les réponses (`project_slug` et `package_name` doivent être des identifiants Python) et retirent du projet généré tout ce qui n'a pas été demandé.

## Projet généré

```
mon_super_projet/
├── .github/workflows/ci.yml   lint + tests sur GitHub Actions
├── .gitignore
├── .pre-commit-config.yaml    pre-commit-hooks, black, isort, ruff
├── README.md                  commandes de démarrage adaptées au framework
├── pyproject.toml             Poetry + config black / isort / ruff / pytest
├── mon_super_projet/          (ou app/ avec use_app_folder=yes)
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```

## Développer le template

```bash
pip install -r requirements-dev.txt
pytest -q                                   # génération dans un dossier temporaire, options, frameworks, exécution du projet généré
ruff check hooks tests && ruff format --check hooks tests
```

La CI du template régénère un projet pour chaque framework et vérifie qu'il passe `poetry check`.

## Licence

[MIT](LICENSE).
