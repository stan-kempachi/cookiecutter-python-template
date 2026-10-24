# Changelog

## 2.0.0 (2026-10-25)

### Refonte

- CI GitHub Actions pour le template et pour les projets générés (fin de GitLab CI, Husky et standard-version)
- hooks réécrits : validation des réponses, suppression réelle des options non retenues
- `use_app_folder` produit un seul dossier de code (`app/` ou le nom du package), plus les deux
- projet généré : `pyproject.toml` configuré (black/isort/ruff/pytest), README et `main.py` adaptés au framework, `.gitignore`
- tests du template : options, frameworks, slug invalide, exécution réelle du projet généré

## 1.0.3 (2025-08-29) · 1.0.2 (2025-08-29) · 1.0.1 (2025-08-24)

Versions initiales, publiées depuis GitLab avec standard-version.
