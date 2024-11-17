from sqlmodel import SQLModel, Field


class Exercise(SQLModel, table=True):
    __tablename__ = "exercises"  # type: ignore

    id: int = Field(default=None, primary_key=True)
    uuid: str = Field(unique=True, nullable=False)
    kind: str = Field(nullable=False)
    max_points: int


class Question(SQLModel, table=True):
    __tablename__ = "questions"  # type: ignore

    id: int = Field(default=None, primary_key=True)
    exercise_id: int
    title: str = Field(nullable=False)
    question_text: str = Field(nullable=False)


class QuestionAnswerOption(SQLModel, table=True):
    __tablename__ = "question_answer_options"  # type: ignore

    id: int = Field(default=None, primary_key=True)
    question_id: int
    option_text: str = Field(nullable=False)
    is_correct: bool
    explanation_text: str
