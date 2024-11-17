from unittest.mock import MagicMock, patch, Mock, call, ANY
from .joke_app import get_random_joke, print_random_joke, Joke
from io import StringIO


class TestJokeApp:

    @patch("requests.get")
    def test_get_random_joke_called_with_correct_url(
        self, mocker_http_get: MagicMock
    ) -> None:
        mocker_http_get.return_value.json = MagicMock(
            return_value={
                "id": 1,
                "setup": "Why did the chicken cross the road?",
                "punchline": "To get to the other side.",
            }
        )
        get_random_joke()

        mocker_http_get.assert_called_once_with(
            "https://opencs.it.jyu.fi/joke-api/joke/random"
        )

    @patch("joke_app.joke_app.get_random_joke")
    @patch("joke_app.joke_app.sleep")
    def test_print_random_joke_console_output(
        self,
        sleep_mock: MagicMock,
        get_random_joke_mock: MagicMock,
        monkeypatch,
    ) -> None:
        punchline = "To get to the other side."
        setup_line = "Why did the chicken cross the road?"
        get_random_joke_mock.return_value = Joke(
            id=1,
            setup=setup_line,
            punchline=punchline,
        )
        print_stream = StringIO()
        monkeypatch.setattr("sys.stdout", print_stream)

        print_random_joke()

        assert print_stream.getvalue() == f"{setup_line}\n{punchline}\n"
        get_random_joke_mock.assert_called_once()

    @patch("joke_app.joke_app.get_random_joke")
    @patch("joke_app.joke_app.sleep")
    @patch("joke_app.joke_app.print")
    def test_print_random_joke_sleeps_between_printing(
        self,
        print_mock: MagicMock,
        sleep_mock: MagicMock,
        get_random_joke_mock: MagicMock,
        monkeypatch,
    ) -> None:
        manager = Mock()
        manager.attach_mock(sleep_mock, "sleep")
        manager.attach_mock(print_mock, "print")
        punchline = "To get to the other side."
        setup_line = "Why did the chicken cross the road?"
        get_random_joke_mock.return_value = Joke(
            id=1,
            setup=setup_line,
            punchline=punchline,
        )

        print_mock = MagicMock()
        monkeypatch.setattr("builtins.print", print_mock)

        print_random_joke()

        expected_calls = [
            call.print(ANY),
            call.sleep(ANY),
            call.print(ANY),
        ]
        assert manager.mock_calls == expected_calls
