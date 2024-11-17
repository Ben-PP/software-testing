from fastapi.testclient import TestClient


class TestJokeApi:
    def test_get_health_response_is_200(self, client: TestClient):
        response = client.get("/health")
        assert response.status_code == 200

    def test_get_random_joke_returns_a_joke(
        self, client: TestClient, test_jokes: list[dict]
    ):
        response = client.get("/joke/random")
        joke = response.json()

        assert response.status_code == 200
        assert joke in test_jokes

    def test_get_all_jokes_returns_all_jokes(
        self, client: TestClient, test_jokes: list[dict]
    ):
        response = client.get("/joke/all")
        jokes = response.json()

        assert response.status_code == 200
        assert jokes == test_jokes

    def test_get_joke_by_id_returns_correct_joke(
        self, client: TestClient, test_jokes: list[dict]
    ):
        for joke in test_jokes:
            response = client.get(f"/joke/{joke['id']}")
            assert response.status_code == 200
            assert response.json() == joke
