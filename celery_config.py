""" Celery configuration. """

from datetime import datetime as dt
from os import environ

result_backend = environ.get('CELERY_RESULT_BACKEND')
imports = ["application.tasks"]
result_expires = 30
timezone = "Europe/London"

accept_content = ["json", "msgpack", "yaml"]
task_serializer = "json"
result_serializer = "json"
