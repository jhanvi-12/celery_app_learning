<h3 align="center">Python Coding Standards for projects</h3>

## Introduction

This document outlines the coding standards to be followed when writing Python code. Adhering to these standards ensures consistency, readability, and maintainability of the codebase.

## Table of Contents

1. [Naming Conventions](#naming-conventions)
2. [Code Formatting](#code-formatting)
3. [Documentation](#documentation)
4. [Imports](#imports)
5. [Error Handling](#error-handling)
6. [Comments](#comments)
## API documentation and response standards
7. [REST API](#rest-api)
8. [REST API Responses](#rest-api-responses)

## Naming Conventions
  
- **Variables**: Use lowercase letters with underscores to separate words (snake_case).
  ```python
  my_variable = 42

- **Functions and Methods**: Use lowercase letters with underscores to separate words (snake_case).
  ```python
  def my_function():
    pass

- **Constants**: Use uppercase letters with underscores to separate words (UPPER_CASE)
  ```python
  MAX_RETRY = 3

## Code Formatting
- **Indentation**: Use 4 spaces for indentation. Do not use tabs.
- **Line Length**: Limit lines to 79 characters to ensure readability.
- **Whitespace**: Use whitespace to improve readability, but avoid excessive spaces.

## Documentation
- **Docstrings**: Include docstrings for all modules, classes, functions, and methods
  ```python
  def my_function(param1, param2):
    """
    Brief description of the function.

    More detailed description if necessary.

    :param param1: Description of param1.
    :param param2: Description of param2.
    :return: Description of return value.
    """
    pass

## Imports
- **Import Style**: Use absolute imports wherever possible.
  ```python
  # Correct
  import module_name

  # Avoid
  from package import module_name

## Error Handling
- **Explicit is better than implicit**: Always catch specific exceptions rather than using a bare except.
- **Handle Exceptions Gracefully**: Gracefully handle exceptions and provide meaningful error messages.

## Comments
- **Use comments to explain non-obvious code**: Comments should explain why the code is written in a particular way, not what the code does.

## The critical points are:

 * Use spaces; never use tabs
 * 4 space indentation
 * 79 character line limit
 * Variables, functions and methods should be lower_case_with_underscores
 * Classes are TitleCase

## REST API
 * There are some points we need to take care while creating APIs. below are the points that we need to take care. 

 * API URL must have content version number for manage versioning of APIs. Here is the example of versions define into URL: 
    https://www.apiexample.com/v1/users 

    Create routing with standard methods.  

 * Example of Methods Routes: 

    - **Create** -> https://www.apiexample.com/v1/user/ 

    - **Show Details** -> https://www.apiexample.com/v1/user/{id}/ 

    - **Update** -> https://www.apiexample.com/v1/user/{id}/ 

    - **Listing**-> https://www.apiexample.com/v1/users 

## REST API Responses
- **1)  Success Response** :- 
    The API response must be content three variables
 
    1.Status

    2.Message 

    3.Data 
  ```python
     example of response: 

      {
        "status": "Success",  
        "message": "Data retrieved successfully" ,  
        "data": {  
                "id": 1,  
                "name": "Python framework",  
                "type": "post",  
                "image": "",
        } 
      }

- **2) Error Response** :-
    The API response content three variables
    1.Status 

    2.Data 

    3.Error Message
    ```python
    example of response: 
      {   
        "status": "Error", 
        "data": None,
        "message": "Something bad happened :(",  
        "description" : "More details about the error here"   
      } 

## Project Structure.

```
newspicking-backend
├─ apps
│  ├─ api
│  │  ├─ articles
│  │  │  ├─ article_response.py
│  │  │  ├─ models
│  │  │  │  ├─ attribute.py
│  │  │  │  ├─ method.py
│  │  │  │  ├─ model.py
│  │  │  │  └─ relationship.py
│  │  │  ├─ response.py
│  │  │  ├─ schema.py
│  │  │  ├─ service.py
│  │  │  ├─ test.py
│  │  │  └─ view.py
│  │  ├─ auth
│  │  │  ├─ models
│  │  │  │  ├─ attribute.py
│  │  │  │  ├─ method.py
│  │  │  │  ├─ model.py
│  │  │  │  └─ relationship.py
│  │  │  ├─ response.py
│  │  │  ├─ schema.py
│  │  │  ├─ service.py
│  │  │  ├─ test.py
│  │  │  └─ view.py
│  │  ├─ channels
│  │  │  ├─ models
│  │  │  │  ├─ attribute.py
│  │  │  │  ├─ method.py
│  │  │  │  ├─ model.py
│  │  │  │  └─ relationship.py
│  │  │  ├─ response.py
│  │  │  ├─ schema.py
│  │  │  ├─ service.py
│  │  │  ├─ test.py
│  │  │  └─ view.py
│  │  └─ core
│  │     ├─ db_attribute.py
│  │     ├─ db_methods.py
│  │     └─ validation.py
│  ├─ constant
│  │  └─ constant.py
│  ├─ utils
│  │  ├─ backgroundtask.py
│  │  ├─ elastic_search_config.py
│  │  ├─ helper.py
│  │  ├─ message.py
│  │  ├─ oauth2.py
│  │  ├─ s3.py
│  │  ├─ signer.py
│  │  ├─ sso.py
│  │  └─ standard_response.py
│  └─ _init_.py
├─ asgi.py
├─ assets
│  └─ templates
│     ├─ reset_pswd.html
│     └─ welcome.html
├─ CODINGSTANDARD.md
├─ config
│  ├─ aws_config.py
│  ├─ cors.py
│  ├─ database.py
│  ├─ elasticsearch_config.py
│  ├─ env_config.py
│  ├─ jwt.py
│  ├─ mail.py
│  ├─ middleware.py
│  ├─ project_path.py
│  ├─ routes.py
│  ├─ social_login.py
│  └─ template_config.py
├─ cron.py
├─ Dockerfile
├─ GITSTANDARD.md
├─ logging.conf
├─ pylint_output.txt
├─ README.md
├─ requirements.txt
├─ run.py
├─ scheduler
│  ├─ requirements.txt
│  ├─ scheduler_job.py
│  ├─ scheduler_vj.py
│  └─ wsgi.py

```