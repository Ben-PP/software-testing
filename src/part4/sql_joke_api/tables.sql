CREATE TABLE exercises (
    id INTEGER PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE,
    kind VARCHAR(256) NOT NULL,
    max_points INTEGER
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises(id),
    title VARCHAR(256) NOT NULL,
    question_text TEXT NOT NULL
);

CREATE TABLE question_answer_options (
    id INTEGER PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id),
    option_text TEXT NOT NULL,
    is_correct BOOLEAN,
    explanation_text TEXT
);
