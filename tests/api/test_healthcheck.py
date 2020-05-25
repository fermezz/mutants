def test_healthcheck_returns_200(client):

    response = client.get("/api/healthcheck/")

    assert 200 == response.status_code
    assert not response.data
