from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Project Management API is running 🚀"}