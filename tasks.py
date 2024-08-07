

from celery import Celery

from config import task_queues, task_routes

app = Celery(
    main="tasks", broker="pyamqp://guest@localhost//", backend="redis://localhost:6379"
)
app.conf.task_queues = task_queues
app.conf.task_routes = task_routes


@app.task(bind=True)
def preprocess_video(self):
    try:
        print("Preprocessing video...")
        # Add preprocessing code here
    except Exception as exc:
        self.retry(exc=exc)


@app.task(bind=True)
def check_moderation(self):
    try:
        print("Performing moderation check...")
        # Add moderation check code here
    except Exception as exc:
        self.retry(exc=exc)


@app.task(bind=True)
def remove_background(self):
    try:
        print("Removing background...")
        # Add background removal code here
    except Exception as exc:
        self.retry(exc=exc)


@app.task(bind=True)
def perform_analysis(self):
    try:
        print("Performing analysis...")
        # Add analysis code here
    except Exception as exc:
        self.retry(exc=exc)


@app.task(bind=True)
def create_internal_assets(self):
    try:
        print("Creating internal assets...")
        # Add code to create internal assets here
    except Exception as exc:
        self.retry(exc=exc)
