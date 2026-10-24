# {{ cookiecutter.project_name }}

{%- if cookiecutter.use_github_actions == "yes" %}

![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF)
{%- endif %}

Projet Python ({{ "application Django" if cookiecutter.framework == "django" else "application Flask" if cookiecutter.framework == "flask" else "script / bibliothèque" }}) géré avec [Poetry](https://python-poetry.org/).

## Démarrer

```bash
poetry install
{%- if cookiecutter.use_pre_commit == "yes" %}
poetry run pre-commit install
{%- endif %}
{%- if cookiecutter.framework == "django" %}
poetry run django-admin startproject config .
poetry run python manage.py runserver
{%- elif cookiecutter.framework == "flask" %}
poetry run flask --app {{ cookiecutter.package_dir }}.main run
{%- else %}
poetry run python -m {{ cookiecutter.package_dir }}.main
{%- endif %}
```

## Qualité
{%- if cookiecutter.use_pytest == "yes" %}

```bash
poetry run pytest
```
{%- endif %}
{%- if cookiecutter.use_black == "yes" or cookiecutter.use_ruff == "yes" %}

```bash
{%- if cookiecutter.use_black == "yes" %}
poetry run black . && poetry run isort .
{%- endif %}
{%- if cookiecutter.use_ruff == "yes" %}
poetry run ruff check .
{%- endif %}
```
{%- endif %}

## Structure

```
{{ cookiecutter.package_dir }}/     code source
{%- if cookiecutter.use_pytest == "yes" %}
tests/              tests pytest
{%- endif %}
pyproject.toml      dépendances et configuration des outils
```
