"""This module perform celery worker tasks."""
import time
from celery import chain, group

from worker.celery_app import celery_app

@celery_app.task(name="add-task", queue="add_queue")
def add(x: int, y: int):
    """This function is used to add the number using celery."""
    print(f"Addition of {x, y}: ---> {x + y}")
    return x + y

@celery_app.task(name="mul-task", queue="multiply_queue")
def multiply(num1: int, num2: int):
    """This function multiply the number of elements."""
    print(f"Multiplication of {num1, num2} are:--> {num1 * num2}")
    return num1 * num2

@celery_app.task(name="sub-task", queue="subtract_queue")
def subtract(num1:float, num2: int):
    """This function subtract the number of elements"""
    print(f"Subtraction of {num1, num2} are:---> {num1 - num2}")
    return num1 - num2

@celery_app.task(name="div-task", queue="divide_queue")
def divide(num1: int, num2: int):
    """This function divide the number of elements"""
    print(f"Division of {num1, num2} are:---> {num1 / num2}")
    return num1 / num2

@celery_app.task(queue="chain-queue", name="chain-queue")
def chain_tasks(num1: int, num2: int):
    """This function returns a list of tasks for a given numbers.
    When we chain tasks together, the second task 
    will take the results of the first task as its first argument"""
    res = chain(add.s(num1, num2).set(queue="add_queue"),
                multiply.s(num2).set(queue="multiply_queue"),
                divide.s(num2).set(queue="divide_queue"),
                subtract.s(num2).set(queue="subtract_queue"),).delay()
    print(res.status, res.parent.status, res.parent.parent.status)
    return res

@celery_app.task(name="group-task", queue="group_queue")
def group_tasks(num1: int, num2: int):
    """This function is used to group tasks together.
    Groups are used to execute tasks in parallel"""
    data = group([
        add.s(num1, num2),
        add.s(num2, num2)
    ]).delay()
    time.sleep(2)
    print("Result of group task: -->" ,data.id, data.ready(), data.get())
    return data
