from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from collections import deque
from threading import Lock
import os

# This will store timestamps of the requests
request_times = deque()
# Lock to ensure thread safety
lock = Lock()

# File to log requests per second
LOG_FILE_PATH = os.environ.get(
    "REQUESTS_PER_SECOND_LOG_FILE", "requests_per_second_log.csv")

# Ensure the log file is created or cleared when the app starts
if not os.path.exists(LOG_FILE_PATH):
    with open(LOG_FILE_PATH, "w") as f:
        f.write("seconds_since_start,requests_per_second\n")


# Background task to write the number of requests per second to a file
def log_requests_per_second():
    iteration = 1
    while True:
        time.sleep(1)
        current_time = time.time()

        # Remove timestamps that are more than 1 second old
        with lock:
            while request_times and request_times[0] < current_time - 1:
                request_times.popleft()

            requests_per_second = len(request_times)
        # Print the result to the console
        print(
            f"\rCurrently receiving {requests_per_second} requests per second. For history, see {LOG_FILE_PATH}" + "  ", end="")

        # Write the result to the file
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"{iteration},{requests_per_second}\n")

        iteration += 1


# Start background task on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    import threading
    # Start logging thread
    logging_thread = threading.Thread(
        target=log_requests_per_second, daemon=True)
    logging_thread.start()

    yield


# Disable access logs
logging.getLogger("uvicorn.access").addFilter(lambda record: False)

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.middleware("http")
async def record_request_time(request: Request, call_next):
    start_time = time.time()
    with lock:
        request_times.append(start_time)
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hello load testing!"}
