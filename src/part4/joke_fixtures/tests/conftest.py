import os
import csv
import shutil
from pytest import fixture
from ..jokes import Joke


@fixture(autouse=True, scope="session")
def setup(request):
    tmp_dir = "tmp-test-resources"

    def cleanup():
        shutil.rmtree(tmp_dir)

    if os.path.exists(tmp_dir):
        cleanup()

    os.mkdir(tmp_dir)
    request.addfinalizer(cleanup)


@fixture
def single_joke_csv_filepath():
    tmp_file = "tmp-test-resources/single_joke.csv"
    with open(tmp_file, "w") as file:
        file.write("setup,punchline\n")
        file.write(
            "Why did the chicken cross the road?,To get to the other side."
        )
    return tmp_file


@fixture
def single_joke():
    tmp_file = "tmp-test-resources/single_joke.csv"
    with open(tmp_file, "r") as file:
        reader = csv.DictReader(file)
        jokes = [Joke(**joke) for joke in list(reader)]
        return jokes[0]


@fixture
def multiple_jokes_csv_filepath():
    tmp_file = "tmp-test-resources/multiple_jokes.csv"
    with open(tmp_file, "w") as file:
        file.write("setup,punchline\n")
        file.write(
            "Why did the chicken cross the road?,To get to the other side.\n"
        )
        file.write(
            "What do you get when you cross a snowman and a vampire?,Frostbite.\n"
        )
        file.write("How do you organize a space party?,You planet.\n")
    return tmp_file


@fixture
def jokes():
    tmp_file = "tmp-test-resources/multiple_jokes.csv"
    with open(tmp_file, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        return [Joke(**joke) for joke in data]
