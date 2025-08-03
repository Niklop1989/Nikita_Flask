import uvicorn
from fastapi import FastAPI
from nikita.api import posts

app = FastAPI()
app.include_router(posts.router)

@app.get('/')
async def root():
    return {'messages':"welcome"}


if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)