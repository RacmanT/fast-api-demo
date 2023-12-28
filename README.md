# FastAPI demo 
## _A simple CRUD web app_

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 

## Setup

Using the `.env.default` file as a template populate a `.env` file with the appropiate values.

Spin up the db: ``` docker-compose up -d```

Initialize a virtual environment and install the dependencies:
```
poetry shell
poetry install
```
Spin up the app: `uvicorn main:app [--reload]`

## TODOs

- [x] Initialize the web app
- [ ] Add basic CRUD operations persisting on PostgresDb
- [ ] Error responses handling
- [ ] JWT Authentication
- [ ] Unit testing
- [ ] Containerize the app
- [ ] CI/CD pipeline using Github Actions
- [ ] Kubernetes deployment (?)