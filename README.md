# Task Manager API
Simple REST API for managing tasks build with FastAPI.

## Features
- Create a task
- Get all tasks
- Delete a task
- Mark task as completed
- Automatic ID generation
- Basic input validation

## Tech Stack
- Python
- FastAPI

## How to run
1. Clone the repository:
```
git clone https://github.com/xkwiatkowski/task-manager-api
```
2. Go to project folder
```
cd task-manager-api
```
3. Create virtual environment
```
python -m venv venv
```
4. Activate virtual environment
Mac/Linux:
```
source venv/bin/activate
```
Windows:
```
venv\Scripts\activate
```
5. Install dependencies:
```
pip install -r requirements.txt
```
6. Run server:
```
uvicorn main:app --reload
```

## API Docs
Available at:
```
http://127.0.0.1:8000/docs
```
