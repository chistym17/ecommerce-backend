from fastapi import FastAPI
from dotenv import load_dotenv


from routes.create_product import router as create_product_router
from routes.get_product import router as get_product_router
from routes.update_product import router as update_product_router
from routes.delete_product import router as delete_product_router




load_dotenv()
app = FastAPI()


app.include_router(create_product_router)
app.include_router(get_product_router)
app.include_router(update_product_router)
app.include_router(delete_product_router)



@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)
