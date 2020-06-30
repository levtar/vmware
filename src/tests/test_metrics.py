from vmware_exporter import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_metrics_response_200(client):
    response = client.get('/metrics')
    # Assert /metrics URL responding 200
    assert response.status_code == 200


def test_http_404(client):
    client = app.test_client()
    # Assert that application responding 404 on not found URL
    response = client.get('/not-found')
    assert response.status_code == 404
    # Assert that application keeps forking after returning the error 404
    response = client.get('/metrics')
    assert response.status_code == 200


def test_metrics_response(client):
    response = client.get('/metrics')
    # Assert the required metrics are returned
    assert b'sample_external_url_up' in response.data
    assert b'sample_external_url_response_ms' in response.data
