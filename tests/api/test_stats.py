from unittest.mock import Mock, patch

from flaskr.api.views import get_mutant_estimated_document_count, get_non_mutant_estimated_document_count


@patch("flaskr.api.views.get_mutant_estimated_document_count")
@patch("flaskr.api.views.get_non_mutant_estimated_document_count")
def test_stats_are_zero_with_no_data(patched_non_mutant_count, patched_mutant_count, client):
    patched_mutant_count.return_value = 0
    patched_non_mutant_count.return_value = 0

    response = client.get("/api/stats/")

    assert 200 == response.status_code
    assert {
        "count_mutant_dna": 0,
        "count_human_dna": 0,
        "ratio": 0.00,
    } == response.json


@patch("flaskr.api.views.get_mutant_estimated_document_count")
@patch("flaskr.api.views.get_non_mutant_estimated_document_count")
def test_stats_are_accurate_with_data(patched_non_mutant_count, patched_mutant_count, client):
    patched_mutant_count.return_value = 40
    patched_non_mutant_count.return_value = 60

    response = client.get("/api/stats/")

    assert 200 == response.status_code
    assert {
        "count_mutant_dna": 40,
        "count_human_dna": 100,
        "ratio": 0.4,
    } == response.json


@patch("flaskr.api.views.get_db")
def test_mutant_estimated_count_is_called_on_the_mutant_collection(patched_get_db):
    mocked_mutant_collection = Mock(name="mutant_collection")
    mocked_db = Mock(name="db")
    mocked_db.mutant = mocked_mutant_collection
    patched_get_db.return_value = mocked_db

    get_mutant_estimated_document_count()

    mocked_mutant_collection.estimated_document_count.assert_called_once_with()


@patch("flaskr.api.views.get_db")
def test_non_mutant_estimated_count_is_called_on_the_non_mutant_collection(patched_get_db):
    mocked_non_mutant_collection = Mock(name="non_mutant_collection")
    mocked_db = Mock(name="db")
    mocked_db.non_mutant = mocked_non_mutant_collection
    patched_get_db.return_value = mocked_db

    get_non_mutant_estimated_document_count()

    mocked_non_mutant_collection.estimated_document_count.assert_called_once_with()
