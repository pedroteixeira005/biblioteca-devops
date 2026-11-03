from src.biblioteca import adicionar_livro
from src.biblioteca import livro_valido
from src.biblioteca import buscar_livro


def test_adicionar_livro():
    livro = adicionar_livro("Clean Code", "Robert C. Martin")
    assert livro["titulo"] == "Clean Code"
    assert livro["autor"] == "Robert C. Martin"


def test_livro_valido():
    livro = adicionar_livro("Effective Java", "Joshua Bloch")
    assert livro_valido(livro) is True


def test_livro_invalido():
    livro = adicionar_livro("", "")
    assert livro_valido(livro) is False


def test_buscar_livro_encontrado():
    livros = [
        {"titulo": "Clean Code", "autor": "Robert C. Martin"},
        {"titulo": "Effective Java", "autor": "Joshua Bloch"}
    ]

    resultado = buscar_livro("Clean Code", livros)
    assert resultado["titulo"] == "Clean Code"


def test_buscar_livro_nao_encontrado():
    livros = [
        {"titulo": "Clean Code", "autor": "Robert C. Martin"}
    ]

    resultado = buscar_livro("Python", livros)
    assert resultado is None


def test_buscar_livro_titulo_vazio():
    livros = [
        {"titulo": "Clean Code", "autor": "Robert C. Martin"}
    ]

    resultado = buscar_livro("", livros)
    assert resultado is None
