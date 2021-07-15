# uvicorn server:app --port 3005
from typing import Optional,List
from fastapi import FastAPI,BackgroundTasks,Request,UploadFile,File
from pydantic import BaseModel
import io
import os
import time
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _save_file_to_server(img, path="./public"):
    main_file_name = os.path.splitext(img.filename)[0]
    extension = os.path.splitext(img.filename)[-1]
    file_name = main_file_name+'-%s'%int(time.time())+extension
    
    file_name = os.path.join(path, file_name)

    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(img.file, buffer)

    return file_name

# upload file
#pip install python-multipart

# files
# Images a.png
# Images a.png
@app.post("/upload")
async def upload(Images: List[UploadFile] = File(...)):
    response = []
    s = time.time()
    for img in Images:
        temp_file = _save_file_to_server(img)
        response.append(temp_file)
    return {'res':response}
