{%- if cookiecutter.framework == "flask" %}
from flask import Flask

app = Flask(__name__)


@app.get("/")
def index() -> dict:
    return {"message": "Hello depuis {{ cookiecutter.project_name }} !"}


if __name__ == "__main__":
    app.run(debug=True)
{%- elif cookiecutter.framework == "django" %}
"""Point d'entrée : après `django-admin startproject config .`, lancez `python manage.py runserver`."""


def main() -> None:
    print("Projet Django {{ cookiecutter.project_name }} — lancez `django-admin startproject config .`")


if __name__ == "__main__":
    main()
{%- else %}
def main() -> None:
    print("Hello depuis {{ cookiecutter.project_name }} !")


if __name__ == "__main__":
    main()
{%- endif %}
