from fastapi import FastAPI
from app.users.api import user_router
import uvicorn

app = FastAPI()
app.include_router(user_router)




if __name__ == "__main__":
    uvicorn.run(app = "main:app", host="localhost", port=8003, reload=True)
