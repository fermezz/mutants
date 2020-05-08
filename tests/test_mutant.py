from mutants.human import Human


def test_it_is_mutant_for_two_sequences_with_for_equal_letters_vertically() -> None:
    dna = ["ATGCGA","ATGTGC","ATATGT","ATAAGG","CACCTA","TCACTG"]

    assert Human(dna).is_mutant()

def test_it_is_mutant_for_two_sequences_with_for_equal_letters_horizontally() -> None:
    dna = ["AAAAGA","TTTTGC","GTGGAG","ATAAGG","CACCTA","TCACTG"]

    assert Human(dna).is_mutant()

def test_it_is_not_mutant() -> None:
    dna = ["ATAAGA","TATTGC","GTGGAG","ATAAGG","CACCTA","TCACTG"]

    assert not Human(dna).is_mutant()
