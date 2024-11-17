from databases import Database
from databases.interfaces import Record
from uuid import uuid4
from tests.util import random_alphanumeric_string
from random import randint
from model import Exercise, Question, QuestionAnswerOption


class DataBuilder:
    def __init__(self, database: Database):
        self.database = database

    async def _create(self, query: str, values: dict) -> Record:
        created = await self.database.fetch_one(query, values)
        if not created:
            raise ValueError("Could not create record")
        return created

    async def exercise(self, kind: str, max_points: int) -> Exercise:
        return await self._create(
            "INSERT INTO exercises (uuid, kind, max_points) VALUES (:uuid, :kind, :max_points) RETURNING *",
            {"uuid": str(uuid4()), "kind": kind, "max_points": max_points},
        )

    async def question(
        self, exercise_id: int, title: str, question_text: str
    ) -> Question:
        return await self._create(
            "INSERT INTO questions (title, question_text, exercise_id) VALUES (:title, :question_text, :exercise_id) RETURNING *",
            {
                "title": title,
                "question_text": question_text,
                "exercise_id": exercise_id,
            },
        )

    async def question_answer_option(
        self,
        question_id: int,
        is_correct: bool = False,
        option_text: str = "Incorrect option",
        explanation_text: str = "No explanation",
    ) -> QuestionAnswerOption:
        return await self._create(
            "INSERT INTO question_answer_options (question_id, is_correct, option_text, explanation_text) VALUES (:question_id, :is_correct, :option_text, :explanation_text) RETURNING *",
            {
                "question_id": question_id,
                "is_correct": is_correct,
                "option_text": option_text,
                "explanation_text": explanation_text,
            },
        )
