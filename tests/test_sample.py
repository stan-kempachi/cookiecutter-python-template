# tests/test_sample.py


def test_basic_math():
    """Exemple de test unitaire simple."""
    assert 2 + 2 == 4


def test_string_operations():
    """Test des opérations simples de chaîne de caractères."""
    name = "GitLab CI"
    assert name.upper() == "GITLAB CI"
    assert name.lower() == "gitlab ci"
