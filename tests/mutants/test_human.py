from flaskr.mutants.domain.human import Human


# Vamos a tratar de estructurar todos los tests de la misma manera, siguiendo el
# patrón Arrange, Act, Assert (AAA). De esta manera podemos ver claramente durante
# el testing qué se está haciendo en cada momento y todo lo que necesita una unidad
# para poder ser testeada. En caso de que una función se ponga muy compleja en el
# tiempo, lo vamos a poder visualizar rápidamente porque nos va a llevar una gran
# cantidad de líneas hacer todo el "arrange" para poder testearla correctamente y
# eso nos va a dar un indicador de que es tiempo de refactorizar :)


def test_it_is_mutant_for_two_sequences_with_four_equal_letters_vertically():
    # Vamos a comentar cada parte del patrón AAA en este test para tener como ejemplo

    # Arrange
    dna = ["ATGCGA", "ATGTGC", "ATATGT", "ATAAGG", "CACCTA", "TCACTG"]

    # Act
    is_mutant = Human(dna).is_mutant()

    # Assert
    assert is_mutant


def test_it_is_mutant_for_two_sequences_with_four_equal_letters_horizontally():
    dna = ["AAAAGA", "TTTTGC", "GTGGAG", "ATAAGG", "CACCTA", "TCACTG"]

    is_mutant = Human(dna).is_mutant()

    assert is_mutant


def test_it_is_not_mutant_for_dna_with_no_sequences_with_four_equal_letters():
    dna = ["ATAAGA", "TATTGC", "GTGGAG", "ATAAGG", "CACCTA", "TCACTG"]

    is_mutant = Human(dna).is_mutant()

    assert not is_mutant


def test_is_mutant_for_two_diagonal_equal_letter_sequences():
    dna = ["ATAGGA", "AATGAG", "GGATGA", "AAGATA", "CCGGCC", "GGCCAG"]

    is_mutant = Human(dna).is_mutant()

    assert is_mutant


def test_is_mutant_for_one_clockwise_and_one_counter_clockwise_diagonal_equal_letter_sequences():
    dna = ["ATAGGT", "AATGTG", "GGTTGA", "AATATA", "CCGGCC", "GGCCAG"]

    is_mutant = Human(dna).is_mutant()

    assert is_mutant
