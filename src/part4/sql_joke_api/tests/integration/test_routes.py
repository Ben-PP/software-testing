import pytest
from fastapi.testclient import TestClient
from tests.data_builder import DataBuilder

pytestmark = pytest.mark.anyio


async def test_get_question_returns_question_with_answer_options_and_max_points(test_client: TestClient, test_data_builder: DataBuilder):
    exercise = await test_data_builder.exercise(kind="question", max_points=10)
    question = await test_data_builder.question(exercise_id=exercise.id, title="Test title", question_text="What is love?")
    option1 = await test_data_builder.question_answer_option(question_id=question.id, is_correct=True, option_text="Baby don't hurt me", explanation_text="No more")
    option2 = await test_data_builder.question_answer_option(question_id=question.id)
    option3 = await test_data_builder.question_answer_option(question_id=question.id)

    response = test_client.get(f"/question/{exercise.uuid}")

    assert response.status_code == 200
    question_data = response.json()

    # Sort the options by id to prevent test failures due to different order of options
    assert "options" in question_data
    question_data["options"] = sorted(question_data["options"], key=lambda x: x["id"])

    assert question_data == {
        "id": question.id,
        "exercise_id": question.exercise_id,
        "title": question.title,
        "question_text": question.question_text,
        "options": sorted([
            {
                "id": option1.id,
                "question_id": question.id,
                "option_text": option1.option_text,
                "is_correct": option1.is_correct,
                "explanation_text": option1.explanation_text,
            },
            {
                "id": option2.id,
                "question_id": question.id,
                "option_text": option2.option_text,
                "is_correct": option2.is_correct,
                "explanation_text": option2.explanation_text,
            },
            {
                "id": option3.id,
                "question_id": question.id,
                "option_text": option3.option_text,
                "is_correct": option3.is_correct,
                "explanation_text": option3.explanation_text,
            },
        ], key=lambda x: x["id"]),
        "max_points": exercise.max_points,
    }
