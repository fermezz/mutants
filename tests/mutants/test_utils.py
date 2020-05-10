from flaskr.mutants.utils import Matrix


def test_matrix_returns_rows_correctly():
    matrix = ["abc", "def", "ghi"]

    rows = list(Matrix(matrix).get_rows())

    assert matrix == rows


def test_matrix_returns_columns_correctly():
    matrix = ["abc", "def", "ghi"]

    columns = list(Matrix(matrix).get_columns())

    expected_columns = ["cfi", "beh", "adg"]
    assert expected_columns == columns


def test_matrix_returns_diagonals_correctly():
    matrix = ["abc", "def", "ghi"]

    diagonals = list(Matrix(matrix).get_all_diagonals())

    expected_diagonals = ["a", "c", "bd", "fb", "ceg", "iea", "fh", "hd", "i", "g"]
    assert expected_diagonals == diagonals
