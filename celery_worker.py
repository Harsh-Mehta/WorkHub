from os import getenv
from application import celery, init_app

app = init_app()
app.app_context().push()
