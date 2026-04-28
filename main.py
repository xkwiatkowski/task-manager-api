from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int | None = None
    title: str
    done: bool = False

    @field_validator("title")
    def title_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

tasks: List[Task] = []

@app.get("/")
def root():
    return {"message": "API is working!"} 

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": f"Task with id {task_id} deleted."}

@app.put("/tasks/{task_id}")
def mark_done(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return {"message": f"Task with id {task_id} marked as done."}
    return {"message": f"Task with id {task_id} not found."}
