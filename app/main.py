from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()



app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
