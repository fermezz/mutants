import json
from unittest.mock import patch

import flaskr.api.views


@patch("flaskr.api.views.NonMutant")
@patch("flaskr.api.views.Mutant")
@patch("flaskr.api.views.Human")
def test_human_object_is_initialized_with_the_passed_dna(patched_human, patched_mutant, pathced_non_mutant, client):
    dna = ["ATGCGA", "ATGTGC", "ATATGT", "ATAAGG", "CACCTA", "TCACTG"]
    payload = json.dumps({"dna": dna})

    client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_human.assert_called_once_with(dna)


@patch("flaskr.api.views.NonMutant")
@patch("flaskr.api.views.Mutant")
@patch.object(flaskr.api.views.Human, "is_mutant", return_value=True)
def test_it_should_return_200_if_human_is_mutant(patched_is_mutant, patched_mutant, patched_non_mutant, client):
    dna = ["ATGCGA", "ATGTGC", "ATATGT", "ATAAGG", "CACCTA", "TCACTG"]
    payload = json.dumps({"dna": dna})

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_is_mutant.assert_called_once()
    patched_mutant.assert_called_once_with(dna=dna)
    patched_non_mutant.assert_not_called()
    assert 200 == response.status_code


@patch("flaskr.api.views.NonMutant")
@patch("flaskr.api.views.Mutant")
@patch.object(flaskr.api.views.Human, "is_mutant", return_value=False)
def test_it_should_return_403_if_human_is_not_mutant(patched_is_mutant, patched_mutant, patched_non_mutant, client):
    dna = ["GTGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CC2CTA", "TCACTG"]
    payload = json.dumps({"dna": dna})

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_is_mutant.assert_called_once()
    patched_mutant.assert_not_called()
    patched_non_mutant.assert_called_once_with(dna=dna)
    assert 403 == response.status_code


@patch("flaskr.api.views.Human")
def test_it_should_return_400_if_dna_is_absent(patched_human, client):
    payload = json.dumps({})  # Empty payload

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_human.assert_not_called()
    assert 400 == response.status_code
