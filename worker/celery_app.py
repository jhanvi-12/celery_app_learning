""" CELERY CONFIGURATION with QUEUE """
import os

import redis
from celery import Celery

# set default env variable value in settings for windows when celery is used.
os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

celery_app = Celery(__name__)
celery_app.conf.broker_url = "redis://localhost:6379/0"
celery_app.conf.result_backend = "redis://localhost:6379/0"

celery_app.conf.task_routes = {
        "worker.celery_worker.add": "add-queue",
        "worker.celery_worker.multiply": "multiply_queue",
        "worker.celery_worker.subtract": "subtract_queue",
        "worker.celery_worker.divide": "divide_queue",
        "worker.celery_worker.chain_tasks": "chain-queue",
        "worker.celery_worker.group_tasks": "group_queue"
        }

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
