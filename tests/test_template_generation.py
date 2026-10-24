import subprocess
import sys
import tomllib
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

TEMPLATE = str(Path(__file__).resolve().parents[1])


def generer(tmp_path, **extra):
    chemin = cookiecutter(TEMPLATE, no_input=True, output_dir=str(tmp_path), extra_context=extra)
    return Path(chemin)


def test_generation_par_defaut(tmp_path):
    projet = generer(tmp_path)
    assert projet.name == "mon_super_projet"
    assert (projet / "mon_super_projet" / "main.py").exists()
    assert not (projet / "app").exists()
    assert (projet / "tests" / "test_main.py").exists()
    assert (projet / ".pre-commit-config.yaml").exists()
    assert (projet / ".github" / "workflows" / "ci.yml").exists()
    assert not list(projet.rglob("*.j2"))

    pyproject = tomllib.loads((projet / "pyproject.toml").read_text())
    assert pyproject["tool"]["poetry"]["packages"] == [{"include": "mon_super_projet"}]
    assert "pytest" in pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"]


def test_dossier_app(tmp_path):
    projet = generer(tmp_path, use_app_folder="yes")
    assert (projet / "app" / "main.py").exists()
    assert not (projet / "mon_super_projet").exists()
    assert "{{" not in (projet / "tests" / "test_main.py").read_text()
    assert 'packages = [{ include = "app" }]' in (projet / "pyproject.toml").read_text()


def test_options_desactivees(tmp_path):
    projet = generer(
        tmp_path, use_pytest="no", use_pre_commit="no", use_github_actions="no", use_black="no", use_ruff="no"
    )
    assert not (projet / "tests").exists()
    assert not (projet / ".pre-commit-config.yaml").exists()
    assert not (projet / ".github").exists()
    dev = tomllib.loads((projet / "pyproject.toml").read_text())["tool"]["poetry"]["group"]["dev"]["dependencies"]
    assert dev == {}


@pytest.mark.parametrize("framework,dep", [("flask", "flask"), ("django", "django")])
def test_frameworks(tmp_path, framework, dep):
    projet = generer(tmp_path, framework=framework)
    pyproject = tomllib.loads((projet / "pyproject.toml").read_text())
    assert dep in pyproject["tool"]["poetry"]["dependencies"]
    assert (projet / "README.md").read_text().count("poetry run") >= 1


def test_slug_invalide_refuse(tmp_path):
    with pytest.raises(FailedHookException):
        generer(tmp_path, project_slug="Mon-Projet")


def test_projet_genere_est_executable(tmp_path):
    """Le script généré tourne et son test passe, sans Poetry (PYTHONPATH direct)."""
    projet = generer(tmp_path)
    run = subprocess.run(
        [sys.executable, "-m", "mon_super_projet.main"], cwd=projet, capture_output=True, text=True, check=True
    )
    assert "Hello depuis Mon super projet" in run.stdout
    subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], cwd=projet, check=True, capture_output=True)
