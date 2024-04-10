from fastapi import FastApi, status
import uvicorn

api = FastApi(

    title="ETICApi"
)

@api.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return datetime.datetime.now()

if __name__== "__main__":
    uvicorn.run(
        app=api,
        host="0.0.0.0",
        port=8000,
        reload=True
    )