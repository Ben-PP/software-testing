import os
from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI, HTTPException
from databases import Database
from pydantic import BaseModel
from model import QuestionAnswerOption

# Database setup
database_url = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///./app.db')
database = Database(database_url)

with open('tables.sql', encoding="utf8") as f:
    init_sql = f.read()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print('Connected to database')
    for statement in init_sql.split(';'):
        # Database execute does not support multiple statements in a query
        if statement.strip():
            await database.execute(statement)
    print('Initialized database')
    yield
    print('Disconnecting from database')
    await database.disconnect()


# Data transfer objects

class QuestionAnswerOptionDto(BaseModel):
    id: int
    question_id: int
    option_text: str
    is_correct: bool
    explanation_text: str


class QuestionDto(BaseModel):
    id: int
    exercise_id: int
    title: str
    question_text: str
    options: list[QuestionAnswerOptionDto]
    max_points: int

# Service functions


async def find_question_by_uuid(exercise_uuid) -> QuestionDto | None:
    ''' Find a question and its answer options by its id '''

    question_query = '''
        SELECT q.*, e.max_points FROM questions q
        JOIN exercises e ON q.exercise_id = e.id
        WHERE e.uuid = :exercise_uuid
    '''

    question = await database.fetch_one(question_query, {'exercise_uuid': exercise_uuid})
    if question is None:
        return None
    question_options_query = QuestionAnswerOption.__table__.select().where(  # type: ignore
        QuestionAnswerOption.question_id == question.id)  # type: ignore
    options = await database.fetch_all(question_options_query)

    return QuestionDto(
        id=question.id,  # type: ignore
        exercise_id=question.exercise_id,  # type: ignore
        title=question.title,  # type: ignore
        question_text=question.question_text,  # type: ignore
        options=[QuestionAnswerOptionDto(
            id=option.id,  # type: ignore
            question_id=option.question_id,  # type: ignore
            option_text=option.option_text,  # type: ignore
            is_correct=option.is_correct,  # type: ignore
            explanation_text=option.explanation_text  # type: ignore
        ) for option in options],
        max_points=question.max_points  # type: ignore
    )


# Routes
router = APIRouter()


@router.get('/question/{uuid}')
async def get_question(uuid: str) -> QuestionDto:
    print(f'Getting question with exercise uuid {uuid}')
    question = await find_question_by_uuid(uuid)
    if question is None:
        raise HTTPException(status_code=404, detail='Question not found')
    return question


# App
app = FastAPI(lifespan=lifespan)
app.include_router(router)
