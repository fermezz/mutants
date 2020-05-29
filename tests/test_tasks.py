from unittest.mock import Mock, patch

from flaskr.tasks import save_human


@patch("flaskr.tasks.NonMutant")
@patch("flaskr.tasks.Mutant")
def test_save_human_calls_mutant_document_if_is_mutant(patched_mutant, patched_non_mutant):
    dna = ["AAAA", "CCCC", "GGGG", "TTTT"]
    is_mutant = True
    mocked_mutant_object = Mock(name="mutant")
    patched_mutant.return_value = mocked_mutant_object

    save_human(dna, is_mutant)

    patched_mutant.assert_called_once_with(dna=dna)
    mocked_mutant_object.save.assert_called_once_with()
    patched_non_mutant.assert_not_called()


@patch("flaskr.tasks.NonMutant")
@patch("flaskr.tasks.Mutant")
def test_save_human_calls_non_mutant_document_if_is_not_mutant(patched_mutant, patched_non_mutant):
    dna = ["AACC", "CCAA", "GGTT", "TTGG"]
    is_mutant = False
    mocked_non_mutant_object = Mock(name="non_mutant")
    patched_non_mutant.return_value = mocked_non_mutant_object

    save_human(dna, is_mutant)

    patched_non_mutant.assert_called_once_with(dna=dna)
    mocked_non_mutant_object.save.assert_called_once_with()
    patched_mutant.assert_not_called()
