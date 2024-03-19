from fastapi import FastAPI
from tasks import generate_text

app = FastAPI()

@app.post("/generate-text/")
async def generate(text: str):
    task = generate_text.delay(text)
    return {"task_id": task.id}
