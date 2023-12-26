from fastapi import FastAPI

from .routers import users, sections, courses

app = FastAPI()

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
