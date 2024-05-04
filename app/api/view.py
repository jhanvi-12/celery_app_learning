"""This module is used to defines endpoint for the celery tasks."""
from fastapi_utils.inferring_router import InferringRouter

from app.api.service import get_add_task_service, get_user_data, get_group_task_service
from worker.celery_worker import add, chain_tasks, group_tasks

router = InferringRouter()

@router.post("/add")
async def add_numbers(x: int, y: int):
    """This function is responsible for processing the celery task."""
    result = add.delay(x,y)
    response = get_add_task_service(result)
    return response

@router.post("/chain/task")
async def get_chain_task(num1: int, num2: int):
    """This is the API method for getting chain tasks from celery."""
    result = chain_tasks(num1, num2)
    response = get_add_task_service(result)
    return response

@router.post("/register")
async def add_user(body: dict):
    """This API is used to create a new user using redis queue."""
    response = get_user_data(body)
    return response

@router.post("/group/task")
async def get_group_task(num1: int, num2: int):
    """This is the API method for getting the group tasks from celery."""
    result = group_tasks(num1, num2)
    response = get_group_task_service(result)
    return response
