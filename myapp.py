from hindiwsd import hindi_wsd  
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import shutil
import json
from contextlib import suppress

# print(hindi_wsd.wordsense("सीफ वल कप के फाइनल में "))   

# with open(".venv\destination.json",encoding='utf8') as json_file:
#         data = json.loads(json_file.read())
        
# transcript=data['transcription']
# print(transcript)

app=FastAPI()

@app.post("/")
def spellcollector(file: UploadFile = File(...)):
    # if(language=="hindi"):
    # model=modelload(language)
    with open(".venv\destination.json", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    with open(".venv\destination.json",encoding='utf8') as json_file:
        data = json.loads(json_file.read())
    transcript=data['transcription']['jointpara']
    sol=[]
    with suppress(UnicodeDecodeError):
        # for i in transcript:
            hindi_wsd.wordsense(transcript)
    filez=open("test.txt",encoding="utf-8")
            # sol.append(filez.read())
    return filez.read()