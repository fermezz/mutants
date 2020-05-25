from datetime import datetime, timedelta
from unittest.mock import Mock, patch


@patch('flaskr.api.utils.datetime')
@patch("flaskr.api.views.get_db")
def test_stats_are_zero_with_no_data(patched_get_db, patched_datetime, client):
    patched_datetime.utcnow.return_value = datetime.utcnow() + timedelta(seconds=11)
    db_mock = Mock(name="db")
    mutant_mock = Mock(name="mutant")
    mutant_mock.estimated_document_count.return_value = 0
    non_mutant_mock = Mock(name="non_mutant")
    non_mutant_mock.estimated_document_count.return_value = 0
    db_mock.mutant = mutant_mock
    db_mock.non_mutant = non_mutant_mock
    patched_get_db.return_value = db_mock

    response = client.get("/api/stats/")

    assert 200 == response.status_code
    assert {
        "count_mutant_dna": 0,
        "count_human_dna": 0,
        "ratio": 0.00,
    } == response.json


@patch('flaskr.api.utils.datetime')
@patch("flaskr.api.views.get_db")
def test_stats_are_accurate_with_data(patched_get_db, patched_datetime, client):
    patched_datetime.utcnow.return_value = datetime.utcnow() + timedelta(seconds=11)
    db_mock = Mock(name="db")
    mutant_mock = Mock(name="mutant")
    mutant_mock.estimated_document_count.return_value = 40
    non_mutant_mock = Mock(name="non_mutant")
    non_mutant_mock.estimated_document_count.return_value = 60
    db_mock.mutant = mutant_mock
    db_mock.non_mutant = non_mutant_mock
    patched_get_db.return_value = db_mock

    response = client.get("/api/stats/")

    assert 200 == response.status_code
    assert {
        "count_mutant_dna": 40,
        "count_human_dna": 100,
        "ratio": 0.4,
    } == response.json
