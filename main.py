# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Load JSON data
with open("q-vercel-python.json", "r") as file:
    data = {student["name"]: student["marks"] for student in json.load(file)}

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: list[str] = Query([])):
    # Retrieve marks for each name in the query
    marks = [data.get(student, "Not Found") for student in name]
    return {"marks": marks}
