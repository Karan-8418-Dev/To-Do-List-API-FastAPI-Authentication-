from fastapi import FastAPI
from . import models
from .database import engine
from .routers import todos, users
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Todo API", description="A simple Todo API with authentication")

app.include_router(users.router, tags=["users"])
app.include_router(todos.router, tags=["todos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)