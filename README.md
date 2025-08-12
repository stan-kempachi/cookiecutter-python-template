# Modèle Cookiecutter Python Template

## Description
Ce projet offre une solution clé en main pour générer des templates Python modulaires adaptés à divers cas d'utilisation (scripts, Django, Flask, etc.) grâce à l'outil **Cookiecutter**. Ce modèle fournit une structure préconfigurée basée sur les bonnes pratiques en matière de développement, tests, intégration continue et personnalisation. La gestion des dépendances est simplifiée grâce à **Poetry**, garantissant un environnement robuste et moderne.

## Fonctionnalités
- Génération automatique et rapide de projets Python prêts à l'emploi.
- Compatibilité avec plusieurs frameworks : script, Django, Flask, etc.
- Prise en charge native de **GitLab CI/CD** via `.gitlab-ci.yml`.
- Validation du code et gestion des hooks grâce à **pre-commit**.
- Structure personnalisable via `cookiecutter.json`.
- Scripts d'exécution avant/après génération grâce à `pre_gen_project.py` et `post_gen_project.py`.

## Structure générée
Voici un exemple de structure générée avec ce template :

```text
.
├── .gitlab-ci.yml           # Configuration CI/CD pour GitLab
├── .pre-commit-config.yaml  # Configuration des hooks pre-commit
├── cookiecutter.json        # Fichier de personnalisation pour le template
├── pre_gen_project.py       # Script exécuté avant la génération
├── post_gen_project.py      # Script exécuté après la génération
├── src/                     # Dossier contenant le code principal
│   ├── __init__.py
│   ├── main.py              # Exemple de script principal
├── tests/                   # Dossier pour les tests unitaires
│   ├── __init__.py
│   ├── test_main.py         # Tests avec pytest
├── pyproject.toml           # Gestion des dépendances avec Poetry
├── poetry.lock              # Verrouillage des dépendances généré par Poetry
├── README.md                # Documentation du projet
└── LICENSE                  # Licence du projet
```

## Installation

### Prérequis
1. Installer **Python 3.7+**.
2. Installer **Cookiecutter** via pip :
   ```bash
   pip install cookiecutter
   ```
3. Installer **Poetry** :
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

### Création d’un projet
Pour générer un nouveau projet, utilisez Cookiecutter :
```bash
cookiecutter https://github.com/stan-kempachi/cookiecutter-python-template.git
```
Suivez les instructions pour personnaliser votre projet.

## Utilisation
1. Naviguez vers le répertoire généré.
2. Installez les dépendances avec **Poetry** :
   ```bash
   poetry install
   ```
3. Lancez votre application :
   ```bash
   poetry run python src/main.py
   ```

## Développement

### Préparation
Pour configurer les hooks **pre-commit**, exécutez :
```bash
pre-commit install
```
Ces hooks vérifient automatiquement votre code avant chaque commit.

### Gestion des dépendances
- Ajouter une dépendance principale :
  ```bash
  poetry add <nom-du-paquet>
  ```
- Ajouter une dépendance de développement uniquement :
  ```bash
  poetry add --dev <nom-du-paquet>
  ```

### Tests unitaires
Exécuter les tests :
```bash
poetry run pytest
```
Assurez-vous que tous les tests passent avant tout déploiement.

### Bonnes pratiques
- Respectez les conventions **PEP 8**.
- Ajoutez des tests pour toute nouvelle fonctionnalité.
- Mettez à jour la documentation en cas de modification importante.

## Intégration CI/CD
Ce template inclut un fichier `.gitlab-ci.yml` qui configure automatiquement les pipelines pour GitLab CI/CD :
- **Linting** : Pour vérifier la qualité du code.
- **Tests unitaires** : Exécution des tests automatisés avec **pytest**.
- **Déploiement** : Ajoutez une configuration personnalisée pour vos besoins.

Pour activer la CI/CD, créez un dépôt GitLab et effectuez un **commit** initial.

## Personnalisation
Adaptez `cookiecutter.json` pour ajuster le modèle à vos besoins spécifiques. Exemple :

```json
{
  "project_name": "Mon Projet",
  "author_name": "Votre Nom",
  "framework": ["none", "django", "flask"]
}
```

Il est également possible d’ajouter des scripts pré et post génération via `pre_gen_project.py` et `post_gen_project.py`.

---

## Licence
Ce projet est distribué sous la licence [MIT](LICENSE).