"""This module is used to create a service functions."""
import json
import time

import requests
from celery.result import AsyncResult
from fastapi import status

from app.constant import constant
from app.utils.standard_response import StandardResponse
from worker.celery_app import redis_client


def get_add_task_service(result):
    """This function is used to get the add task service."""
    response = AsyncResult(result.id)
    while not response.ready():
        time.sleep(2)
        print("Waiting for celery task to finish!!")
    return StandardResponse(
        status.HTTP_200_OK,
        result.id,
        result.status
    ).make

def get_user_data(body: dict):
    """This function is used to push the user data into the
    redis queue and pop user data one bu one to proccessed further.
    params: 
        body: dict
    response:
        standard response object."""
    body_dict = json.dumps(body)
    redis_client.lpush('data_queue', body_dict)
    while True:
        data = redis_client.rpop("data_queue")
        if data is None:
            break
        else:
            res = json.loads(data)
            print("data_queue", res)
            # Implement your logic here to create user or any other.
            response = requests.post("https://reqres.in/api/users",
                                     params=res, timeout=20)
            return StandardResponse(
                status.HTTP_200_OK,
                response.json(),
                constant.USER_CREATED
            ).make

def get_group_task_service(result):
    """This function is used to provide the response status of the celery group task"""
    if result:
        data = {"Result": result.get()}
        return StandardResponse(
            status.HTTP_200_OK,
            data,
            constant.INFO_FETCHED
        ).make
    else:
        return StandardResponse(
            status.HTTP_400_BAD_REQUEST,
            None,
            constant.ERROR_OCCURED
        ).make