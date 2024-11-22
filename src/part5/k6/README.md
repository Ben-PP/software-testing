# Simple API server that records the number of requests per second to a log file

[Poetry](https://python-poetry.org/docs/) is used to manage project dependencies.

## Install dependencies

```bash
poetry install
```

## Run the server

The following launches the server on port 8000

```bash
poetry run fastapi run server.py
```

While the server is on, it records the number of requests made to the server for every second in the file `requests_per_second_log.csv` 
