from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

tasks: List[Task] = []

@app.get("/")
def root():
    return {"message": "API is working!"} 

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return task
