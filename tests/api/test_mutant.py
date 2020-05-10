import json
from unittest.mock import patch

import flaskr.api


@patch("flaskr.api.Human")
def test_human_object_is_initialized_with_the_passed_dna(patched_human, client):
    dna = ["ATGCGA", "ATGTGC", "ATATGT", "ATAAGG", "CACCTA", "TCACTG"]
    payload = json.dumps({"dna": dna})

    client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_human.assert_called_once_with(dna)


@patch.object(flaskr.api.Human, "is_mutant", return_value=True)
def test_it_should_return_200_if_human_is_mutant(patched_is_mutant, client):
    dna = ["ATGCGA", "ATGTGC", "ATATGT", "ATAAGG", "CACCTA", "TCACTG"]
    payload = json.dumps({"dna": dna})

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_is_mutant.assert_called_once()
    assert 200 == response.status_code


@patch.object(flaskr.api.Human, "is_mutant", return_value=False)
def test_it_should_return_403_if_human_is_not_mutant(patched_is_mutant, client):
    payload = json.dumps({
        "dna": ["GTGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CC2CTA", "TCACTG"],
    })

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_is_mutant.assert_called_once()
    assert 403 == response.status_code


@patch("flaskr.api.Human")
def test_it_should_return_400_if_dna_is_absent(patched_human, client):
    payload = json.dumps({})  # Empty payload

    response = client.post("/api/mutant/", headers={"Content-Type": "application/json"}, data=payload)

    patched_human.assert_not_called()
    assert 400 == response.status_code
