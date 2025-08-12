# Modèle Cookiecutter Python Template

## Description
Ce projet permet de générer des templates Python adaptables pour divers cas d'utilisation (scripts, Django, Flask, etc.) à l'aide de l'outil Cookiecutter. Il propose une structure prédéfinie et intégrée, offrant des bonnes pratiques pour le développement, les tests, l'intégration continue et la personnalisation.

## Fonctionnalités
- Génération automatique de projets Python configurés.
- Supporte plusieurs frameworks : script simple, Django, Flask, etc.
- Intégration avec **GitLab CI/CD** via `.gitlab-ci.yml`.
- Validation de code et hooks avec **pre-commit**.
- Modèle personnalisable via `cookiecutter.json`.
- Scripts avant/après génération grâce à `pre_gen_project.py`.

## Structure générée
Voici un exemple de structure générée par ce template :

```text
.
├── .gitlab-ci.yml           # Configuration CI/CD pour GitLab
├── cookiecutter.json        # Fichier de configuration pour votre modèle
├── pre_gen_project.py       # Script exécuté avant la génération du projet
├── post_gen_project.py      # Script exécuté après la génération du projet
├── src/                     # Répertoire contenant le code principal
│   ├── __init__.py
│   ├── main.py              # Exemple de script Python principal
├── tests/                   # Répertoire pour les tests unitaires
│   ├── __init__.py
│   ├── test_main.py         # Exemple de fichier de test avec pytest
├── requirements.txt         # Dépendances Python
├── README.md                # Documentation principale
├── setup.py                 # Script d'installation pour votre projet
└── LICENSE                  # Licence du projet
```

## Installation
### Prérequis
1. Installer **Python 3.7+**
2. Installer **Cookiecutter** via pip :
   ```bash
   pip install cookiecutter
   ```

### Génération d’un projet
Utilisez Cookiecutter pour créer un nouveau projet. Exemple :
```bash
cookiecutter https://github.com/mon-utilisateur/mon-modele-cookiecutter.git
```

Suivez les instructions interactives pour personnaliser votre projet.

## Utilisation
1. Accédez au répertoire généré.
2. Configurez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécutez le projet :
   ```bash
   python src/main.py
   ```

## Développement
### Préparation
Assurez-vous de configurer les hooks pre-commit :
```bash
pre-commit install
```
Les hooks vérifient automatiquement le respect des bonnes pratiques lors des commits.

### Bonnes pratiques
- Respectez les conventions **PEP 8**.
- Ajoutez des tests pour toute nouvelle fonctionnalité.
- Documentez les modifications majeures dans le README.

## Intégration CI/CD
Ce modèle inclut une configuration pour GitLab CI/CD via `.gitlab-ci.yml` :
- **Linting** : Vérifie le style de code.
- **Tests unitaires** : Exécute les tests avec `pytest`.
- **Déploiement** (optionnel) : Ajoutez un job de déploiement personnalisé.

Pour activer la CI/CD, configurez votre projet GitLab après le premier commit.

## Personnalisation
Modifiez `cookiecutter.json` selon vos besoins. Exemple :

```json
{
  "project_name": "Mon Projet",
  "author_name": "Votre Nom",
  "framework": ["none", "django", "flask"]
}
```

Ajoutez des scripts avant ou après génération dans `pre_gen_project.py` ou `post_gen_project.py`.

## Tests
Pour exécuter les tests :
```bash
pytest
```
Assurez-vous que votre code est correctement testé avant tout déploiement.

## Contribuer
1. Forkez ce dépôt.
2. Travaillez dans une branche :
   ```bash
   git checkout -b ma-fonctionnalite
   ```
3. Soumettez une pull request et décrivez vos modifications.

## FAQ
### Pourquoi utiliser Cookiecutter ?
Pour accélérer et normaliser la création de projets Python prêts à l’emploi.

### Puis-je ajouter d'autres frameworks ?
Oui ! Ajoutez simplement ces options dans `cookiecutter.json` et modifiez les scripts de génération si nécessaire.

### Où signaler un problème ?
Ouvrez une issue dans le dépôt GitHub.

## À propos
Ce modèle a été conçu pour simplifier la création et la maintenance de projets Python, en mettant en avant les meilleures pratiques.

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.